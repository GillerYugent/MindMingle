#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
class Default(BaseModel):
    id:UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None