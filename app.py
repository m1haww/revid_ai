from quart import Quart, jsonify
import os
import json

from static.music_service import MusicService
from static.text_script_service import TextScriptService
from static.video_generation_service import VideoGenerationService

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

    print("=== WEBHOOK REQUEST BODY ===")
    print(json.dumps(request_data, indent=2))
    print("===========================")
    
    return jsonify({"status": "received", "data": request_data})

@app.route('/create-video', methods=['POST', 'GET'])
async def generate_video():
    script_service = TextScriptService(OPEN_AI_API_KEY)
    script = script_service.generate_video_script(prompt)

    if not script:
        return jsonify({"error": "Failed to generate script", "success": 0})

    music_service = MusicService(RAPID_API_KEY)
    music_urls = await music_service.fetch_trending_music(count=3)

    audio_url = music_urls[0] if music_urls else None

    if not audio_url:
        return jsonify({"error": "Failed to generate audio", "success": 0})

    video_service = VideoGenerationService(REVID_API_KEY)
    video_data = await video_service.create_video_input(script, audio_url, f"{HOST}/on-video-complete")

    if video_data.get("success") == 1 and "pid" in video_data:
        return jsonify({
            "success": 1,
            "message": "Video creation initiated successfully",
            "pid": video_data["pid"],
            "webhook": video_data.get("webhook"),
            "script": script
        })

    return jsonify(video_data)

if __name__ == '__main__':
    import asyncio
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    port = int(os.environ.get("PORT", 8080))
    config.bind = [f"0.0.0.0:{port}"]
    asyncio.run(serve(app, config))