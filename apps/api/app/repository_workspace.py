from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.workspace import Workspace
from app.schemas_workspace import WorkspaceCreate


class WorkspaceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: WorkspaceCreate) -> Workspace:
        workspace = Workspace(
            name=data.name,
            slug=data.slug,
            description=data.description,
        )
        self.db.add(workspace)
        await self.db.commit()
        await self.db.refresh(workspace)
        return workspace

    async def get_by_slug(self, slug: str) -> Workspace | None:
        result = await self.db.execute(
            select(Workspace).where(Workspace.slug == slug)
        )
        return result.scalar_one_or_none()

    async def list(self) -> list[Workspace]:
        result = await self.db.execute(select(Workspace).order_by(Workspace.created_at.desc()))
        return list(result.scalars().all())
