from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.projects import router as projects_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models.project import Project  # noqa: F401 - registers model metadata


@asynccontextmanager
async def lifespan(_: FastAPI):
    # MVP convenience for local development. Use Alembic migrations before production.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="Free-first, provider-independent AI documentary orchestration studio.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(projects_router)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.app_env,
    }


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    return {
        "message": "DJ AI API is running",
        "docs": "/docs",
        "health": "/health",
        "projects": "/api/projects",
    }
