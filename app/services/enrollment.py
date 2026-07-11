from app.schemas.enrollment import CreateEnroll,EnrollResponse,UpdateEnroll

class Enrollment_Services:
    def __init__(self) -> None:
        pass
    def post(self,data:CreateEnroll)->EnrollResponse:
        return EnrollResponse(
            id=1,
            enrol_code=1
        )
    def get(self)->EnrollResponse:
        return EnrollResponse(
            id=1,
            enrol_code=1
        )
    def patch(self,id:int,data:UpdateEnroll)->EnrollResponse:
        return EnrollResponse(
            id=1,
            enrol_code=1
        )
    def delete(self,id:int)->EnrollResponse:
        return EnrollResponse(
            id=1,
            enrol_code=1
        )
    
enrollment_services=Enrollment_Services()