from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.department import Department
from app.models.Section import Section

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.Section import Section


class CourseBase(SQLModel):
    course_code: int = Field(index=True)
    course_title: str
    course_description: Optional[str]


class Course(CourseBase):
    id: int = Field(primary_key=True)

    departments:List["Department"]=Relationship(back_populates="Instructor")
    sections:List["Section"]=Relationship(back_populates="Instructor")
