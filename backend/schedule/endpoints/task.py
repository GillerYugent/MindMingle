from fastapi import APIRouter
from schedule.schema import Task,TaskCreate,TaskDelete
from uuid import UUID
router = APIRouter()

@router.get('/{shedule_id}',response_model=list[Task])
async def task_get(shedule_id:UUID)->list[Task]:
    pass

@router.get('/{task_id}',response_model=Task)
async def task_get_by_id(task_id:UUID) ->Task:
    pass

@router.post('/',response_model=Task)
async def task_create(task:TaskCreate)->Task:
    pass

@router.delete('/{task_id}',response_model=TaskDelete)
async def task_delete(task_id:UUID)->TaskDelete:
    pass