#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       


from fastapi import APIRouter
from startups.schema import StartUp, StartUp_Delete, StartUp_Create
from uuid import UUID
router = APIRouter()

@router.get('/',response_model=list[StartUp])
async def startup_get() ->list[StartUp]:
    pass

@router.get('/{startup_id}',response_model=StartUp)
async def startup_get_by_id(startup_id:UUID) -> StartUp:
    pass

@router.post('/',response_model=StartUp)
async def startup_create(startup:StartUp_Create) -> StartUp:
    pass

@router.delete('/{startup_id}',response_model=StartUp_Delete)
async def startup_delete(startup_id:UUID) -> StartUp_Delete:
    pass

