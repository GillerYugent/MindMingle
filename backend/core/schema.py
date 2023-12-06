#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from pydantic import BaseModel
from datetime import datetime
class Default(BaseModel):
    id:int
    created_at: datetime | None = None
    updated_at: datetime | None = None