from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ....db.database import get_db
from ....schemas.user import UserCreate, UserUpdate, UserResponse
from ....services import user_service


router = APIRouter(
    prefix="/users",
    tags=["users"], # Indique la catégorie du router, uniquement pour la documentation
    responses={ 404: { "description": "User not found" } } # Infique toutes les erreurs possible, uniquement pour la documentation
)


@router.get("/", response_model=list[UserResponse])
def read_users(
    db: Session = Depends(get_db)
):
    users = user_service.get_users(db)
    return users


@router.get("/{user_id}", response_model=UserResponse)
def read_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    user = user_service.get_user(db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    return user


@router.post("/", status_code=201, response_model=UserResponse)
def create_user(
    user: UserCreate, 
    db: Session = Depends(get_db)
):
    return user_service.create_user(db, user=user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int, 
    user_update: UserUpdate, 
    db: Session = Depends(get_db)
):
    db_user = user_service.update_user(db, user_id=user_id, user_update=user_update)

    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    return db_user


@router.delete("/{user_id}", status_code=204)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    success = user_service.delete_user(db, user_id=user_id)
    
    if not success:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    return # Simple return, car le status 204 permet de ne rien renvoyer par défaut