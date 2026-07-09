from app.models.student import StudentBase
from typing import Optional


class CreateStudent(StudentBase):
    pass


class UpdateStudent(StudentBase):
    name: Optional[str] = None
    phone: Optional[int] = None
    email: Optional[str] = None
    Address: Optional[str] = None


class StudentResponse(StudentBase):
    id: int
