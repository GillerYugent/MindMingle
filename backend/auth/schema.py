#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from core.schema import Default

#Класс для опыта
class ExperiencCreate(BaseModel):
    user_id:int
    role:str
    company:str
    description: Optional[str] = None

class Experience(ExperiencCreate, Default):
    pass

class ExperienceDelete(BaseModel):
    id:int

#Класс для образования
class EducationCreate(BaseModel):
    name:str
    user_id:int
    #Сделать лет образования, название направления и всё остальное, что нужно дя описания универа
    description: Optional[str] = None
    id_end:bool

class Education(EducationCreate, Default):
    pass

class EducationDelete(BaseModel):
    id:int

#Класс для навыков
class SkillCreate(BaseModel):
    user_id:int
    name: str
    level: str
    description: Optional[str] = None

class Skill(SkillCreate, Default):
    pass

class SkillDelete(BaseModel):
    id:int

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
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:int