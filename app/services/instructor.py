from app.schemas.instructor import CreateInstructor,InstructorResponse,UpdateInstructor

class InstructorService:
    def __init__(self) -> None:
        pass

    def Get_Instructor(self,data:InstructorResponse)->InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def Post_Instructor(self,data:CreateInstructor)->InstructorResponse:
        return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def patch_Instructor(self,data:UpdateInstructor)->InstructorResponse:
         return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

    def delete_Instructor(self,data:InstructorResponse)->InstructorResponse:
         return InstructorResponse(
            id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )

instructor_service=InstructorService()