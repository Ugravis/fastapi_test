from fastapi import FastAPI
from .routers import users
from .db.database import engine, Base
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI test")

app.include_router(users.router)

@app.get('/')
async def root():
    return { "message": "Helléào world from FastAPI" }