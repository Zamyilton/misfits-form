from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    """
    User - Class for user
    Args:
        name(str) - Name of user
        id(int) - special id number
        email(str) - Email of the user
        password(str) - password of the user
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=True)
    passwd = Column(String(128), nullable=False)

    def __init__(self, id, name, email, passwd):
        self.id = id
        self.name = name
        self.email = email
        self.passwd = passwd
