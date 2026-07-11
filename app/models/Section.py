from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.term import Term
    from app.models.room import Room
    from app.models.instructor import Instructor
    from app.models.enrollment import Enrollment



class SectionBase(SQLModel):
    section_name:str

class Section(SectionBase):
    id:int=Field(primary_key=True)

    Courses:List["Course"]=Relationship(back_populates="Section")
    Terms:List["Term"]=Relationship(back_populates="Section")
    Rooms:List["Room"]=Relationship(back_populates="Section")
    Instructor:List["Instructor"]=Relationship(back_populates="Section")
    Enrollments:List["Enrollment"]=Relationship(back_populates="Section")