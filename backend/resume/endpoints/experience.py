#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from resume.schema import ExperiencCreate, Experience, ExperienceDelete

router = APIRouter()

@router.get('/{resume_id}',response_model=list[Experience])
async def experience_get(resume_id:int) -> list[Experience]:
    pass

@router.get('/{experience_id}',response_class=Experience)
async def experience_get_by_id(experience_id:int) -> Experience:
    pass

@router.post('/',response_class=Experience)
async def experience_create(experience:ExperiencCreate) -> Experience:
    pass

@router.delete('/{experience_id}',response_class=ExperienceDelete)
async def experience_delete(experience_id:int) -> ExperienceDelete:
    pass
