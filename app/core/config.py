from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./campus_connect.db"
    APP_NAME: str = "University course registration and resource management API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True  

    SECRET_KEY:str="im_duh_secret_key"
    ALGORITHM:str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int=10

settings = Settings()
