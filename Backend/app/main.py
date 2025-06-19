from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes.users import user_router


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
