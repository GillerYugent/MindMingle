from fastapi import APIRouter
from startups.schema import StartUp
router = APIRouter()

@router.get('/',response_model=StartUp)
async def router_get() ->list[StartUp]:
    pass