from fastapi import APIRouter, HTTPException
from starlette import status
from ..database import db_dependency
from .service import authenticate_user
from ..schemas.users import UserLogin

auth_router = APIRouter(
    tags=['auth'],
)



@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(db: db_dependency, user: UserLogin):
    user = authenticate_user(username=user.username, password= user.password, db=db)

    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Wrong credentials")
    
