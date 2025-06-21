from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes.users import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
