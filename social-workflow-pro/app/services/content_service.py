import os
from fastapi import UploadFile, HTTPException
from datetime import datetime
from typing import Optional
import aiofiles
from ..models.workflow import Workflow, Platform, ContentType

class ContentService:
    UPLOAD_DIR = "uploads"
    
    async def create_content(
        self,
        file: UploadFile,
        schedule_time: datetime,
        platform: str,
        caption: Optional[str] = None,
        campaign_id: Optional[int] = None
    ):
        """Handle content upload and scheduling"""
        
        # Create uploads directory if it doesn't exist
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)
        
        # Generate unique filename
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{datetime.now().timestamp()}{file_ext}"
        file_path = os.path.join(self.UPLOAD_DIR, unique_filename)
        
        # Save uploaded file
        async with aiofiles.open(file_path, 'wb') as out_file:
            while content := await file.read(1024):  # Read in chunks
                await out_file.write(content)
        
        # Create workflow for the content
        workflow = Workflow(
            campaign_id=campaign_id,
            content_type=self._get_content_type(file.content_type),
            platform=Platform(platform),
            schedule_time=schedule_time,
            content={
                "file_path": file_path,
                "caption": caption,
                "original_filename": file.filename
            }
        )
        
        return {
            "id": workflow.id,
            "schedule_time": schedule_time,
            "platform": platform,
            "status": "scheduled",
            "file_path": file_path
        }
    
    def _get_content_type(self, mime_type: str) -> ContentType:
        """Determine content type from MIME type"""
        if mime_type.startswith('image/'):
            return ContentType.IMAGE
        elif mime_type.startswith('video/'):
            return ContentType.VIDEO
        else:
            raise HTTPException(400, "Unsupported file type")
