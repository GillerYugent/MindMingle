#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from auth.schema import User, UserCreate, UserDelete
from uuid import UUID
router = APIRouter()

@router.get('/', response_model=list[User])
async def user_get() -> list[User]:
    pass

@router.get('/{user_id}',response_model=User)
async def get_user_by_id(user_id:UUID) -> User:
    pass

@router.post('/',response_model=User)
async def user_create(user:UserCreate) -> User:
    pass

@router.delete('/{user_id}',response_model=UserDelete)
async def user_delete(user_id:UUID) -> UserDelete:
    pass

