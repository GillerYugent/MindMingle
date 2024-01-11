#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from resume.schema import ExperiencCreate, Experience, ExperienceDelete
from uuid import UUID
router = APIRouter()

@router.get('/{resume_id}/experience',response_model=list[Experience])
async def experience_get(resume_id:UUID) -> list[Experience]:
    pass

@router.get('/experience/{experience_id}',response_model=Experience)
async def experience_get_by_id(experience_id:UUID) -> Experience:
    pass

@router.post('/experience/',response_model=Experience)
async def experience_create(experience:ExperiencCreate) -> Experience:
    pass

@router.delete('/experience/{experience_id}',response_model=ExperienceDelete)
async def experience_delete(experience_id:UUID) -> ExperienceDelete:
   pass
