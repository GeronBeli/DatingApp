from sqlalchemy import Column, Integer, String
from .database import Base



class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

