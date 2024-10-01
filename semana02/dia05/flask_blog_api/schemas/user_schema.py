from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    status: bool

class UpdateUserSchema(UserSchema):
    password: Optional[str] = None
    password_confirm: Optional[str] = None

class LoginSchema(BaseModel):
    email: str
    password: str

class RefreshSchema(BaseModel):
    refresh_token: str