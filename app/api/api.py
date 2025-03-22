from fastapi import APIRouter

from .endpoints import alcoholism


router = APIRouter()

router.include_router(alcoholism.router, prefix="/alcoholism")
