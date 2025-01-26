from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum

class ContentType(str, Enum):
    POST = "post"
    STORY = "story"
    REEL = "reel"
    TWEET = "tweet"
    VIDEO = "video"

class WorkflowStatus(str, Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    FAILED = "failed"

class WorkflowBase(BaseModel):
    content_type: ContentType
    platform: str
    content: Dict[str, Any]
    schedule_time: datetime
    metadata: Optional[Dict[str, Any]] = None

class WorkflowCreate(WorkflowBase):
    campaign_id: int

class WorkflowUpdate(BaseModel):
    content: Optional[Dict[str, Any]] = None
    schedule_time: Optional[datetime] = None
    status: Optional[WorkflowStatus] = None
    metadata: Optional[Dict[str, Any]] = None

class WorkflowInDB(WorkflowBase):
    id: int
    campaign_id: int
    status: WorkflowStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CampaignBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    status: str

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None

class CampaignInDB(CampaignBase):
    id: int
    created_at: datetime
    updated_at: datetime
    workflows: List[WorkflowInDB] = []

    class Config:
        from_attributes = True
