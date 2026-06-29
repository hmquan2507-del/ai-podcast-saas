from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.api_title,
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai-talking-video-platform-api",
        "version": "0.1.0",
    }
