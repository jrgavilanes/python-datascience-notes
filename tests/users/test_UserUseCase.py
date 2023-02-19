import unittest
from unittest.mock import MagicMock

from features.users.UserRepository import UserModel
from features.users.UserUseCase import UserUseCase


class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        self.user_repository = MagicMock()
        self.userUseCase = UserUseCase(self.user_repository)

    def test_initialization(self):
        with self.assertRaises(Exception):
            UserUseCase()

    def test_get_next_id(self):
        self.user_repository.get_next_id.return_value = 1
        next_id = self.userUseCase.get_next_id()
        self.assertEqual(next_id, 1)

    def test_get_by_id(self):
        record_id = 1
        user_data = {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'password': '123456', 'country': 'USA'}
        self.user_repository.get_by_id.return_value = user_data
        returned_user_data = self.userUseCase.get_by_id(record_id)
        self.assertEqual(returned_user_data, user_data)

        record_id = 999
        self.user_repository.get_by_id.return_value = None
        returned_user_data = self.userUseCase.get_by_id(record_id)
        self.assertIsNone(returned_user_data)

    def test_get_all_records(self):
        user_data_1 = {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'password': '123456', 'country': 'USA'}
        user_data_2 = {'id': 2, 'name': 'Jane Doe', 'email': 'janedoe@example.com', 'password': '654321', 'country': 'UK'}
        all_records = [user_data_1, user_data_2]
        self.user_repository.get_all_records.return_value = all_records
        returned_all_records = self.userUseCase.get_all_records()
        self.assertEqual(returned_all_records, all_records)

    def test_upsert(self):
        user_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'password': '123456', 'country': 'USA'}
        request_method = 'POST'
        self.user_repository.get_next_id.return_value = 1
        new_user = self.userUseCase.upsert(user_data, request_method)
        self.assertIsInstance(new_user, UserModel)

        user_data = {'id': 1, 'name': 'Jane Doe', 'email': 'janedoe@example.com', 'password': '654321', 'country': 'UK'}
        request_method = 'PUT'
        updated_user = self.userUseCase.upsert(user_data, request_method)
        self.assertIsInstance(updated_user, UserModel)

    def test_delete_by_id(self):
        record_id = 1
        self.user_repository.delete_by_id.return_value = 1
        deleted_count = self.userUseCase.delete_by_id(record_id)
        self.assertEqual(deleted_count, 1)

        record_id = 999
        self.user_repository.delete_by_id.return_value = 0
        deleted_count = self.userUseCase.delete_by_id(record_id)
        self.assertEqual(deleted_count, 0)

    def test_commit(self):
        csv_file = 'test.csv'
        sep = ','
        self.user_repository.commit.return_value = 'Records saved successfully.'
        message = self.userUseCase.commit(csv_file, sep)
        self.assertEqual(message, 'Records requested to be saved.')


if __name__ == '__main__':
    unittest.main()
