import json

import pandas as pd

from UserRepository import User, UserRepository

u = User(name="juanra", email="hola@ya.com", password="hola", country="españa")

userRepository = UserRepository()
userRepository.upsert(User())

# users = pd.read_csv("users.csv", sep=";", index_col="id")
users = pd.read_csv("users.csv", sep=";")

dict_users = users.to_dict("records")

users_db = {}

for x in dict_users:
    users_db[x["id"]] = x

print(users_db)

users_db_json = json.dumps(list(users_db.values()))

# In [76]: list(users_db.keys())
# Out[76]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("pues")
print(x)
print("y")
csv_json = pd.read_json(users_db_json)
csv_json.to_csv("users.csv", sep=";", index=False)
