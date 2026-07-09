from app.schemas.student import CreateStudent,StudentResponse
from app.models.student import Student

def Create_Student_Service(db,data:CreateStudent)->Student:
    new_student=Student(**data.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh()
    return new_student

def Get_Student_Service(db,data:StudentResponse)->Student:
    