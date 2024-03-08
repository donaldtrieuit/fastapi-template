from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from routes.deps import UserServiceDep
from schemas.user_schema import Token

router = APIRouter()


@router.post("/token")
async def login_for_access_token(
    service: UserServiceDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    token, err = service.authenticate(form_data.username, form_data.password)
    if err is not None:
        raise HTTPException(status_code=400, detail=err)
    return token
