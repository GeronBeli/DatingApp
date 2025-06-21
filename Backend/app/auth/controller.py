from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from ..database import db_dependency
from .service import authenticate_user, create_access_token
from ..schemas.users import UserLogin
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

auth_router = APIRouter(
    tags=['auth'],prefix='/auth'
)



@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(username=form_data.username, password= form_data.password, db=db)
    token = create_access_token(user.username, timedelta(minutes=20))

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Wrong credentials")
    
    return {'access_token': token, 'token_type': 'bearer'}
    
