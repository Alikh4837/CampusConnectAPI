from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./campus_connect.db"
    APP_NAME: str = "University course registration and resource management API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True  


settings = Settings()
