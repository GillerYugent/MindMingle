#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel
from core.schema import Default
from typing import Optional, List
class ResumeCreate(BaseModel):
    user_id:int
    #Доработать схему, так как мне сейчас лень

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
    years: int
    direction: str
    #Сделать всё остальное, что нужно дя описания универа
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