from app.models.instructor import InstructorBase
from typing import Optional


class CreateInstructor(InstructorBase):
    password:str


class UpdateInstructor(InstructorBase):
    name: Optional[str] = None
    phone: Optional[int] = None
    email:Optional[str]=None
    address: Optional[str] = None
    emergency_contact: Optional[int] = None


class InstructorResponse(InstructorBase):
    id: int
