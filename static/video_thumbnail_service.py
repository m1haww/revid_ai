import os
import tempfile
import aiohttp
import asyncio
from urllib.parse import urlparse
import base64

class VideoThumbnailService:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
    
    async def extract_thumbnail_from_url(self, video_url):
        """
        Downloads a video from URL and extracts the first frame as a thumbnail
        Returns base64 encoded image or URL to saved thumbnail
        """
        try:
            video_path = await self._download_video(video_url)
            
            if not video_path:
                return None
            
            thumbnail_path = await self._extract_first_frame(video_path)
            
            if os.path.exists(video_path):
                os.remove(video_path)
            
            if thumbnail_path and os.path.exists(thumbnail_path):
                with open(thumbnail_path, 'rb') as f:
                    thumbnail_data = base64.b64encode(f.read()).decode('utf-8')
                
                os.remove(thumbnail_path)
                
                return {
                    'success': True,
                    'thumbnail_base64': thumbnail_data,
                    'mime_type': 'image/jpeg'
                }
            
            return None
            
        except Exception as e:
            print(f"Error extracting thumbnail: {e}")
            return None
    
    async def _download_video(self, video_url):
        """
        Downloads video from URL to temporary file
        """
        try:
            # Parse URL to get filename
            parsed_url = urlparse(video_url)
            filename = os.path.basename(parsed_url.path) or 'video.mp4'
            
            # Create temp file path
            temp_path = os.path.join(self.temp_dir, f"temp_{filename}")
            
            async with aiohttp.ClientSession() as session:
                async with session.get(video_url) as response:
                    if response.status == 200:
                        with open(temp_path, 'wb') as f:
                            while True:
                                chunk = await response.content.read(1024 * 1024)  # 1MB chunks
                                if not chunk:
                                    break
                                f.write(chunk)
                        return temp_path
            
            return None
            
        except Exception as e:
            print(f"Error downloading video: {e}")
            return None
    
    async def _extract_first_frame(self, video_path):
        """
        Extracts first frame from video using ffmpeg
        """
        try:
            thumbnail_path = video_path.replace('.mp4', '_thumbnail.jpg')
            
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-vframes', '1',  # Extract only 1 frame
                '-f', 'image2',
                '-y',  # Overwrite output file if exists
                thumbnail_path
            ]
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0 and os.path.exists(thumbnail_path):
                return thumbnail_path
            else:
                print(f"FFmpeg error: {stderr.decode()}")
                return None
                
        except Exception as e:
            print(f"Error extracting frame: {e}")
            return None
    
    async def extract_thumbnail_with_imageio(self, video_url):
        """
        Alternative method using imageio-ffmpeg if ffmpeg is not available
        """
        try:
            import imageio
            import numpy as np
            from PIL import Image
            
            # Download video
            video_path = await self._download_video(video_url)
            if not video_path:
                return None
            
            # Read first frame
            reader = imageio.get_reader(video_path)
            first_frame = reader.get_data(0)
            reader.close()
            
            # Convert to PIL Image
            image = Image.fromarray(first_frame)
            
            # Save as JPEG
            thumbnail_path = video_path.replace('.mp4', '_thumbnail.jpg')
            image.save(thumbnail_path, 'JPEG', quality=85)
            
            # Clean up video
            os.remove(video_path)
            
            # Read and encode
            with open(thumbnail_path, 'rb') as f:
                thumbnail_data = base64.b64encode(f.read()).decode('utf-8')
            
            os.remove(thumbnail_path)
            
            return {
                'success': True,
                'thumbnail_base64': thumbnail_data,
                'mime_type': 'image/jpeg'
            }
            
        except Exception as e:
            print(f"Error with imageio method: {e}")
            return None