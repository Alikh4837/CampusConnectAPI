from app.schemas.instructor import (
    CreateInstructor,
    InstructorResponse,
    UpdateInstructor,
)
from app.models.instructor import Instructor
from app.core.security import hash_password


class InstructorService:
    def __init__(self) -> None:
        pass

    def Get_Instructor(self, data: InstructorResponse) -> InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def Post_Instructor(self, data: CreateInstructor) -> InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def patch_Instructor(self, data: UpdateInstructor) -> InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def delete_Instructor(self, data: InstructorResponse) -> InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def get_by_email(self, email: str) -> Instructor | None:
        mock_instructor = Instructor(
            id=1,
            name="john",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password=hash_password("123"),
            emergency_contact="123",
        )
        if email == mock_instructor.email:
            return mock_instructor
        return None


instructor_service = InstructorService()
