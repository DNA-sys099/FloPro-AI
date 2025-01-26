from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from ...db.session import get_db
from ...schemas.workflow import (
    WorkflowCreate,
    WorkflowUpdate,
    WorkflowInDB,
    CampaignCreate,
    CampaignInDB
)
from ...services.workflow_service import WorkflowService, CampaignService

router = APIRouter()

@router.post("/workflows/", response_model=WorkflowInDB)
async def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):
    """Create a new workflow"""
    return await WorkflowService.create_workflow(db, workflow)

@router.get("/workflows/{workflow_id}", response_model=WorkflowInDB)
def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    """Get a specific workflow by ID"""
    workflow = WorkflowService.get_workflow(db, workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow

@router.get("/workflows/", response_model=List[WorkflowInDB])
def get_workflows(
    skip: int = 0,
    limit: int = 100,
    campaign_id: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all workflows with optional filtering"""
    return WorkflowService.get_workflows(
        db,
        skip=skip,
        limit=limit,
        campaign_id=campaign_id,
        status=status
    )

@router.put("/workflows/{workflow_id}", response_model=WorkflowInDB)
async def update_workflow(
    workflow_id: int,
    workflow_update: WorkflowUpdate,
    db: Session = Depends(get_db)
):
    """Update a workflow"""
    workflow = await WorkflowService.update_workflow(db, workflow_id, workflow_update)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow

@router.delete("/workflows/{workflow_id}")
def delete_workflow(workflow_id: int, db: Session = Depends(get_db)):
    """Delete a workflow"""
    success = WorkflowService.delete_workflow(db, workflow_id)
    if not success:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return {"message": "Workflow deleted successfully"}

@router.post("/campaigns/", response_model=CampaignInDB)
def create_campaign(campaign: CampaignCreate, db: Session = Depends(get_db)):
    """Create a new campaign"""
    return CampaignService.create_campaign(db, campaign)

@router.get("/campaigns/{campaign_id}", response_model=CampaignInDB)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    """Get a specific campaign by ID"""
    campaign = CampaignService.get_campaign(db, campaign_id)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.get("/campaigns/", response_model=List[CampaignInDB])
def get_campaigns(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all campaigns with optional filtering"""
    return CampaignService.get_campaigns(
        db,
        skip=skip,
        limit=limit,
        status=status
    )
