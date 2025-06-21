from fastapi import APIRouter, HTTPException, Request
from starlette import status
from ..database import db_dependency
from sqlalchemy import select
from ..models import Users
from ..schemas.users import UserLogin
from ..auth.service import bcrypt_context
import os
from ..auth.service import user_dependency

user_router = APIRouter(
    prefix='/user',
    tags=["user"]
)

def check_user_authentication(user: user_dependency):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed"
        )

@user_router.get("/")
async def get_all_users(req: Request, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    users = db.scalars(select(Users)).all()
    
    return users

@user_router.get("/{id}")
async def get_user(id: int, db: db_dependency):
    user = db.scalar(select(Users).where(Users.id == id))
    return user


@user_router.post("/")
async def create_user(user: UserLogin, db: db_dependency):

    hashed_password = bcrypt_context.hash(user.password)

    new_user = Users(
        username = user.username,
        password_hash = hashed_password,
    )

    db.add(new_user)
    db.commit()
