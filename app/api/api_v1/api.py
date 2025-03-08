from fastapi import APIRouter
from .routes import users

api_router = APIRouter()

api_router.include_router(users.router)

@api_router.get("/")
async def root():
    return { "message": "Bienvenue sur la v1 de l'api" }