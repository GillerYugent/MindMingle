#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel
from core.schema import Default
from typing import List, Optional

class StartUp_Create(BaseModel):
    title:str
    description: str | None = None
    owner_id:int
    is_premium:bool
    stack: List[str]
    logo: bytes
    language:str
    photo_list: Optional[List[bytes]] = None

class StartUp(StartUp_Create,Default):
    status:bool
    memberlist: Optional[List[int]] = None #id разработчиков, участвующих в стартапе

class StartUp_Delete(BaseModel):
    id:int