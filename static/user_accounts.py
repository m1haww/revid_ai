from models.user_model import User

user_accounts = [
    User(
        id="user_001",
        tiktok_username="strawberyyg",
        youtube_username="George Straw",
        instagram_username="georgestraw022"
    ),
    User(
        id="user_002",
        tiktok_username="Michael Whitaker",
        youtube_username="Michael Whitaker",
        instagram_username="michaelwhitaker872"
    ),
    User(
        id="user_003",
        tiktok_username="face.ai.annis",
        youtube_username="Annis Laster",
        instagram_username=None
    ),
    User(
        id="user_004",
        tiktok_username="Justin Oliver",
        youtube_username="Justin Oliver",
        instagram_username=None
    ),
    User(
        id="user_005",
        tiktok_username="face.ai.floyd",
        youtube_username="Floyd Baker",
        instagram_username=None
    )
]

def get_all_users():
    """Get all user accounts"""
    return user_accounts

def get_user_by_id(user_id: str):
    """Find user by ID"""
    for user in user_accounts:
        if user.id == user_id:
            return user
    return None

def get_user_by_tiktok(username: str):
    """Find user by TikTok username"""
    for user in user_accounts:
        if user.tiktok_username == username:
            return user
    return None

def get_user_by_youtube(username: str):
    """Find user by YouTube username"""
    for user in user_accounts:
        if user.youtube_username == username:
            return user
    return None

def get_user_by_instagram(username: str):
    """Find user by Instagram username"""
    for user in user_accounts:
        if user.instagram_username == username:
            return user
    return None

def add_user(user: User):
    """Add a new user to the list"""
    user_accounts.append(user)