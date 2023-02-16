import json
import uuid

import pandas as pd


class User:
    def __init__(self, user_id=uuid.UUID, name="", email="", password="", country=""):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.country = country

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "country": self.country
        }


path_file = "users.csv"
file_separator = ";"


class UserRepository:
    def __init__(self, csv_file=path_file, sep=file_separator):
        self.csv_file = path_file
        self.sep = file_separator
        self.users_pd = pd.read_csv(filepath_or_buffer=csv_file, sep=sep)
        self.users = {}
        for user in self.users_pd.to_dict("records"):
            self.users[user["id"]] = user

    def get_by_id(self, record_id: int):
        if record_id in self.users:
            return self.users[record_id].copy()
        return None

    def get_all_records(self):
        return self.users.copy()

    def upsert(self, user: User):
        self.users[user.id] = user.to_dict()

    def delete(self, user: User):
        if user.id in self.users:
            del self.users[user.id]

    def commit(self, csv_file=None, sep=None):
        if csv_file is None:
            csv_file = self.csv_file

        if sep is None:
            sep = self.sep

        records = json.dumps(list(self.users.values()))
        csv_json = pd.read_json(records)
        csv_json.to_csv(csv_file, sep, index=False)
        self.users_pd = pd.read_csv(filepath_or_buffer=csv_file, sep=sep)
