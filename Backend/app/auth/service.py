from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from ..database import db_dependency
from ..models import Users

load_dotenv()

SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated= 'auto')


def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, str(user.password_hash)):
        return False
    return user