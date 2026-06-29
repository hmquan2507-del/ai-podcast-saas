from fastapi import FastAPI

from app.api_workspace import router as workspace_router
from app.core.config import settings


app = FastAPI(
    title=settings.api_title,
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "ai-talking-video-platform-api",
        "version": "0.1.0",
    }


app.include_router(workspace_router)
