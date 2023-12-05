from fastapi import APIRouter
from startups.routers import router as startup_router

router = APIRouter()

router.include_router(startup_router,prefix='/startup',tags=["Startup routers"])