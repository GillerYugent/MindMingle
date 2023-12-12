#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
# 

from fastapi import APIRouter
from resume.endpoints.resume import router as resume_router
from resume.endpoints.education import router as education_router
from resume.endpoints.experience import router as experience_router
from resume.endpoints.skills import router as skills_router

router = APIRouter()


#router.include_router(skills_router)
router.include_router(education_router, prefix="/education")
router.include_router(experience_router,prefix="/experience")
router.include_router(resume_router)