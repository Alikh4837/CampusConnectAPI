from app.schemas.course import CreateCourse,CourseResponse,UpdateCourse

class Course_Service:
    def __init__(self) -> None:
        pass
    def post(self,data:CreateCourse)->CourseResponse:
        return CourseResponse(
            id=1,
            course_code=1,
            course_title="Mathematics",
            course_description="highly recommended"
        )
    def get(self)->CourseResponse:
         return CourseResponse(
            id=1,
            course_code=1,
            course_title="Mathematics",
            course_description="highly recommended"
        )
    def patch(self,id:int,data:UpdateCourse)->CourseResponse:
         return CourseResponse(
            id=1,
            course_code=1,
            course_title="Mathematics",
            course_description="highly recommended"
        )
    def delete(self,id:int)->CourseResponse:
         return CourseResponse(
            id=1,
            course_code=1,
            course_title="Mathematics",
            course_description="highly recommended"
        )