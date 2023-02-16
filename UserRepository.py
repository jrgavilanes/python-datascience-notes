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
            "id": self.id
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "country": self.country
        }


class UserRepository:
    def __init__(self, csv_file="users.csv", sep=";"):
        self.users = pd.read_csv(filepath_or_buffer=csv_file, sep=sep)

    def get_all_users(self):
        return self.users

    def insert(self, user: User):
        self.users
