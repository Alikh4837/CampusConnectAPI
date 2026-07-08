from app.core.config import settings

from sqlmodel import create_engine

engine=create_engine(settings.DATABASE_URL,connect_args={"Check_same_threads":False})