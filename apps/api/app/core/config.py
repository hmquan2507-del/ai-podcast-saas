from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/ai_podcast_saas"
    api_title: str = "AI Talking Video Platform API"

    class Config:
        env_file = ".env"


settings = Settings()
