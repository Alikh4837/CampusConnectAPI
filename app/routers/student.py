from fastapi import APIRouter, Depends
from app.schemas.student import StudentResponse, CreateStudent
from app.models.student import Student
from app.services.student import student_service

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentResponse)
def create_student(data: CreateStudent) -> StudentResponse:
    return student_service.create(data)


@router.get("/", response_model=StudentResponse)
def get_student() -> StudentResponse:
    student = Student(  
        id=1,
        name="john",
        dob="29june2005",
        gender="Male",
        phone="20912",
        email="alikh4837@gmail.com",
        address="Johar town",
        password="123",
        emergency_contact="123",
    )

    return StudentResponse(**student.model_dump())


@router.get("/list", response_model=list[StudentResponse])
async def list_students() -> list[StudentResponse]:
    students = [
        Student(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",
        ),
        Student(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",
        ),
    ]

    results: list[StudentResponse] = []
    for student in students:
        validated = StudentResponse(**student.model_dump())
        results.append(validated)

    return results


@router.patch("/", response_model=StudentResponse)
async def update_student() -> StudentResponse:
    student = Student(
        id=1,
        name="john",
        dob="29june2005",
        gender="Male",
        phone="20912",
        email="alikh4837@gmail.com",
        address="Johar town",
        password="123",
        emergency_contact="123",
    )

    return StudentResponse(**student.model_dump())


@router.delete("/{id}", response_model=StudentResponse)
async def delete_student(id: int) -> StudentResponse:
    student = Student(
        id=1,
        name="john",
        dob="29june2005",
        gender="Male",
        phone="20912",
        email="alikh4837@gmail.com",
        address="Johar town",
        password="123",
        emergency_contact="123",
    )

    return StudentResponse(**student.model_dump())
