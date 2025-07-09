import aiohttp
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class VideoModel:
    """Model class for video publishing across different platforms"""
    video_url: str
    thumbnail_url: str
    title: str
    description: str
    
    tiktok_privacy_level: Optional[str] = "PUBLIC_TO_EVERYONE"
    tiktok_disable_duet: Optional[bool] = False
    tiktok_disable_stitch: Optional[bool] = False
    tiktok_disable_comment: Optional[bool] = False
    tiktok_cover_timestamp_ms: Optional[int] = 1000

    youtube_tags: Optional[List[str]] = None
    youtube_category: Optional[str] = None

    instagram_caption: Optional[str] = None


video_models: List[VideoModel] = [
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/1.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/video-capture-t0000.00seg-977.png",
        title="📸 Bigfoot Just Vlogged Himself?! 😱",
        description="""Bigfoot just dropped his first vlog and… it's wild. 😂
Caught on camera deep in the forest, this legendary creature might be more tech-savvy than we thought.

👣 Watch as he documents his day, greets the camera, and takes us on a misty morning stroll through the woods. 🌲💨

1️⃣ Follow for more Bigfoot POV moments
2️⃣ Tag a friend who still doesn't believe 👀
3️⃣ Drop a 🐾 in the comments if you'd watch a whole series

Legends aren't hiding anymore—they're vlogging now. 😂🎬
#Bigfoot #DailyVlog #ViralShorts #ForestLife #CryptidTok #MistyMornings #POV""",
        youtube_tags=["Bigfoot", "DailyVlog", "ViralShorts", "ForestLife", "CryptidTok", "MistyMornings", "POV"],
        instagram_caption="📸 Bigfoot Just Vlogged Himself?! 😱 #Bigfoot #DailyVlog #ViralShorts #ForestLife #CryptidTok #MistyMornings #POV"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/2.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/video-capture-t0000.00seg-9699.png",
        title="🎥 Bigfoot Jumped Without a Parachute?!",
        description="""Bigfoot just did the unthinkable… 😳
No parachute. No plan. Just vibes. 🪂❌
One second he was filming a peaceful vlog…
Next thing you know—he's airborne. 😂💨

Is Bigfoot secretly a skydiver? Or just built different?
Either way, that landing was WILD. 💥

🔥 New Bigfoot Daily Vlog dropping every week
🐾 Hit follow for more cryptid chaos
🎬 Drop a comment if you'd jump too (or not 🫣)

#Bigfoot #NoParachute #Skydiving #ViralShorts #BigfootDailyVlog #BuiltDifferent #EpicMoments #CryptidTok""",
        youtube_tags=["Bigfoot", "NoParachute", "Skydiving", "ViralShorts", "BigfootDailyVlog", "BuiltDifferent", "EpicMoments", "CryptidTok"],
        instagram_caption="🎥 Bigfoot Jumped Without a Parachute?! 😳 #Bigfoot #NoParachute #Skydiving #ViralShorts #BigfootDailyVlog #BuiltDifferent #EpicMoments #CryptidTok"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/3.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/video-capture-t0000.00seg-5473.png",
        title="Bigfoot Motivation Speech 🗣️🐾",
        description="""When Bigfoot speaks, you listen. 🐾💬
This isn't just a cryptid in the woods — this is your daily reminder to keep going, no matter how wild the path gets. 🌲💪

"You don't need to be seen to make an impact."
"You're not lost — you're just off the grid."
🔥 Raw. Real. Relatable.

This is the motivation you didn't know you needed… from the most unexpected life coach. 😤🌿

🎤 Bigfoot delivers straight wisdom from the forest floor
🧠 No filters. No fluff. Just facts.
🐾 Tag someone who needs to hear this today

#Bigfoot #Motivation #DailyVlog #BigfootWisdom #ForestTalks #MindsetShift #CryptidTok #FYP #StayWild""",
        youtube_tags=["Bigfoot", "Motivation", "DailyVlog", "BigfootWisdom", "ForestTalks", "MindsetShift", "CryptidTok", "FYP", "StayWild"],
        instagram_caption="Bigfoot Motivation Speech 🗣️🐾 #Bigfoot #Motivation #DailyVlog #BigfootWisdom #ForestTalks #MindsetShift #CryptidTok #FYP #StayWild"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/4.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/video-capture-t0000.00seg-1135.png",
        title="Bigfoot's Drone Ad 📡🐾",
        description="""Who knew Bigfoot was into tech? 👀
Introducing the most legendary drone review you've ever seen — straight from the king of the forest himself. 🐾📸

"This drone changed the way I scout trails, track footprints, and film my daily vlogs." – Bigfoot 💬

🚁 Ultra-stable in windy woods
🌲 Perfect for stealth missions
🎥 Shoots in 4K (even in fog)

If it's good enough for Bigfoot… imagine what you could do with it. 😉

📦 Order now before it vanishes
🐾 Link in bio (or just follow the scent)

#Bigfoot #DroneAd #TechTok #WildReview #BigfootApproved #ViralShorts #CryptidTech #FYP #DroneLife""",
        youtube_tags=["Bigfoot", "DroneAd", "TechTok", "WildReview", "BigfootApproved", "ViralShorts", "CryptidTech", "FYP", "DroneLife"],
        instagram_caption="Bigfoot's Drone Ad 📡🐾 #Bigfoot #DroneAd #TechTok #WildReview #BigfootApproved #ViralShorts #CryptidTech #FYP #DroneLife"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/5.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-3273.png",
        title="Bigfoot Teaches Yoga?! 🧘‍♂️🌲",
        description="""You've heard of hot yoga…
But are you ready for forest yoga with Bigfoot? 🐾🧘‍♂️

Deep in the misty woods, Bigfoot is finding inner peace one stretch at a time.
Downward Sasquatch? Nailed it.
Tree pose? He invented it. 🌳

🧘‍♂️ Join today's wild yoga session
💨 Breathe in… the moss
🐾 Stretch out… the stress

Nature's most mysterious legend just became your new wellness coach.

#Bigfoot #YogaTok #ForestFlow #DailyVlog #MindfulMoments #StretchWithSasquatch #CryptidCalm #WellnessVibes #FYP""",
        youtube_tags=["Bigfoot", "YogaTok", "ForestFlow", "DailyVlog", "MindfulMoments", "StretchWithSasquatch", "CryptidCalm", "WellnessVibes", "FYP"],
        instagram_caption="Bigfoot Teaches Yoga?! 🧘‍♂️🌲 #Bigfoot #YogaTok #ForestFlow #DailyVlog #MindfulMoments #StretchWithSasquatch #CryptidCalm #WellnessVibes #FYP"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/Capture_seong_gihun_202507070255.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-9768.png",
        title="We Are Not Horses – Squid Game S3",
        description="""He walked through ruin, not for the prize…
but for something bigger than the game. 🕊️
In a world that treated people like pawns,
he chose to protect innocence. 👶💔

"We are not horses. We are humans."
A line that shook the game.
A moment that reminded us all what's worth fighting for.

🎬 The most emotional scene in Squid Game Season 3
👶 One man. One baby. One truth.
💬 Tag someone who needs to hear this today.

#SquidGame #SquidGame3 #Player456 #WeAreHumans #DramaticEdit #CinematicShorts #FYP #NetflixEdit #EmotionalScene #PowerfulMoments""",
        youtube_tags=["SquidGame", "SquidGame3", "Player456", "WeAreHumans", "DramaticEdit", "CinematicShorts", "FYP", "NetflixEdit", "EmotionalScene", "PowerfulMoments"],
        instagram_caption="We Are Not Horses – Squid Game S3 #SquidGame #SquidGame3 #Player456 #WeAreHumans #DramaticEdit #CinematicShorts #FYP #NetflixEdit #EmotionalScene #PowerfulMoments"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/Create_a_touching_202507070305.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-3068.png",
        title="Born Into the Game – Squid Game S3",
        description="""In the middle of chaos… a new life begins. 👶💔
She didn't ask for this.
She didn't choose the game.
But in the darkest moment, she gave the world light.

A mother's strength.
A child's first breath.
Even in a place built on pain… love still finds a way.

🎬 One of the most emotional scenes in Squid Game Season 3
🕯️ Tag someone who believes in hope — even when it hurts
👶 #ProtectTheInnocent

#SquidGame #SquidGame3 #EmotionalScene #Newborn #Motherhood #HopeInDarkness #NetflixEdit #CinematicShorts #FYP #PowerfulMoments""",
        youtube_tags=["SquidGame", "SquidGame3", "EmotionalScene", "Newborn", "Motherhood", "HopeInDarkness", "NetflixEdit", "CinematicShorts", "FYP", "PowerfulMoments"],
        instagram_caption="Born Into the Game – Squid Game S3 #SquidGame #SquidGame3 #EmotionalScene #Newborn #Motherhood #HopeInDarkness #NetflixEdit #CinematicShorts #FYP #PowerfulMoments"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/Depict_player_120_202507070257.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-8733.png",
        title="Player 120's Moment of Strength – Squid Game S3",
        description="""Before the chaos…
there's silence.
Before the fight…
there's fear.

But she stood tall. 💚
In a room full of eyes, she found her purpose.
Player 120 didn't come to survive.
She came to lead. 🧠🔥

This is where her story begins.

#SquidGame #SquidGame3 #Player120 #EmotionalScene #GameTime #GreenTracksuit #ViralShorts #CourageInSilence #FYP #SquidGameEdit""",
        youtube_tags=["SquidGame", "SquidGame3", "Player120", "EmotionalScene", "GameTime", "GreenTracksuit", "ViralShorts", "CourageInSilence", "FYP", "SquidGameEdit"],
        instagram_caption="Player 120's Moment of Strength – Squid Game S3 #SquidGame #SquidGame3 #Player120 #EmotionalScene #GameTime #GreenTracksuit #ViralShorts #CourageInSilence #FYP #SquidGameEdit"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/Dramatize_jang_geumja_202507070309.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-8764.png",
        title="Jang Geum-ja's Breaking Point – Squid Game S3",
        description="""She didn't break for the games.
She didn't cry for herself.
But when it came to him…
She shattered. 💔

Player 149 gave everything to protect the ones she loved.
But in this moment, all she could offer…
was one final plea.

This is what real love looks like — even in a place built on fear.

#SquidGame #SquidGame3 #Player149 #EmotionalScene #CryingScene #NetflixEdit #SquidGameSeason3 #MotherAndSon #FYP #ViralShorts""",
        youtube_tags=["SquidGame", "SquidGame3", "Player149", "EmotionalScene", "CryingScene", "NetflixEdit", "SquidGameSeason3", "MotherAndSon", "FYP", "ViralShorts"],
        instagram_caption="Jang Geum-ja's Breaking Point – Squid Game S3 #SquidGame #SquidGame3 #Player149 #EmotionalScene #CryingScene #NetflixEdit #SquidGameSeason3 #MotherAndSon #FYP #ViralShorts"
    ),
    VideoModel(
        video_url="https://storage.googleapis.com/vucket-1/videos%20veo3/Highlight_junhee_player_202507070250.mp4",
        thumbnail_url="https://storage.googleapis.com/vucket-1/videos%20veo3/video-capture-t0000.00seg-2352.png",
        title="Please… Take Care of Our Baby – Squid Game S3",
        description="""Her body was broken…
but her heart was full of love. 💔👶
In her final breath, she didn't ask for help.
She asked for hope.

"Please take care of our baby."
Not a goodbye.
But a promise — whispered through pain, meant to outlive the game.

This is the moment that silenced everyone.

#SquidGame #SquidGame3 #EmotionalScene #FinalWords #Player222 #Motherhood #BabyInTheGame #Heartbreaking #NetflixEdit #FYP #SquidGameSeason3""",
        youtube_tags=["SquidGame", "SquidGame3", "EmotionalScene", "FinalWords", "Player222", "Motherhood", "BabyInTheGame", "Heartbreaking", "NetflixEdit", "FYP", "SquidGameSeason3"],
        instagram_caption="Please… Take Care of Our Baby – Squid Game S3 #SquidGame #SquidGame3 #EmotionalScene #FinalWords #Player222 #Motherhood #BabyInTheGame #Heartbreaking #NetflixEdit #FYP #SquidGameSeason3"
    ),
]

