from fastapi import APIRouter, Request
from starlette import status
from ..database import db_dependency
from sqlalchemy import select
from ..models import Users

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