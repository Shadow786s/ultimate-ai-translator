from typing import List, Optional

from pydantic import BaseModel


class SubtitleEntry(BaseModel):

    index: int

    start: str

    end: str

    text: str


class TranslationEntry(BaseModel):

    index: int

    start: str

    end: str

    original: str

    translation: str


class TranslationJob(BaseModel):

    job_id: str

    status: str

    progress: float

    completed: int

    total: int

    current_batch: int

    total_batches: int

    entries: List[TranslationEntry] = []

    error: Optional[str] = None
