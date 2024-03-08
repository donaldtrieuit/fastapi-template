from pydantic import BaseModel


class UserLogin(BaseModel):
    password: str
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str | None = None
