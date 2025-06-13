from g4f.client import Client
import logging
import json

class VideoMetadataService:
    def __init__(self):
        self.client = Client()
        self.logger = logging.getLogger(__name__)

    def get_video_metadata(self, video_script):
        """Generate both title and description in a single AI call"""
        if not video_script or not video_script.strip():
            return {
                "title": "Untitled Video",
                "description": "No description available."
            }
        
        prompt = f"""You are a world-class video content creator. Generate a title and description for the following video script.

Return your response in valid JSON format with exactly this structure:
{{
    "title": "Your engaging title here (max 10 words)",
    "description": "Your beautiful description here"
}}

TITLE REQUIREMENTS:
- Maximum 10 words
- Engaging and click-worthy
- Captures the main topic
- Would attract viewers

DESCRIPTION REQUIREMENTS:
- Write a single paragraph description (NO line breaks, NO markdown formatting)
- Start with an attention-grabbing hook
- Include what viewers will discover
- Mention key benefits and value
- End with a call to action
- Use plain text only - no asterisks, no special formatting
- Make it flow naturally as one continuous text
- Include relevant hashtags at the end

Write with ENERGY and create excitement, but keep it as plain text!

VIDEO SCRIPT:
{video_script}

IMPORTANT: Return ONLY valid JSON with plain text values, no formatting:"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a JSON-only responder. Always return valid JSON with no additional text."},
                    {"role": "user", "content": prompt}
                ],
                web_search=False,
                temperature=0.7
            )

            content = response.choices[0].message.content.strip()
            # Try to parse JSON
            try:
                metadata = json.loads(content)
                # Validate and sanitize
                title = metadata.get("title", "").strip('"\'')
                if len(title) > 100:
                    title = title[:97] + "..."
                
                return {
                    "title": title or self._generate_fallback_title(video_script),
                    "description": metadata.get("description", "") or self._generate_fallback_description(video_script)
                }
            except json.JSONDecodeError:
                self.logger.error(f"Failed to parse JSON response: {content}")
                return {
                    "title": self._generate_fallback_title(video_script),
                    "description": self._generate_fallback_description(video_script)
                }
        
        except Exception as e:
            self.logger.error(f"Error generating video metadata: {str(e)}")
            return {
                "title": self._generate_fallback_title(video_script),
                "description": self._generate_fallback_description(video_script)
            }

    def get_video_title(self, video_script):
        """Generate a concise, engaging title for the video"""
        metadata = self.get_video_metadata(video_script)
        return metadata["title"]
    
    def get_video_description(self, video_script):
        """Generate an engaging description for the video"""
        metadata = self.get_video_metadata(video_script)
        return metadata["description"]
    
    def _generate_fallback_title(self, video_script):
        """Simple fallback title if AI service fails"""
        words = video_script.split()[:5]
        return ' '.join(words) + "..." if len(words) >= 5 else "Video Content"
    
    def _generate_fallback_description(self, video_script):
        """Simple fallback description if AI service fails"""
        words = video_script.split()
        word_count = len(words)
        
        preview = ' '.join(words[:50])
        description = f"This video contains {word_count} words of content. Preview: {preview}... Note: Automated description generation was unavailable. Please review the full script for details."
        
        return description