
from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "CyberSage AI is an AI-powered Cyber Threat Intelligence "
        "analysis platform using fine-tuned Small Language Models, "
        "MCP integrations, and Retrieval-Augmented Generation."
    ),
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to CyberSage AI",
        "status": "running",
        "docs": "/docs",
    }
