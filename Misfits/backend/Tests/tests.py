import unittest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models.user import User

class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Replace passwd with your mysql password
        user_name="root" # Mysql user
        passwd="" # Mysql user password
        db="Misfits" # Database name
        # Create an in-memory SQLite database for testing
        cls.engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user_name, passwd, db), pool_pre_ping=True)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        # Create the User table
        User.metadata.create_all(cls.engine)

    def setUp(self):
        # Start a new transaction for each test
        self.transaction = self.session.begin()

    def tearDown(self):
        # Rollback the transaction after each test
        self.transaction.rollback()

    def test_user_creation(self):
        # Create a new User object
        user = User(id=1, name='John Doe', email='johndoe@example.com', passwd='password')

        # Add the user to the session
        self.session.add(user)
        self.session.commit()

        # Retrieve the user from the session by ID
        retrieved_user = self.session.query(User).get(1)

        # Assert that the retrieved user matches the original user
        self.assertEqual(retrieved_user.id, 1)
        self.assertEqual(retrieved_user.name, 'John Doe')
        self.assertEqual(retrieved_user.email, 'johndoe@example.com')
        self.assertEqual(retrieved_user.passwd, 'password')

if __name__ == '__main__':
    unittest.main()
