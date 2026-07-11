from fastapi import APIRouter

router=APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)

@router.post("/",response_model=)