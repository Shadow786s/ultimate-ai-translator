import os


class Settings:

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )


    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5-mini"
    )


    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite+aiosqlite:///./translator.db"
    )


    MAX_BATCH_SIZE = int(
        os.getenv(
            "MAX_BATCH_SIZE",
            "200"
        )
    )


    DEFAULT_BATCH_SIZE = int(
        os.getenv(
            "DEFAULT_BATCH_SIZE",
            "100"
        )
    )


    MAX_FILE_SIZE_MB = int(
        os.getenv(
            "MAX_FILE_SIZE_MB",
            "50"
        )
    )


settings = Settings()
