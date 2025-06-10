import aiohttp
import base64
from typing import Optional, Dict

class FileUploadService:
    def __init__(self):
        self.upload_url = "https://image-generation-backend-164860087792.us-central1.run.app/api/file/upload-file"
    
    async def upload_base64_image(self, base64_data: str, filename: str = "thumbnail.jpg") -> Optional[Dict]:
        """
        Uploads a base64 encoded image to the cloud storage API
        
        Args:
            base64_data: Base64 encoded image data
            filename: Name for the uploaded file
            
        Returns:
            Dict with upload response including the image URL, or None if failed
        """
        try:
            image_bytes = base64.b64decode(base64_data)

            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                image_bytes,
                filename=filename,
                content_type='image/jpeg'
            )

            async with aiohttp.ClientSession() as session:
                async with session.post(self.upload_url, data=form_data) as response:
                    if response.status == 200:
                        result = await response.json()
                        return {
                            'success': True,
                            'url': result.get('url') or result.get('fileUrl') or result.get('file_url'),
                            'response': result
                        }
                    else:
                        error_text = await response.text()
                        print(f"Upload failed with status {response.status}: {error_text}")
                        return None
                        
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None
    
    async def upload_file_from_bytes(self, file_bytes: bytes, filename: str, content_type: str = 'image/jpeg') -> Optional[Dict]:
        """
        Uploads file bytes directly to the cloud storage API
        
        Args:
            file_bytes: Raw file bytes
            filename: Name for the uploaded file
            content_type: MIME type of the file
            
        Returns:
            Dict with upload response including the file URL, or None if failed
        """
        try:
            # Create form data
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                file_bytes,
                filename=filename,
                content_type=content_type
            )
            
            # Upload file
            async with aiohttp.ClientSession() as session:
                async with session.post(self.upload_url, data=form_data) as response:
                    if response.status == 200:
                        result = await response.json()
                        return {
                            'success': True,
                            'url': result.get('url') or result.get('fileUrl') or result.get('file_url'),
                            'response': result
                        }
                    else:
                        error_text = await response.text()
                        print(f"Upload failed with status {response.status}: {error_text}")
                        return None
                        
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None
    
    async def upload_thumbnail_from_extraction(self, thumbnail_data: Dict) -> Optional[str]:
        """
        Convenience method to upload thumbnail data from VideoThumbnailService
        
        Args:
            thumbnail_data: Dict containing 'thumbnail_base64' from VideoThumbnailService
            
        Returns:
            The uploaded image URL or None if failed
        """
        if not thumbnail_data or not thumbnail_data.get('success'):
            return None
            
        base64_data = thumbnail_data.get('thumbnail_base64')
        if not base64_data:
            return None
            
        upload_result = await self.upload_base64_image(base64_data, "video_thumbnail.jpg")
        
        if upload_result and upload_result.get('success'):
            return upload_result.get('url')
        
        return None