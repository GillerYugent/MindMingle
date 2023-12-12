#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel, EmailStr, Field
from core.schema import Default
from uuid import UUID
from typing import Optional
#Классы для пользователей
class UserCreate(BaseModel):
    username: str
    first_name:str
    last_name:str
    email: EmailStr
    phone: Optional[str]=None #Должно быть не обязательно
    password: str
    description: Optional[str] = None #Должно быть не обязательным
    status: bool = Field(default=-1)#0 - работник 1-стартапер (-1)-еще не определенно
    is_active:bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:UUID