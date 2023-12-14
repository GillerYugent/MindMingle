

from pydantic import BaseModel
from core.schema import Default
from typing import Optional
from uuid import UUID


class Schedule_Create(BaseModel):
    title:str
    startup_id: UUID
    user_id: Optional[UUID] = None

class Schedule(Schedule_Create,Default):
    pass

class Schedule_Delete(BaseModel):
    id:UUID