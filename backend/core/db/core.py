from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,Integer,String, DateTime
import uuid
import datetime

class Default(DeclarativeBase):
    id:Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    created_at: Column(DateTime,default=datetime.datetime.utcnow)
    update_at: Column(DateTime,default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)