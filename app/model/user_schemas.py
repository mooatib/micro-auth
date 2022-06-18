from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str

    class Config:
        orm_mode = True


class UserEncrypted(User):
    password: str

    class Config:
        orm_mode = True
