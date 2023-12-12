import uvicorn

from src.config import settings

uvicorn.run(
    "main:app",
    host=settings.APP_HOST,
    port=settings.APP_PORT,
    reload=settings.DEVELOPMENT,
)
