import unittest
from unittest import mock

from bicyclerental.models.bicycle_model import Bicycle
from bicyclerental.utilities.dao.bicycle_dao import BicycleDAO
from sqlalchemy.orm.session import Session
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


def get_mock_bicycle(id):
    mock_bicycle = Bicycle()
    mock_bicycle.id = id
    mock_bicycle.type = "testType"
    mock_bicycle.brand = "testBrand"
    mock_bicycle.seat = 1
    mock_bicycle.user_id = 1
    return mock_bicycle


class TestBicycleDAO(unittest.TestCase):
    session: Session
    bicycle_dao: BicycleDAO

    @classmethod
    def setUpClass(cls) -> None:
        mock_bicycle1 = get_mock_bicycle(1)
        cls.session = UnifiedAlchemyMagicMock(data=[
            (
                [mock.call.query(Bicycle),
                mock.call.filter(Bicycle.id == 1)],
                [mock_bicycle1]
            ),
            (
                [mock.call.query(Bicycle),
                 mock.call.filter(Bicycle.type == "testType")],
                [mock_bicycle1]
            ),
            (
                [mock.call.query(Bicycle),
                 mock.call.filter(Bicycle.brand == "testBrand")],
                [mock_bicycle1]
            ),

        ])
        cls.bicycle_dao = BicycleDAO(cls.session)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.rollback()

    def test_get_bicycle_by_id(self):
        result = self.bicycle_dao.get_bicycle_from_id(1)
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_bicycle(1), result[0])

    def test_get_bicycle_by_brand(self):
        result = self.bicycle_dao.get_bicycle_from_brand("testBrand")
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_bicycle(1), result[0])

    def test_get_bicycle_by_type(self):
        result = self.bicycle_dao.get_bicycle_from_type("testType")
        self.assertTrue(len(result) == 1)
        self.assertEqual(get_mock_bicycle(1), result[0])

if __name__ == '__main__':
    unittest.main()
