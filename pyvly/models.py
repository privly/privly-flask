from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, \
    ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from pyvly.database import Model


class Post(Model):
    """
    Posts are the central storage endpoint for Privly content.
    Currently two posting applications use the Post endpoint: ZeroBins push
    encrypted content to the serialized JSON storage, and Privly "posts" use
    the rendered Markdown storage.
    """
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    random_id = Column(String(100), unique=True)
    random_token = Column(Text)
    content = Column(Text)
    structured_content = Column(Text)
    burn_after = Column(DateTime)
    privly_application = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    public = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'), unique=False)
    user = relationship('User', backref='posts')

    def __init__(self,
                 random_id,
                 random_token,
                 content,
                 structured_content,
                 burn_after,
                 privly_application,
                 public,
                 user):
        self.random_id = random_id
        self.random_token = random_token
        self.content = content
        self.structured_content = structured_content
        self.burn_after = burn_after
        self.privly_application = privly_application
        self.user = user
        self.public = public
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @classmethod
    def get_user_post(cls, user, id):
        return cls.query.filter_by(user=user, random_id=id).first()        

    @classmethod
    def get_post(cls, post_id):
        return cls.query.filter_by(random_id=post_id).first()

    def url_parameters(self):
        """Get the parameters for the non-data URL parts of the model"""
        return dict(
            privlyApp=self.privly_application,
            random_token=self.random_token,
            privlyInject1=True)

    def __json__(self, permission=True):
        fmt = '%Y-%m-%dT%H:%M:%SZ'
        return dict(
                burn_after_date=self.burn_after.strftime(fmt),
                created_at=self.created_at.strftime(fmt),
                updated_at=self.updated_at.strftime(fmt),
                random_token=self.random_token,
                privly_application=self.privly_application,
                content=self.content,
                structured_content=self.structured_content,
                public=self.public,
                user_id=self.user_id,
                permissions=dict(
                    canupdate=permission,
                    candestroy=permission,
                    canshare=permission,
                    canshow=True)
            )

class User(Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(Text)
    created = Column(DateTime)
    updated = Column(DateTime)
    confirmation_token = Column(String(100))
    verified = Column(Boolean, default=False)

    def __init__(self, email, password, token):
        self.email = email
        self.password = generate_password_hash(password=password,
                                               method='pbkdf2:sha512',
                                               salt_length=128)
        self.created = datetime.now()
        self.updated = self.created
        self.confirmation_token = token

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(cls.email == email).first()

    def get_post(self, id):
        return Post.query.filter_by(user=self, id=id).first()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return unicode(self.id)