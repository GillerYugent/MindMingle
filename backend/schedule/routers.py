


from fastapi import APIRouter
from schedule.endpoints.schedule import router as schedule_router
from schedule.endpoints.task import router as task_router

router = APIRouter()

router.include_router(schedule_router)
router.include_router(task_router,prefix="/task")