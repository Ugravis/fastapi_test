from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int


class UserResponse(UserBase):
    id: int

    class Config: 
        from_attributes = True


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None