from TikTokApi import TikTokApi
import os

class MusicService:
    def __init__(self, ms_token):
        self.ms_token = ms_token
        self.api = None

    async def fetch_trending_music(self, count=10):
        trending_data = []
        
        async with TikTokApi() as api:
            self.api = api
            await api.create_sessions(
                ms_tokens=[self.ms_token], 
                num_sessions=1, 
                sleep_after=3,
                browser=os.getenv("TIKTOK_BROWSER", "chromium")
            )
            
            async for video in api.trending.videos(count=count):
                try:
                    video_data = video.as_dict
                    
                    if not video_data.get('id') or video_data.get('id') == '':
                        continue
                    
                    sound_data = None
                    
                    if 'music' in video_data:
                        music = video_data['music']
                        if music and music.get('id'):
                            try:
                                sound = api.sound(id=music['id'])
                                sound_info = await sound.info()
                                
                                sound_data = {
                                    'id': music['id'],
                                    'title': music.get('title', sound_info.get('title', 'Unknown')),
                                    'author': music.get('authorName', sound_info.get('author', 'Unknown')),
                                    'duration': music.get('duration', sound_info.get('duration', 0)),
                                    'play_url': music.get('playUrl', sound_info.get('playUrl', '')),
                                    'cover_url': music.get('coverLarge', sound_info.get('coverUrl', ''))
                                }
                            except Exception as e:
                                print(f"Error fetching detailed sound info for {music['id']}: {e}")
                                sound_data = {
                                    'id': music['id'],
                                    'title': music.get('title', 'Unknown'),
                                    'author': music.get('authorName', 'Unknown'),
                                    'duration': music.get('duration', 0),
                                    'play_url': music.get('playUrl', ''),
                                    'cover_url': music.get('coverLarge', '')
                                }
                    
                    trending_item = {
                        'sound': sound_data
                    }
                    
                    trending_data.append(trending_item)
                    
                except Exception as e:
                    print(f"Error processing video: {e}")
                    continue
        
        return trending_data
