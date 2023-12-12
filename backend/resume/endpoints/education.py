#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from resume.schema import Education, EducationCreate, EducationDelete
from uuid import UUID
router = APIRouter()

@router.get("/{resume_id}", response_model=list[Education])
async def get_education(resume_id:UUID) -> list[Education]:
    pass

@router.get("/{education_id}", response_model=Education)
async def get_education_by_id(education_id: UUID) -> Education:
    pass

@router.post("/", response_model=Education)
async def create_education(education: EducationCreate) -> Education:
    pass

@router.delete("/{education_id}", response_model=EducationDelete)
async def delete_education(education_id: UUID) -> EducationDelete:
    pass