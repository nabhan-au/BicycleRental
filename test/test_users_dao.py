import unittest
from unittest import mock

from bicyclerental.models.users_model import Users
from sqlalchemy.orm.session import Session
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from bicyclerental.utilities.dao.users_dao import UsersDao


def get_mock_user():
    mock_user = Users()
    mock_user.id = 1
    mock_user.age = 1
    mock_user.lastname = 'testLastname'
    mock_user.firstname = 'testFirstname'
    return mock_user


class TestUserDAO(unittest.TestCase):
    session: Session
    user_dao: UsersDao

    @classmethod
    def setUpClass(cls) -> None:
        mock_user = get_mock_user()
        cls.session = UnifiedAlchemyMagicMock(data=[
            (
                [mock.call.query(Users),
                mock.call.filter(Users.id == 1)],
                [mock_user]
            ),
            (
                [mock.call.query(Users),
                 mock.call.filter(Users.age == 1)],
                [mock_user]
            ),
            (
                [mock.call.query(Users),
                 mock.call.filter(Users.lastname == "testLastname")],
                [mock_user]
            ),
            (
                [mock.call.query(Users),
                 mock.call.filter(Users.firstname == "testFirstname")],
                [mock_user]
            ),

        ])
        cls.user_dao = UsersDao(cls.session)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.rollback()

    def test_get_user_by_id(self):
        result = self.user_dao.get_user_from_id(1)
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_user(), result[0])

    def test_get_user_by_age(self):
        result = self.user_dao.get_user_from_age(1)
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_user(), result[0])

    def test_get_user_by_firstname(self):
        result = self.user_dao.get_user_from_name("testFirstname")
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_user(), result[0])

    def test_get_user_by_lastname(self):
        result = self.user_dao.get_user_from_lastname("testLastname")
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_user(), result[0])

if __name__ == '__main__':
    unittest.main()