from sqlalchemy import Column, String, Integer, ForeignKey, JSON, Enum, DateTime, Boolean
from sqlalchemy.orm import relationship
from .base import BaseModel
import enum

class ContentType(str, enum.Enum):
    POST = "post"
    STORY = "story"
    REEL = "reel"
    TWEET = "tweet"
    VIDEO = "video"

class WorkflowStatus(str, enum.Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    FAILED = "failed"

class Platform(str, enum.Enum):
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"

class Campaign(BaseModel):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String(1000))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(50))
    workflows = relationship("Workflow", back_populates="campaign")
    content_metadata = Column(JSON)  

class Workflow(BaseModel):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    content_type = Column(Enum(ContentType))
    status = Column(Enum(WorkflowStatus))
    platform = Column(Enum(Platform))
    content = Column(JSON)
    schedule_time = Column(DateTime)
    metadata = Column(JSON)
    campaign = relationship("Campaign", back_populates="workflows")
    approvals = relationship("Approval", back_populates="workflow")

class Approval(BaseModel):
    __tablename__ = "approvals"

    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    approver_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String(50))
    comments = Column(String(1000))
    
    workflow = relationship("Workflow", back_populates="approvals")
    approver = relationship("User")

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50))
    is_active = Column(Boolean, default=True)
    
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="members")

class Team(BaseModel):
    __tablename__ = "teams"

    name = Column(String(100), nullable=False)
    description = Column(String(500))
    
    members = relationship("User", back_populates="team")
