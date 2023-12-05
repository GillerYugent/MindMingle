from pydantic import BaseModel, EmailStr
from typing import List, Optional
from backend.core.schema import Default

class UserCreate(BaseModel):
    username: str
    first_name:str
    last_name:str
    email: EmailStr
    phone:str
    password: str
    discription: str
    status: bool
    skills = Optional[List[str]] = None
    expereince = Optional[list[str]] = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class User(UserCreate,Default):
    pass

class UserDelete(BaseModel):
    id:int
