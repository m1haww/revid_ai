from typing import Optional
from dataclasses import dataclass

@dataclass
class User:
    """
    User model for video publishing and account organization
    """
    id: str
    tiktok_username: Optional[str] = None
    youtube_username: Optional[str] = None
    instagram_username: Optional[str] = None
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            "id": self.id,
            "tiktok_username": self.tiktok_username,
            "youtube_username": self.youtube_username,
            "instagram_username": self.instagram_username
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create user object from dictionary"""
        return cls(
            id=data.get("id"),
            tiktok_username=data.get("tiktok_username"),
            youtube_username=data.get("youtube_username"),
            instagram_username=data.get("instagram_username")
        )
    
    def has_social_accounts(self) -> bool:
        """Check if user has any social media accounts linked"""
        return any([self.tiktok_username, self.youtube_username, self.instagram_username])
    
    def get_social_accounts(self) -> dict:
        """Get dictionary of non-null social media accounts"""
        accounts = {}
        if self.tiktok_username:
            accounts["tiktok"] = self.tiktok_username
        if self.youtube_username:
            accounts["youtube"] = self.youtube_username
        if self.instagram_username:
            accounts["instagram"] = self.instagram_username
        return accounts