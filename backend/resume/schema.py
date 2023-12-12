#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       
from uuid import UUID
from pydantic import BaseModel
from core.schema import Default
from typing import Optional, List
class ResumeCreate(BaseModel):
    user_id:UUID
    #Доработать схему, так как мне сейчас лень
    

class Resume(ResumeCreate,Default):
    id:UUID

class ResumeDelete(BaseModel):
    id:UUID

#Класс для опыта
class ExperiencCreate(BaseModel):
    resume_id:UUID
    role:str
    company:str
    description: Optional[str] = None

class Experience(ExperiencCreate, Default):
    pass

class ExperienceDelete(BaseModel):
    id:UUID

#Класс для образования
class EducationCreate(BaseModel):
    name:str
    resume_id:UUID
    years: int
    direction: str
    #Сделать всё остальное, что нужно дя описания универа
    description: Optional[str] = None
    is_end:bool

class Education(EducationCreate, Default):
    pass

class EducationDelete(BaseModel):
    id:UUID

#Класс для навыков
class SkillCreate(BaseModel):
    resume_id:UUID
    name: str

class Skill(SkillCreate, Default):
    pass

class SkillDelete(BaseModel):
    id:UUID