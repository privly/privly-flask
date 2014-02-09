from  datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from pyvly.database import Model


class Post(Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    burn_after = Column(DateTime)
    random_token = Column(Text)
    privly_application = Column(String(100))

    def __init__(self, content, burn_after, random_token, privly_application):
        self.content = content
        self.burn_after = burn_after
        self.random_token = random_token
        self.privly_application = privly_application


class User(Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    salt = Column(String(100))
    created = Column(DateTime)
    updated = Column(DateTime)

    def __init__(self, email, password, salt):
        self.email = email
        self.password = password
        self.salt = salt
        self.created = datetime.now()
        self.updated = self.created
