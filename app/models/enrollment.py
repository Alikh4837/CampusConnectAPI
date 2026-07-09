from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.Section import Section
from app.models.student import Student

if TYPE_CHECKING:
    from app.models.Section import Section
    from app.models.student import Student

class EnrollmentBase(SQLModel):
    enrol_code:int

class Enrollment(EnrollmentBase):
    id:int=Field(primary_key=True)

    sections:List["Section"]=Relationship(back_populates="Instructor")
    students:List["Student"]=Relationship(back_populates="Instructor")
