import json
import os

class VideoPublishState:
    """Manages the state of video publishing, tracking current index"""
    
    STATE_FILE = "video_publish_state.json"
    
    @classmethod
    def get_current_index(cls) -> int:
        """Get the current video index from state file"""
        if os.path.exists(cls.STATE_FILE):
            try:
                with open(cls.STATE_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get('current_index', 0)
            except:
                return 0
        return 0
    
    @classmethod
    def set_current_index(cls, index: int):
        """Set the current video index in state file"""
        data = {'current_index': index}
        with open(cls.STATE_FILE, 'w') as f:
            json.dump(data, f)
    
    @classmethod
    def increment_index(cls, total_videos: int) -> int:
        """Increment the index and wrap around if needed"""
        current = cls.get_current_index()
        next_index = (current + 1) % total_videos
        cls.set_current_index(next_index)
        return current  # Return the index that was just used
    
    @classmethod
    def reset_index(cls):
        """Reset the index to 0"""
        cls.set_current_index(0)