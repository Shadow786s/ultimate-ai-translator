from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(

    title="Ultimate AI Subtitle Translator",

    version="1.0.0",

    lifespan=lifespan

)

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

app.include_router(upload_router)


@app.get("/")
async def root():

    return {

        "name": "Ultimate AI Subtitle Translator",

        "status": "online"

    }


@app.get("/health")
async def health():

    return {

        "status": "healthy"

    }
