

from pydantic import BaseModel, Field
from core.schema import Default
from typing import Optional
from uuid import UUID
from datetime import datetime

class Schedule_Create(BaseModel):
    title:str
    startup_id: UUID
    user_id: Optional[UUID] = None

class Schedule(Schedule_Create,Default):
    pass

class Schedule_Delete(BaseModel):
    id:UUID

class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    schedule_id:UUID
    task_creater = UUID
    deadline:Optional[datetime] = None
    status:int = Field(default=0)
    worker: Optional[UUID]=None

class Task(TaskCreate, Default):
    pass

class TaskDelete(BaseModel):
    id:UUID


