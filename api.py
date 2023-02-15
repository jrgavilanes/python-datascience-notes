import pandas as pd
from flask import Flask, jsonify, request

users = pd.read_csv("users.csv", sep=";")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"message": "ve a /users"})


@app.route("/users", methods=["GET"])
def get_all_users():
    result = [user for user in users.to_dict("records")]
    response = jsonify({"result": "OK", "users": result})
    response.status_code = 200

    return response


@app.route("/users", methods=["POST"])
def insert_user():
    global users

    id_user = int(users.id.max() + 1)
    email = ""
    password = ""
    name = ""
    country = ""

    if "id" in request.json:
        id_user = request.json["id"]

    if "email" in request.json:
        email = request.json["email"]

    if "password" in request.json:
        password = request.json["password"]

    if "name" in request.json:
        name = request.json["name"]

    if "country" in request.json:
        country = request.json["country"]

    user = {
        "id": id_user,
        "email": email,
        "password": password,
        "name": name,
        "country": country
    }

    users = users.append(user, ignore_index=True)

    response = jsonify({"result": "OK", "user": user})
    response.status_code = 200

    return response


@app.route("/users/<int:id_user>", methods=["GET"])
def get_user_by_id(id_user: int):
    x = users[users["id"] == id_user]
    result = x.to_dict("records")
    if len(result):
        response = jsonify({"result": "OK", "user": result[0]})
    else:
        response = jsonify({"result": "KO", "message": "Not found"})
        response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)
