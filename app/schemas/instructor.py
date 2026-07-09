from app.models.instructor import InstructorBase
from typing import Optional


class CreateInstructor(InstructorBase):
    pass


class UpdateInstructor(InstructorBase):
    name: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    emergency_contact: Optional[int] = None


class InstructorResponse(InstructorBase):
    id: int
