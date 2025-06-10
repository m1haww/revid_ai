import requests

class MusicService:
    def __init__(self, rapidapi_key):
        self.rapidapi_key = rapidapi_key

        self.fallback_music = [
            {
                'id': 'fallback_1',
                'title': 'Upbeat Corporate',
                'author': 'Background Music',
                'duration': 30,
                'play_url': 'https://www.bensound.com/bensound-music/bensound-ukulele.mp3',
                'cover_url': ''
            }
        ]

    async def fetch_trending_music(self, count=5):
        """
        Fetches trending TikTok videos and returns a list of music MP3 URLs
        """
        try:
            url = "https://tiktok-scraper7.p.rapidapi.com/feed/search"
            
            querystring = {
                "keywords": "fyp",
                "region": "us",
                "count": str(count * 3),
                "cursor": "0",
                "publish_time": "0",
                "sort_type": "0"
            }
            
            headers = {
                "x-rapidapi-key": self.rapidapi_key,
                "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
            }
            
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            
            data = response.json()
            music_urls = []

            if data.get('data') and data['data'].get('videos'):
                videos = data['data']['videos']
                
                for video in videos:
                    if len(music_urls) >= count:
                        break

                    music_url = video.get('music')
                    
                    if music_url and isinstance(music_url, str) and music_url.startswith('http') and '.mp3' in music_url:
                        music_urls.append(music_url)

            if len(music_urls) < 1:
                print("No music found in trending videos, using fallback")
                return self._get_fallback_music_urls(1)
            
            return music_urls[:count]
            
        except Exception as e:
            print(f"Error fetching trending music from RapidAPI: {e}")
            return self._get_fallback_music_urls(count)
    
    def _get_fallback_music_urls(self, count):
        """
        Returns fallback music URLs when API fails
        """
        music_urls = []
        for i in range(min(count, len(self.fallback_music))):
            music_urls.append(self.fallback_music[i]['play_url'])
        return music_urls