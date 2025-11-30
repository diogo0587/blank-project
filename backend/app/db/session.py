from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()

# Garantir que o DSN seja sempre string para o SQLAlchemy,
# mesmo que algum tipo de URL seja injetado via BaseSettings.
engine = create_engine(str(settings.POSTGRES_DSN), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()