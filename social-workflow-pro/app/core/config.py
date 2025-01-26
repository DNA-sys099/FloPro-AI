from pydantic_settings import BaseSettings
from typing import Optional
import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "Social Workflow Pro"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = "sqlite:///./social_workflow.db"
    
    # Social Media API Credentials (Free Platforms Only)
    FACEBOOK_ACCESS_TOKEN: Optional[str] = None
    INSTAGRAM_USERNAME: Optional[str] = None
    INSTAGRAM_PASSWORD: Optional[str] = None
    LINKEDIN_ACCESS_TOKEN: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
