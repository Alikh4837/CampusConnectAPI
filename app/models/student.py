from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.enrollment import Enrollment

class StudentBase(SQLModel):
    name: str
    dob:str
    gender:str
    phone: str = Field(index=True)
    email: str
    address: str
    password:str
    emergency_contact:Optional[str]


class Student(StudentBase,table=True):
    id: int = Field(primary_key=True)

    enrollments:List["Enrollment"]=Relationship(back_populates="student")