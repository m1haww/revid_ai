import aiohttp

async def publish_video_for_user(video_url: str, thumbnail_url: str, user, api_key: str):
    """Publish video to user's social media accounts"""
    publish_url = "https://www.revid.ai/api/public/v2/publish-now"

    publish_data: dict = {
        "videoUrl": video_url
    }

    # if user.tiktok_username:
    #     publish_data["tiktok"] = {
    #         "username": user.tiktok_username,
    #         "title": "Check out Face AI - Transform your selfies with AI!",
    #         "privacy_level": "PUBLIC_TO_EVERYONE",
    #         "disable_duet": False,
    #         "disable_stitch": False,
    #         "disable_comment": False,
    #         "brand_organic_toggle": False,
    #         "brand_content_toggle": False,
    #         "discloseContent": False,
    #         "tiktokCoverTimestampMs": 1000
    #     }

    if user.youtube_username:
        publish_data["youtube"] = {
            "username": user.youtube_username,
            "title": "Face AI - AI-Powered Photo Enhancement",
            "description": "Transform your selfies with Face AI! Create professional headshots and apply unique visual effects using artificial intelligence. Perfect for profile pictures and creative photo editing.",
            "thumbnailUrl": thumbnail_url or "https://cdn.revid.ai/thumbnails/default_thumbnail.jpeg"
        }

    # if user.instagram_username:
    #     publish_data["instagram"] = {
    #         "username": user.instagram_username,
    #         "title": "Transform your photos with Face AI ✨",
    #         "thumbnailUrl": thumbnail_url or "https://cdn.revid.ai/thumbnails/default_thumbnail.jpeg"
    #     }

    try:
        headers = {
            "Content-Type": "application/json",
            "key": api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(publish_url, json=publish_data, headers=headers) as response:
                result = await response.json()
                return {
                    "success": response.status == 200,
                    "status_code": response.status,
                    "response": result,
                    "published_to": list(user.get_social_accounts().keys())
                }
    except Exception as e:
        print(f"Error publishing video: {e}")
        return {
            "success": False,
            "error": str(e)
        }