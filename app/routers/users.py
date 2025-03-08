from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..db.database import get_db
from ..db.models.user import User

# Schema Pydantic pr le renvoi de GET
class UserResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config: 
        from_attributes = True

# Schema Pydantic pr la validation de POST
class UserCreate(BaseModel):
    name: str
    age: int

# Schema Pydantic pr la validation de PATCH/PUT
class UserUpdate(BaseModel):
    name: str = None
    age: int = None

router = APIRouter(
    prefix="/users",
    tags=["users"], # Indique la catégorie du router, uniquement pour la documentation
    responses={ 404: { "description": "User not found" } } # Infique toutes les erreurs possible, uniquement pour la documentation
)

@router.get("/", response_model=list[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    return user

@router.post("/", status_code=201, response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    
    user_data = user_update.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        if value is not None:
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")
    
    db.delete(db_user)
    db.commit()
    return # Simple return, car le status 204 permet de ne rien renvoyer par défaut