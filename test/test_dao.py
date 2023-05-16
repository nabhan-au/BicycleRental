import unittest
from bicyclerental.utilities.session_db import SessionDB
from bicyclerental.utilities.dao.users_dao import UsersDao
from bicyclerental.utilities.dao.bicycle_dao import BicycleDAO

class TestSessionDB(unittest.TestCase):

    dao: SessionDB

    @classmethod
    def setUpClass(cls) -> None:
        cls.dao = SessionDB('sqlite:///:memory:')
    
    def test_get_user_dao(self):
        self.assertIsInstance(self.dao.get_users(), UsersDao)
    
    def test_get_bicycle_dao(self):
        self.assertIsInstance(self.dao.get_bicycle(), BicycleDAO)


if __name__ == '__main__':
    unittest.main()
