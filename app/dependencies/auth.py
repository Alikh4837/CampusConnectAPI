from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.schemas.auth import TokenData
from jose import jwt, JWTError
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_token_data(token: str = Depends(oauth2_scheme)) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        subject: str | None = payload.get("sub")
        role: str | None = payload.get("role")
        if subject is None or role is None:
            raise credentials_exception
        return TokenData(subject=subject, role=role)
    except JWTError:
        raise credentials_exception


def require_role(require_role: str):
    def checker(token_data: TokenData = Depends(get_current_token_data)) -> TokenData:
        if token_data.role != require_role:
            raise HTTPException(
                status_code=403, detail="Not authorised for this action"
            )
        return token_data

    return checker
