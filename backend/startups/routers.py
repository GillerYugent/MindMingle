from fastapi import APIRouter
from startups.endpoints.startups import router as startup_routers
router = APIRouter()

router.include_router(startup_routers,prefix="/startups")