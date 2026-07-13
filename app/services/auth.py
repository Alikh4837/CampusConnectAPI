from app.services.student import student_service
from app.services.instructor import instructor_service
from app.core.security import verify_password, create_access_token


class Auth_Service:
    def __init__(self) -> None:
        pass

    def login_student(self, email: str, password: str) -> str:
        student = student_service.get_by_email(email)
        if not student or not verify_password(password, student.password):
            raise ValueError("Invalid Credentials")
        return create_access_token(subject=str(student.id), role="student")

    def login_instructor(self, email: str, password: str) -> str:
        instructor = instructor_service.get_by_email(email)
        if not instructor or not verify_password(password, instructor.password):
            raise ValueError("Invalid credentials")
        return create_access_token(subject=str(instructor.id), role="instructor")


authservice = Auth_Service()
