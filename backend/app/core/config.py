from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DJ AI"
    app_env: str = "development"
    database_url: str = "sqlite:///./dj_ai.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
