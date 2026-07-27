import uuid

from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Float,
    Text,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from .database import Base


class TranslationJob(
    Base
):

    __tablename__ = (
        "translation_jobs"
    )


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda:
            str(uuid.uuid4())
    )


    filename: Mapped[str] = mapped_column(
        String(255)
    )


    source_language: Mapped[str] = mapped_column(
        String(50),
        default="auto"
    )


    target_language: Mapped[str] = mapped_column(
        String(50),
        default="roman-hindi"
    )


    batch_size: Mapped[int] = mapped_column(
        Integer,
        default=100
    )


    total_subtitles: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    completed_subtitles: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    progress: Mapped[float] = mapped_column(
        Float,
        default=0
    )


    current_batch: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    total_batches: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="queued"
    )


    error: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
