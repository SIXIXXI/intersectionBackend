from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

from app.api.api import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    swagger_ui_parameters={"persistAuthorization": True},
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    # currently allow all origins, can set up settings.BACKEND_CORS_ORIGINS
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
