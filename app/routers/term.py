from fastapi import APIRouter
from app.schemas.term import TermResponse, CreateTerm
from app.services.term import term_service
from app.models.term import Term

router = APIRouter(prefix="/terms", tags=["Terms"])


@router.post("/", response_model=TermResponse)
async def Create_Term(data: CreateTerm) -> TermResponse:
    return term_service.Create_Term(data)


@router.get("/", response_model=TermResponse)
async def Get_Term() -> TermResponse:
    term = Term(
        id=1,
        Enrollment_Status=False,
    )
    return TermResponse(**term.model_dump())


@router.get("/list", response_model=list[TermResponse])
async def Get_list() -> list[TermResponse]:
    terms = [
        Term(
            id=1,
            Enrollment_Status=False,
        ),
        Term(
            id=2,
            Enrollment_Status=True,
        ),
    ]
    result: list[TermResponse] = []
    for term in terms:
        validated = TermResponse(**term.model_dump())
        result.append(validated)

    return result


@router.patch("/{id}", response_model=TermResponse)
async def update_term(id: int) -> TermResponse:
    term = Term(
        id=1,
        Enrollment_Status=False,
    )
    return TermResponse(**term.model_dump())


@router.delete("/{id}", response_model=TermResponse)
async def delete_term(id: int) -> TermResponse:
    term = Term(
        id=1,
        Enrollment_Status=False,
    )
    return TermResponse(**term.model_dump())
