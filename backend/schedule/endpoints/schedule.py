from fastapi import APIRouter
from schedule.schema import Schedule,Schedule_Create,Schedule_Delete
from uuid import UUID
router = APIRouter()

@router.get('/',response_model=list[Schedule])
async def schedule_get() -> list[Schedule]:
    pass

@router.get('/{schedule_id}',response_model=Schedule)
async def schedule_get_by_id(schedule_id:UUID) -> Schedule:
    pass

@router.post('/',response_model=Schedule)
async def schedule_create(schedule:Schedule_Create) -> Schedule:
    pass

@router.delete('/',response_model=Schedule_Delete)
async def schedule_delete(schedule_id:UUID) -> Schedule_Delete:
    pass