from fastapi import APIRouter
from app.schemas.course import CourseResponse
from app.services.course import course_service,CreateCourse
from app.models.course import Course

router=APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.post("/",response_model=CourseResponse)
async def Create_Course(data:CreateCourse)->CourseResponse:
    return course_service.post(data)

@router.get("/",response_model=CourseResponse)
async def Get_Course()->CourseResponse:
    course=Course(
        id=1,
        course_code=1,
        course_title="the pacifier",
        course_description="helper"
    )
    return CourseResponse(**course.model_dump())

@router.get("/list", response_model=list[CourseResponse])
async def Get_list() -> list[CourseResponse]:
    courses = [
        Course(
            id=1,
        course_code=1,
        course_title="the pacifier",
        course_description="helper"
        ),
        Course(
            id=1,
        course_code=1,
        course_title="the pacifier",
        course_description="helper"
        ),
    ]
    result: list[CourseResponse] = []
    for course in courses:
        validated = CourseResponse(**course.model_dump())
        result.append(validated)

    return result


@router.patch("/{id}", response_model=CourseResponse)
async def update_Course(id: int) -> CourseResponse:
    course = Course(
        id=1,
        course_code=1,
        course_title="the pacifier",
        course_description="helper"
    )
    return CourseResponse(**course.model_dump())


@router.delete("/{id}", response_model=CourseResponse)
async def delete_Course(id: int) -> CourseResponse:
    courses = Course(
        id=1,
        course_code=1,
        course_title="the pacifier",
        course_description="helper"
    )
    return CourseResponse(**courses.model_dump())
