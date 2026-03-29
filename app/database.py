from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "sqlite:///./launch_pad.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


class Base(DeclarativeBase):
    pass


def get_db() -> Session:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    from app import models  # noqa: F401 — ensure models are registered

    Base.metadata.create_all(bind=engine)
