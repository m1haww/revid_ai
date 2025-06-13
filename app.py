from quart import Quart, jsonify
import os
from urllib.parse import quote
from static.music_service import MusicService
from static.publish_video import publish_video_for_user
from static.text_script_service import TextScriptService
from static.video_generation_service import VideoGenerationService
from static.video_thumbnail_service import VideoThumbnailService
from static.file_upload_service import FileUploadService
from static.user_accounts import get_all_users, get_user_by_id
from static.video_metadata_service import VideoMetadataService

HOST = "https://revid-ai-57018476417.northamerica-northeast1.run.app"
REVID_API_KEY = os.getenv("API_KEY", "8eb5870b-7b55-4589-87be-b6fb7752cdbe")
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
RAPID_API_KEY = os.getenv("RAPID_API_KEY", "6f0aa73520mshfe4eacac82fb342p18af61jsn2278f0e0ff37")

prompt = "Create a TikTok ad script for an iOS app called 'Face AI'. It uses artificial intelligence to enhance selfies, generate professional headshots, and apply unique visual effects. Target audience: users who want better profile pictures, resume headshots, or just enjoy playing with AI photo effects."

app = Quart(__name__)

@app.route("/on-video-complete", methods=["POST"])
async def on_video_complete():
    from quart import request
    
    request_data = await request.get_json()
    
    user_id = request.args.get('user_id')
    video_title = request.args.get('title', 'Untitled Video')
    video_description = request.args.get('description', '')
    
    user = None
    if user_id:
        user = get_user_by_id(user_id)
    
    video_url = None
    
    if request_data.get("videoUrl"):
        video_url = request_data["videoUrl"]
    elif request_data.get("video_url"):
        video_url = request_data["video_url"]
    elif request_data.get("result", {}).get("videoUrl"):
        video_url = request_data["result"]["videoUrl"]
    elif request_data.get("data", {}).get("videoUrl"):
        video_url = request_data["data"]["videoUrl"]

    thumbnail_url = None
    
    if video_url:
        thumbnail_service = VideoThumbnailService()
        thumbnail_data = await thumbnail_service.extract_thumbnail_from_url(video_url)

        if thumbnail_data and thumbnail_data.get('success'):
            file_upload_service = FileUploadService()
            thumbnail_url = await file_upload_service.upload_thumbnail_from_extraction(thumbnail_data)

    response = {
        "status": "received",
        "video_url": video_url,
        "thumbnail_url": thumbnail_url,
        "user_id": user_id,
        "user": user.to_dict() if user else None,
        "full_data": request_data
    }
    
    if video_url:
        print(f"Video URL found: {video_url}")

        if user and user.has_social_accounts():
            publish_result = await publish_video_for_user(video_url, thumbnail_url, user, REVID_API_KEY, video_title, video_description)
            response["publish_result"] = publish_result
    
    return jsonify(response)

@app.route('/create-videos-for-all-users', methods=['POST', 'GET'])
async def create_videos_for_all_users():
    users = get_all_users()
    results = []

    script_service = TextScriptService(OPEN_AI_API_KEY)

    music_service = MusicService(RAPID_API_KEY)
    metadata_service = VideoMetadataService()

    for user in users:
        script = script_service.generate_video_script(prompt)

        if not script:
            return jsonify({"error": f"Failed to generate script for user: {user.id}", "success": 0})
        
        metadata = metadata_service.get_video_metadata(script)
        video_title = metadata["title"]
        video_description = metadata["description"]
        
        encoded_title = quote(video_title)
        encoded_description = quote(video_description)
        
        webhook_url = f"{HOST}/on-video-complete?user_id={user.id}&title={encoded_title}&description={encoded_description}"

        music_urls = await music_service.fetch_trending_music(count=3)
        audio_url = music_urls[0] if music_urls else None

        if not audio_url:
            return jsonify({"error": "Failed to generate audio", "success": 0})

        video_service = VideoGenerationService(REVID_API_KEY)
        video_data = await video_service.create_video_input(script, audio_url, webhook_url)
        
        if video_data.get("success") == 1 and "pid" in video_data:
            results.append({
                "user_id": user.id,
                "user": user.to_dict(),
                "success": 1,
                "pid": video_data["pid"],
                "webhook": video_data.get("webhook"),
                "title": video_title,
                "description": video_description
            })
        else:
            results.append({
                "user_id": user.id,
                "user": user.to_dict(),
                "success": 0,
                "error": video_data
            })
    
    return jsonify({
        "total_users": len(users),
        "results": results
    })

if __name__ == '__main__':
    import asyncio
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    port = int(os.environ.get("PORT", 8080))
    config.bind = [f"0.0.0.0:{port}"]
    asyncio.run(serve(app, config))