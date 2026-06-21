from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SelfDev API",
    version="1.0.0"
)

app.include_router(router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)