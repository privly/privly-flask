from sqlalchemy import Column, Integer, String, DateTime, Text
from pyvly.database import Model


class Post(Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    burn_after = Column(DateTime)
    random_token = Column(Text)
    privly_application = Column(String(100))



class User(Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    salt = Column(String(100))
    created = Column(DateTime)
    updated = Column(DateTime)
