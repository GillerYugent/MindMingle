#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel, EmailStr, Field
from core.schema import Default

#Классы для пользователей
class UserCreate(BaseModel):
    username: str
    first_name:str
    last_name:str
    email: EmailStr
    phone:str
    password: str
    description: str
    status: bool
    is_active:bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:int