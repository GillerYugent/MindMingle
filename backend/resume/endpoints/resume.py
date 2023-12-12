#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
# 
from fastapi import APIRouter
from resume.schema import ResumeCreate, Resume, ResumeDelete
from uuid import UUID
router = APIRouter()


@router.get('/',response_model=list[Resume])
async def resume_get() -> list[Resume]:
    pass

@router.get('/{resume_id}',response_model=Resume)
async def resume_get_by_id(resume_id:UUID) -> Resume:
    pass

@router.post('/',response_model=Resume)
async def resume_create(resume:ResumeCreate) -> Resume:
    pass

@router.delete('/{resume_id}',response_model=ResumeDelete)
async def resume_delete(resume_id:UUID) -> ResumeDelete:
    pass
