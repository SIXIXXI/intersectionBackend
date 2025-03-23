from fastapi import APIRouter

from .endpoints import func


router = APIRouter()

router.include_router(func.router, prefix="/func")
