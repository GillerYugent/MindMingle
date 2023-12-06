#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#       

from fastapi import APIRouter
from auth.endpoints.auth import router as auth_router
from auth.endpoints.education import router as education_router
from auth.endpoints.experience import router as experience_router
from auth.endpoints.skills import router as skills_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(skills_router)
router.include_router(education_router)
router.include_router(experience_router)