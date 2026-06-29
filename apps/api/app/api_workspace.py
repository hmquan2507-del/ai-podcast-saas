from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repository_workspace import WorkspaceRepository
from app.schemas_workspace import WorkspaceCreate, WorkspaceRead


router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.post("", response_model=WorkspaceRead)
async def create_workspace(payload: WorkspaceCreate, db: AsyncSession = Depends(get_db)):
    repo = WorkspaceRepository(db)
    existing = await repo.get_by_slug(payload.slug)
    if existing:
        raise HTTPException(status_code=409, detail="Workspace slug already exists")
    return await repo.create(payload)


@router.get("", response_model=list[WorkspaceRead])
async def list_workspaces(db: AsyncSession = Depends(get_db)):
    repo = WorkspaceRepository(db)
    return await repo.list()
