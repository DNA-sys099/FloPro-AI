from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
from typing import Optional
from ...schemas.content import ContentCreate, ContentResponse
from ...services.content_service import ContentService

router = APIRouter()

@router.post("/upload/", response_model=ContentResponse)
async def upload_content(
    file: UploadFile = File(...),
    schedule_time: datetime = Form(...),
    platform: str = Form(...),
    caption: Optional[str] = Form(None),
    campaign_id: Optional[int] = Form(None)
):
    """
    Upload content (image/video) and schedule it for posting.
    
    - file: The media file to upload (image/video)
    - schedule_time: When to post the content
    - platform: Which platform to post to (facebook/instagram/linkedin)
    - caption: Optional text caption for the post
    - campaign_id: Optional campaign to associate with
    """
    content_service = ContentService()
    return await content_service.create_content(
        file=file,
        schedule_time=schedule_time,
        platform=platform,
        caption=caption,
        campaign_id=campaign_id
    )
