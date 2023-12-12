from fastapi import FastAPI, status
from src.app.views import router as main_router
from src.config.settings import APP_TITLE, APP_API_PREFIX

app = FastAPI(title=APP_TITLE, docs_url="/docs", redoc_url=None)
app.include_router(router=main_router, prefix=APP_API_PREFIX)


@app.get("/")
def root_handler():
    return status.HTTP_418_IM_A_TEAPOT
