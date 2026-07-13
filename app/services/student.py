from app.schemas.student import StudentResponse, CreateStudent,UpdateStudent
from app.models.student import Student
from app.core.security import hash_password


class StudentService:
    def __init__(self) -> None:
        pass

    def get(self,data:StudentResponse)->StudentResponse:
        return StudentResponse(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",
        )

    def create(self, data: CreateStudent) -> StudentResponse:
        return StudentResponse(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",
        )

    def update(self,data:UpdateStudent)->StudentResponse:
        return StudentResponse(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",)

    def delete(self,data:StudentResponse)->StudentResponse:
        return StudentResponse(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password="123",
            emergency_contact="123",
        )
    def get_by_email(self,email:str)->Student|None:
        mock_student = Student(
            id=1,
            name="john",
            dob="29june2005",
            gender="Male",
            phone="20912",
            email="alikh4837@gmail.com",
            address="Johar town",
            password=hash_password("123"),  
            emergency_contact="123",
        )
        if email == mock_student.email:
            return mock_student
        return None


student_service = StudentService()
