from fastapi import APIRouter
from app.schemas.enrollment import EnrollResponse, CreateEnroll
from app.services.enrollment import enrollment_services
from app.models.enrollment import Enrollment

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("/", response_model=EnrollResponse)
async def Create_Enroll(data: CreateEnroll) -> EnrollResponse:
    return enrollment_services.post(data)


@router.get("/", response_model=EnrollResponse)
async def Get_Enroll() -> EnrollResponse:
    enrollment = Enrollment(id=1, enrol_code=1)
    return EnrollResponse(**enrollment.model_dump())


@router.get("/list", response_model=list[EnrollResponse])
async def Get_list() -> list[EnrollResponse]:
    enrollments = [
        Enrollment(id=1, enrol_code=1),
        Enrollment(id=1, enrol_code=1),
    ]
    result: list[EnrollResponse] = []
    for enrollment in enrollments:
        validated = EnrollResponse(**enrollment.model_dump())
        result.append(validated)

    return result


@router.patch("/{id}", response_model=EnrollResponse)
async def update_Enrollment(id: int) -> EnrollResponse:
    enrollment = Enrollment(id=1, enrol_code=1)
    return EnrollResponse(**enrollment.model_dump())


@router.delete("/{id}", response_model=EnrollResponse)
async def delete_Enrollment(id: int) -> EnrollResponse:
    enrollments = Enrollment(id=1, enrol_code=1)
    return EnrollResponse(**enrollments.model_dump())
