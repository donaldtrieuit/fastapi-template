from datetime import timedelta

from sqlalchemy.orm import Session

from common.email import validate_email
from core import security
from core.config import settings
from repositories.user_repo import get_user_by_email, get_user_by_username
from schemas.user_schema import Token


class UserService:

    def __init__(self, db: Session):
        self._db = db

    def authenticate(
        self, user_name: str, password: str
    ) -> tuple[None, str] | tuple[Token, None]:
        user = (
            get_user_by_email(self._db, user_name)
            if validate_email(user_name)
            else get_user_by_username(self._db, user_name)
        )
        if not user:
            return None, "User not found"
        if not security.verify_password(password, user.password):
            return None, "Wrong password"
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return (
            Token(
                access_token=security.create_access_token(
                    user.id, expires_delta=access_token_expires
                )
            ),
            None,
        )
