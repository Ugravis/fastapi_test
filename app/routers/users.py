from fastapi import APIRouter, HTTPException

test_users  = [
    { "name": "Jean", "age": 25 },
    { "name": "Clovis", "age": 27 },
    { "name": "Louis", "age": 14 }
]

router = APIRouter(
    prefix="/users",
    tags=["users"], # Indique la catégorie du router, uniquement pour la documentation
    responses={ 404: { "description": "User not found" } } # Infique toutes les erreurs possible, uniquement pour la documentation
)

@router.get("/")
async def read_users():
    return test_users

@router.get("/{user_id}")
async def read_user(user_id: int):
    if user_id < 0 or user_id >= len(test_users):
        raise HTTPException(status_code=404, detail=f"ID {user_id} does not exist")
    return test_users[user_id]