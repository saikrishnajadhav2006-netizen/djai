from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    story_input: str = Field(min_length=10, max_length=20000)
    language: str = Field(default="English", max_length=40)
    target_duration_seconds: int = Field(default=60, ge=15, le=600)


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    story_input: str
    language: str
    target_duration_seconds: int
    status: str
    created_at: datetime
