from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserUpdate
from ..db.models.User import User as UserModel


def get_users(db: Session):
    return db.query(UserModel).all()


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    new_user = UserModel(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = get_user(db, user_id)
    if db_user is None: return None

    user_data = user_update.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        if value is not None:
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None: return None
    
    db.delete(db_user)
    db.commit()
    return True