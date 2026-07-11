from app.core.config import settings

from sqlmodel import create_engine

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
