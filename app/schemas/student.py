from app.models.student import StudentBase
from typing import Optional


class CreateStudent(StudentBase):
    password:str


class UpdateStudent(StudentBase):
    name: Optional[str] = None
    dob:Optional[str]=None
    gender:Optional[str]=None
    phone: Optional[int] = None
    email: Optional[str] = None
    Address: Optional[str] = None
    emergency_contact:Optional[int]=None

class StudentResponse(StudentBase):
    id: int
