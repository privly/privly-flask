from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE_URL


class BaseModel(object):
    """Base class for all database models"""

    @classmethod
    def get(self, id):

        return self.query.filter(self.id == id).first()

    def save(self, commit=True):
        """Creates or updates a model in the database"""
        db_session.add(self)
        if commit:
            db_session.commit()

    def delete(self, commit=True):
        """Removes a model from the database"""
        db_session.remove(self)
        if commit:
            db_session.commit()

Model = declarative_base(name="Model", cls=BaseModel)

# Create database engine
engine = create_engine(DATABASE_URL, convert_unicode=True)

# Create our db session
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Attach database session to all models
Model.db_session = db_session

# Attach query property to all models
Model.query = db_session.query_property()

def init_db():
    from pyvly import models
    Model.metadata.create_all(bind=engine)
