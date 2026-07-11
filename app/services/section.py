from app.schemas.section import CreateSection,SectionResponse,UpdateSection

class Section_Service:
    def __init__(self) -> None:
        pass
    def post(self,data:CreateSection)->SectionResponse:
        return SectionResponse(
            id=1,
            section_name="Sec A"
        )
    def get(self)->SectionResponse:
        return SectionResponse(
            id=1,
            section_name="Sec A"
        )
    def patch(self,id:int,data:UpdateSection)->SectionResponse:
        return SectionResponse(
            id=1,
            section_name="Sec A"
        )
    def delete(self,id:int)->SectionResponse:
        return SectionResponse(
            id=1,
            section_name="Sec A"
        )
    
section_service=Section_Service()