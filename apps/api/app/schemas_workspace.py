from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class WorkspaceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    slug: str = Field(min_length=1, max_length=160)
    description: str | None = None


class WorkspaceRead(BaseModel):
    id: UUID
    name: str
    slug: str
    status: str
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
