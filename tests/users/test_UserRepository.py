import unittest
from io import StringIO

from features.users.UserRepository import user_default_values, UserModel, UserRepository


class TestUserDefaultValues(unittest.TestCase):

    def test_default_values(self):
        expected = {
            "id": None,
            "name": None,
            "email": None,
            "password": None,
            "country": None
        }
        self.assertEqual(user_default_values(), expected)


class TestUserModel(unittest.TestCase):

    def test_valid_user(self):
        user = UserModel(1, "John Doe", "john.doe@example.com", "secret", "USA")
        expected = {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "secret",
            "country": "USA"
        }
        self.assertEqual(user.to_dict(), expected)

    def test_invalid_user(self):
        with self.assertRaises(Exception) as context:
            UserModel()
        self.assertTrue("user_id no informado" in str(context.exception))

        with self.assertRaises(Exception) as context:
            UserModel(1, "John Doe", "john.doe@example.com", "secret")
        self.assertTrue("country no informado" in str(context.exception))


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.csv_data = StringIO("""id,name,email,password,country
                                   1,John Doe,john.doe@example.com,secret,USA
                                   2,Jane Doe,jane.doe@example.com,secret,Canada
                                   """)
        self.repo = UserRepository(csv_file=self.csv_data, sep=',')

    def test_get_next_id(self):
        self.assertEqual(self.repo.get_next_id(), 3)

        self.repo.users = {}
        self.assertEqual(self.repo.get_next_id(), 1)

    def test_get_by_id(self):
        expected = {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "secret",
            "country": "USA"
        }
        self.assertEqual(self.repo.get_by_id(1), expected)

        expected = {}
        self.assertEqual(self.repo.get_by_id(3), expected)

    def test_get_all_records(self):
        expected = {
            1: {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "password": "secret",
                "country": "USA"
            },
            2: {
                "id": 2,
                "name": "Jane Doe",
                "email": "jane.doe@example.com",
                "password": "secret",
                "country": "Canada"
            }
        }
        self.assertEqual(self.repo.get_all_records(), expected)

    def test_upsert(self):
        expected = {
            "id": 3,
            "name": "new name",
            "email": "new email",
            "password": "new pass",
            "country": "new c"
        }
        self.repo.upsert(UserModel(user_id=3, name="new name", email="new email", password="new pass", country="new c"))
        result = self.repo.get_by_id(3)
        self.assertEqual(result, expected)

        expected = {
            "id": 3,
            "name": "mod name",
            "email": "mod email",
            "password": "mod pass",
            "country": "mod c"
        }

        self.repo.upsert(UserModel(user_id=3, name="mod name", email="mod email", password="mod pass", country="mod c"))
        result = self.repo.get_by_id(3)
        self.assertEqual(result, expected)

    def test_delete(self):
        expected = {
            2: {
                "id": 2,
                "name": "Jane Doe",
                "email": "jane.doe@example.com",
                "password": "secret",
                "country": "Canada"
            }
        }

        self.repo.delete_by_id(1)
        self.assertEqual(self.repo.get_all_records(), expected)

        result = self.repo.delete_by_id(1)
        self.assertEqual(result, 0)
