


from fastapi import APIRouter
from schedule.endpoints.schedule import router as schedule_router

router = APIRouter()

router.include_router(schedule_router)