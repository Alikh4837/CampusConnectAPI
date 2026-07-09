from app.models.course import CourseBase
from typing import Optional

class CreateCourse(CourseBase):
    pass

class UpdateCourse(CourseBase):
    course_code:Optional[int]=None
    course_title:Optional[str]=None
    course_description:Optional[str]=None

class CourseResponse(CourseBase):
    id:int