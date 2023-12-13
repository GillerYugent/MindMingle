#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from resume.schema import Skill, SkillCreate, SkillDelete
from uuid import UUID
router = APIRouter()

@router.get('/{resume_id}',response_model=list[Skill])
async def skill_get(resume_id:UUID) -> list[Skill]:
    pass

@router.get('/{skill_id}',response_model=Skill)
async def skill_get_by_id(skill_id:UUID) -> Skill:
    pass

@router.post('/',response_model=Skill)
async def skill_create(skill:SkillCreate) -> Skill:
    pass

@router.delete('/{skill_id}',response_model=SkillDelete)
async def skill_delete(skill_id:UUID) -> SkillDelete:
    pass