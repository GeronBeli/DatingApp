from typing import Annotated
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from ..database import db_dependency
from ..models import Users
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from starlette import status

load_dotenv()

SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated= 'auto')
oath2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login')


def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, str(user.password_hash)):
        return False
    return user


def create_access_token(username: str, expires_delta: timedelta):
    encode = {'sub': username}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oath2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail=' Could not validate user')
        return {'username': username}
    except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail=' Could not validate user')
                                

user_dependency = Annotated[dict, Depends(get_current_user)]

