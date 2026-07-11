from fastapi import APIRouter

from app.schemas.section import SectionResponse
from app.services.section import section_service, CreateSection
from app.models.section import Section

router = APIRouter(prefix="/sections", tags=["Sections"])


@router.post("/", response_model=SectionResponse)
async def Create_Section(data: CreateSection) -> SectionResponse:
    return section_service.post(data)


@router.get("/", response_model=SectionResponse)
async def Get_Section() -> SectionResponse:
    section = Section(
        id=1,
        section_name="section A",
    )
    return SectionResponse(**section.model_dump())


@router.get("/list", response_model=list[SectionResponse])
async def Get_list() -> list[SectionResponse]:
    sections = [
        Section(
            id=1,
            section_name="section A",
        ),
        Section(
            id=1,
            section_name="section A",
        ),
    ]
    result: list[SectionResponse] = []
    for section in sections:
        validated = SectionResponse(**section.model_dump())
        result.append(validated)

    return result


@router.patch("/{id}", response_model=SectionResponse)
async def update_Section(id: int) -> SectionResponse:
    section = Section(
        id=1,
        section_name="section A",
    )
    return SectionResponse(**section.model_dump())


@router.delete("/{id}", response_model=SectionResponse)
async def delete_section(id: int) -> SectionResponse:
    sections = Section(
        id=1,
        section_name="section A",
    )
    return SectionResponse(**sections.model_dump())