async def publish_video_for_user(video_url: str, thumbnail_url: str, user, api_key: str, title: str = None, description: str = None):
    """Publish video to user's social media accounts"""
    publish_url = "https://www.revid.ai/api/public/v2/publish-now"

    publish_data: dict = {
        "videoUrl": video_url
    }

    if user.tiktok_username:
        publish_data["tiktok"] = {
            "username": user.tiktok_username,
            "title": title or "Check out Face AI - Transform your selfies with AI!",
            "privacy_level": "PUBLIC_TO_EVERYONE",
            "disable_duet": False,
            "disable_stitch": False,
            "disable_comment": False,
            "brand_organic_toggle": False,
            "brand_content_toggle": False,
            "discloseContent": False,
            "tiktokCoverTimestampMs": 1000
        }

    if user.youtube_username:
        publish_data["youtube"] = {
            "username": user.youtube_username,
            "title": title or "Face AI - AI-Powered Photo Enhancement",
            "description": description or "Transform your selfies with Face AI! Create professional headshots and apply unique visual effects using artificial intelligence. Perfect for profile pictures and creative photo editing.",
            "thumbnailUrl": thumbnail_url or "https://cdn.revid.ai/thumbnails/default_thumbnail.jpeg"
        }

    if user.instagram_username:
        publish_data["instagram"] = {
            "username": user.instagram_username,
            "title": "Transform your photos with Face AI ✨",
            "thumbnailUrl": thumbnail_url or "https://cdn.revid.ai/thumbnails/default_thumbnail.jpeg"
        }

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