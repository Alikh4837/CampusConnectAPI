from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.enrollment import Enrollment

if TYPE_CHECKING:
    from app.models.enrollment import Enrollment

class StudentBase(SQLModel):
    name: str
    dob:str
    gender:str
    phone: int = Field(index=True)
    email: str
    Address: str
    password:str
    emergency_contact:Optional[int]


class Student(StudentBase):
    id: int = Field(primary_key=True)

    enrollments:List["Enrollment"]=Relationship(back_populates="Student")