from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from core.schema import Default
import typing
#Класс для опыта
class Experience(BaseModel):
    role:str
    company:str
    description: Optional[str] = None

#Класс для навыков
class Skills(BaseModel):
    name: str
    level: str
    description: Optional[str] = None

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
    skills: Union[typing.List[Skills], None] = None
    experience: Union[typing.List[Experience], None] = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:int

