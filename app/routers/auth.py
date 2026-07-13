from fastapi import APIRouter, HTTPException
from app.schemas.auth import Token, LoginRequest
from app.services.auth import authservice

router = APIRouter(prefix="/Auth", tags=["Auth"])


@router.post("/login/student", response_model=Token)
def login_student(data: LoginRequest) -> Token:
    try:
        token = authservice.login_student(data.email, data.password)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return Token(access_token=token)


@router.post("/login/instructor", response_model=Token)
def login_instructor(data: LoginRequest) -> Token:
    try:
        token = authservice.login_instructor(data.email, data.password)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return Token(access_token=token)
