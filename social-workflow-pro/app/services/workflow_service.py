from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from datetime import datetime
from ..models.workflow import Workflow, Campaign
from ..schemas.workflow import WorkflowCreate, WorkflowUpdate, CampaignCreate
from ..utils.content_analyzer import analyze_content
from ..utils.scheduler import schedule_content

class WorkflowService:
    @staticmethod
    async def create_workflow(db: Session, workflow: WorkflowCreate) -> Workflow:
        # Analyze content for optimization
        analyzed_content = await analyze_content(workflow.content)
        
        # Create workflow instance
        db_workflow = Workflow(
            campaign_id=workflow.campaign_id,
            content_type=workflow.content_type,
            status="draft",
            platform=workflow.platform,
            content=analyzed_content,
            schedule_time=workflow.schedule_time,
            metadata=workflow.metadata or {}
        )
        
        db.add(db_workflow)
        db.commit()
        db.refresh(db_workflow)
        
        # Schedule the content if it's ready
        if workflow.schedule_time:
            await schedule_content(db_workflow)
        
        return db_workflow

    @staticmethod
    def get_workflow(db: Session, workflow_id: int) -> Optional[Workflow]:
        return db.query(Workflow).filter(Workflow.id == workflow_id).first()

    @staticmethod
    def get_workflows(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        campaign_id: Optional[int] = None,
        status: Optional[str] = None
    ) -> List[Workflow]:
        query = db.query(Workflow)
        
        if campaign_id:
            query = query.filter(Workflow.campaign_id == campaign_id)
        if status:
            query = query.filter(Workflow.status == status)
            
        return query.offset(skip).limit(limit).all()

    @staticmethod
    async def update_workflow(
        db: Session,
        workflow_id: int,
        workflow_update: WorkflowUpdate
    ) -> Optional[Workflow]:
        db_workflow = WorkflowService.get_workflow(db, workflow_id)
        if not db_workflow:
            return None
            
        update_data = workflow_update.dict(exclude_unset=True)
        
        # If content is being updated, re-analyze it
        if "content" in update_data:
            update_data["content"] = await analyze_content(update_data["content"])
        
        for field, value in update_data.items():
            setattr(db_workflow, field, value)
        
        # If schedule time is updated, reschedule the content
        if "schedule_time" in update_data:
            await schedule_content(db_workflow)
        
        db.commit()
        db.refresh(db_workflow)
        return db_workflow

    @staticmethod
    def delete_workflow(db: Session, workflow_id: int) -> bool:
        db_workflow = WorkflowService.get_workflow(db, workflow_id)
        if not db_workflow:
            return False
            
        db.delete(db_workflow)
        db.commit()
        return True

class CampaignService:
    @staticmethod
    def create_campaign(db: Session, campaign: CampaignCreate) -> Campaign:
        db_campaign = Campaign(**campaign.dict())
        db.add(db_campaign)
        db.commit()
        db.refresh(db_campaign)
        return db_campaign

    @staticmethod
    def get_campaign(db: Session, campaign_id: int) -> Optional[Campaign]:
        return db.query(Campaign).filter(Campaign.id == campaign_id).first()

    @staticmethod
    def get_campaigns(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None
    ) -> List[Campaign]:
        query = db.query(Campaign)
        if status:
            query = query.filter(Campaign.status == status)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_campaign(
        db: Session,
        campaign_id: int,
        campaign_data: Dict[str, Any]
    ) -> Optional[Campaign]:
        db_campaign = CampaignService.get_campaign(db, campaign_id)
        if not db_campaign:
            return None
            
        for field, value in campaign_data.items():
            setattr(db_campaign, field, value)
            
        db.commit()
        db.refresh(db_campaign)
        return db_campaign
