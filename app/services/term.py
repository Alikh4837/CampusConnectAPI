from app.schemas.term import CreateTerm,TermResponse,UpdateTerm

class Term_Service:
    def __init__(self) -> None:
        pass
    def Create_Term(self,data:CreateTerm)->TermResponse:
        return TermResponse(
            id=1,
            Enrollment_Status=False
        )
    def Get_Term(self)->TermResponse:
        return TermResponse(
            id=1,
            Enrollment_Status=False
        )
    def Patch_Term(self,id:int,data:UpdateTerm)->TermResponse:
        return TermResponse(
            id=1,
            Enrollment_Status=False
        )
    def Delete_Term(self,id:int)->TermResponse:
        return TermResponse(
            id=1,
            Enrollment_Status=False
        )