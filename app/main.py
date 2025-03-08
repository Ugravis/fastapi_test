from fastapi import FastAPI
from .api.api_v1.api import api_router
from .db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI test",
    description="Test/template API made by FastAPI",
    version="0.0.1"
)

app.include_router(api_router, prefix="/v1")

@app.get('/')
async def root():
    return { "message": "Hello world from FastAPI" }