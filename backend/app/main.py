from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from .database import (
    init_db
)


@asynccontextmanager
async def lifespan(
    app: FastAPI
):

    await init_db()

    yield


app = FastAPI(

    title=
    "Ultimate AI Translator API",

    version=
    "1.0.0",

    lifespan=
    lifespan
)


app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "*"
    ],

    allow_credentials=
    True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]
)


@app.get("/")
async def root():

    return {

        "name":
        "Ultimate AI Translator",

        "status":
        "online"

    }


@app.get("/health")
async def health():

    return {

        "status":
        "healthy"

    }


@app.get("/database-status")
async def database_status():

    return {

        "database":
        "initialized",

        "status":
        "ready"

    }
