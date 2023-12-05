from fastapi import APIRouter
from startups.routers import router as startup_router
from auth.routers import router as user_router

router = APIRouter()

router.include_router(startup_router,prefix='/startup',tags=["Startup routers"])
router.include_router(user_router, prefix="/users", tags=["User routers"])
