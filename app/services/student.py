from app.schemas.student import StudentResponse, CreateStudent
from app.models.student import Student


class StudentService:
    def __init__(self) -> None:
        pass

    def get(self):
        pass

    def create(self, data: CreateStudent) -> StudentResponse:
        return StudentResponse(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone=20912,
            email="alikh4837@gmail.com",
            Address="Johar town",
            password="123",
            emergency_contact=123,
        )

    def update(self):
        pass

    def delete(self):
        pass


student_service = StudentService()
