from pydantic import BaseModel, EmailStr
from typing import List, Optional
from backend.core.schema import Default

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
    skills = Optional[List[Skills]] = None
    experience = Optional[list[Experience]] = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:int

