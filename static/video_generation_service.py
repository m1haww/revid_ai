import requests
from typing import Dict, Any
import json
from static.music_service import MusicService



class VideoGenerationService:
    def __init__(self, api_key):
        self.api_url = "https://www.revid.ai/api/public/v2/render"
        self.api_key = api_key
        
    async def create_video_input(
        self,
        input_text: str,
        audio_url: str,
        webbook_url: str,
    ) -> Dict[str, Any]:
        
        if not audio_url:
            return {"success": 0, "error": "No music URL available"}

        payload = {
            "webhook": webbook_url,
            "creationParams": {
                "targetDuration": 15,
                "ratio": "9 / 16",
                "mediaType": "movingImage",
                "inputText": input_text,
                "flowType": "text-to-video",
                "slug": "ai-ad-generator",
                "slugNew": "",
                "isCopiedFrom": False,
                "hasToGenerateVoice": True,
                "hasToTranscript": False,
                "hasToSearchMedia": True,
                "hasAvatar": False,
                "hasWebsiteRecorder": False,
                "hasTextSmallAtBottom": False,
                "selectedAudio": "Observer",
                "selectedVoice": "yl2ZDV1MzN4HbQJbMihG",
                "selectedAvatarType": "",
                "websiteToRecord": "",
                "hasToGenerateCover": False,
                "nbGenerations": 1,
                "disableCaptions": False,
                "mediaMultiplier": "medium",
                "characters": [],
                "captionPresetName": "Wrap 1",
                "captionPositionName": "bottom",
                "sourceType": "contentScraping",
                "selectedStoryStyle": {
                    "value": "custom",
                    "label": "General"
                },
                "durationSeconds": 40,
                "generationPreset": "GHIBLI",
                "hasToGenerateMusic": False,
                "isOptimizedForChinese": False,
                "generationUserPrompt": "",
                "enableNsfwFilter": False,
                "addStickers": False,
                "typeMovingImageAnim": "dynamic",
                "hasToGenerateSoundEffects": False,
                "forceModelType": "gpt-image-1",
                "selectedCharacters": [],
                "lang": "",
                "voiceSpeed": 1,
                "disableAudio": False,
                "disableVoice": False,
                "useOnlyProvidedMedia": True,
                "imageGenerationModel": "ultra",
                "videoGenerationModel": "base",
                "hasEnhancedGeneration": True,
                "hasEnhancedGenerationPro": True,
                "inputMedias": [
                    {
                        "url": "https://cdn.revid.ai/uploads/1749032740401-image.png",
                        "title": "",
                        "type": "image"
                    },
                    {
                        "url": "https://cdn.revid.ai/uploads/1749032732750-image.png",
                        "title": "",
                        "type": "image"
                    },
                    {
                        "url": "https://cdn.revid.ai/uploads/1749032761045-image.png",
                        "title": "",
                        "type": "image"
                    }
                ],
                "hasToGenerateVideos": True,
                "audioUrl": audio_url,
                "watermark": None,
                "estimatedCreditsToConsume": 10
            }
        }

        try:
            headers = {
                "Content-Type": "application/json",
                "key": self.api_key
            }

            response = requests.request(
                "POST",
                self.api_url,
                headers=headers,
                data=json.dumps(payload)
            )

            response_data = response.json()
            print(f"Revid AI response: {response_data}")
            
            return response_data
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "status_code": getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None
            }