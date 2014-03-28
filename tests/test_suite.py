import os
import unittest
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from pyvly import database, main, models


class PyVlyTestSuite(unittest.TestCase):

    def setUp(self):
        # Setup the testing environment
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

        # Create a database for the tests
        _basedir = os.path.abspath(os.path.dirname(__file__))
        database_uri = "sqlite:///" + os.path.join(_basedir, "test.db")
        self.engine = create_engine(database_uri)

        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=self.engine))

        database.Model.metadata.create_all(self.engine)

    def tearDown(self):
        # Clear the db
        database.Model.metadata.drop_all(self.engine)
        self.db_session.remove()
