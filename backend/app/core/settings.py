from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    PROJECT_NAME: str = "Ultimate AI Subtitle Translator"

    VERSION: str = "1.0.0"

    API_PREFIX: str = "/api/v1"

    OPENAI_API_KEY: str = Field(
        default=""
    )

    OPENAI_MODEL: str = Field(
        default="gpt-5"
    )

    DATABASE_URL: str = Field(
        default=""
    )

    REDIS_URL: str = Field(
        default=""
    )

    DEFAULT_BATCH_SIZE: int = 100

    MAX_BATCH_SIZE: int = 500

    MAX_FILE_SIZE_MB: int = 100

    LOG_LEVEL: str = "INFO"

    MAX_CONCURRENT_BATCHES: int = 3

    TRANSLATION_TIMEOUT: int = 300

    RETRY_COUNT: int = 3

    REVIEW_ENABLED: bool = True

    AUTO_LANGUAGE_DETECTION: bool = True

    ROMAN_HINDI_MODE: bool = True


@lru_cache
def get_settings():

    return Settings()
