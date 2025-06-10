from quart import Quart, jsonify
import os

from static.text_script_service import TextScriptService
from static.video_generation_service import VideoGenerationService

REVID_API_KEY = os.getenv("API_KEY", "8eb5870b-7b55-4589-87be-b6fb7752cdbe")
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
MUSIC_MS_TOKEN = os.getenv("MUSIC_MS_TOKEN",
                           "0Noq8K453yDmxVGaNjo1Ivnwo2HeGkGOmWc_avIPpzn09KB3dPSrOVyOEkyGExHAxY3D2EGOP6AzYjV5T33XC_yWR1UweYo1ZPcWMus5qnBwD-xDyB1eNkbZPfp4WR2rU8uZR4i_V4-yhZ63zowybbhe")

prompt = "Create a TikTok ad script for an iOS app called 'Face AI'. It uses artificial intelligence to enhance selfies, generate professional headshots, and apply unique visual effects. Target audience: users who want better profile pictures, resume headshots, or just enjoy playing with AI photo effects."

app = Quart(__name__)

@app.route('/', methods=['GET'])
async def hello_world():
    script_service = TextScriptService(OPEN_AI_API_KEY)
    script = script_service.generate_video_script(prompt)

    if not script:
        return jsonify({"error": "Failed to generate script", "success": 0})

    video_service = VideoGenerationService(REVID_API_KEY, MUSIC_MS_TOKEN)
    video_data = await video_service.create_video_input(script)

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
    config.bind = ["0.0.0.0:5001"]
    asyncio.run(serve(app, config))