from fastapi import APIRouter, Request
from starlette import status
from ..database import db_dependency
from sqlalchemy import select
from ..models import Users
from ..schemas.users import UserLogin
from ..auth.service import bcrypt_context
import os

user_router = APIRouter(
    prefix='/user',
    tags=["user"]
)

@user_router.get("/")
async def get_all_users(req: Request, db: db_dependency):
    users = db.scalars(select(Users)).all()
    
    return users

@user_router.get("/{id}")
async def get_user(id: int, db: db_dependency):
    user = db.scalar(select(Users).where(Users.id == id))
    return user


@user_router.post("/")
async def create_user(user: UserLogin, db: db_dependency):
    salt = os.urandom(16).hex()

    hashed_password = bcrypt_context.hash(user.password + salt)

    new_user = Users(
        username = user.username,
        password_hash = hashed_password,
        salt = salt
    )

    db.add(new_user)
    db.commit()
