from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.section import Section
    from app.models.student import Student


class EnrollmentBase(SQLModel):
    enrol_code: int


class Enrollment(EnrollmentBase, table=True):
    id: int = Field(primary_key=True)

    student_id: Optional[int] = Field(default=None, foreign_key="student.id")
    section_id: Optional[int] = Field(default=None, foreign_key="section.id")

    section: Optional["Section"] = Relationship(back_populates="enrollments")
    student: Optional["Student"] = Relationship(back_populates="enrollments")
