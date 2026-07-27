import uuid

from sqlalchemy import (
    String,
    Integer,
    DateTime,
    Float,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime

from app.database.session import Base


class TranslationJob(Base):

    __tablename__ = "translation_jobs"


    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    filename: Mapped[str] = mapped_column(
        String(300)
    )


    status: Mapped[str] = mapped_column(
        String(30),
        default="queued"
    )


    source_language: Mapped[str] = mapped_column(
        String(50),
        default="auto"
    )


    target_language: Mapped[str] = mapped_column(
        String(50),
        default="roman-hindi"
    )


    total_subtitles: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    translated_subtitles: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    progress: Mapped[float] = mapped_column(
        Float,
        default=0
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
