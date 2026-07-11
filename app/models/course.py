from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.section import Section


class CourseBase(SQLModel):
    course_code: int = Field(index=True)
    course_title: str
    course_description: Optional[str]=None


class Course(CourseBase,table=True):
    id: int = Field(primary_key=True)

    department_id:Optional[int]=Field(default=None,foreign_key="department.id")

    department: Optional["Department"] = Relationship(back_populates="courses")
    sections:List["Section"]=Relationship(back_populates="courses")
