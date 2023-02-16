import pandas as pd
from flask import Flask, jsonify, request

users = pd.read_csv("users.csv", sep=";", index_col="id")

DEFAULT_VALUES = {
    "email": "",
    "password": "",
    "name": "",
    "country": ""
}

app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"message": "ve a /users"})


@app.route("/users", methods=["GET"])
def get_all_users():
    result = users.reset_index().to_dict("records")
    response = jsonify({"result": "OK", "users": result})
    response.status_code = 200
    return response


@app.route("/users", methods=["POST"])
def insert_user():
    # global users
    #
    # id_user = int(users.id.max() + 1)
    # email = ""
    # password = ""
    # name = ""
    # country = ""
    #
    # if "id" in request.json:
    #     id_user = request.json["id"]
    #
    # if "email" in request.json:
    #     email = request.json["email"]
    #
    # if "password" in request.json:
    #     password = request.json["password"]
    #
    # if "name" in request.json:
    #     name = request.json["name"]
    #
    # if "country" in request.json:
    #     country = request.json["country"]
    #
    # user = {
    #     "id": id_user,
    #     "email": email,
    #     "password": password,
    #     "name": name,
    #     "country": country
    # }
    #
    # users = users.append(user, ignore_index=True)
    #
    # response = jsonify({"result": "OK", "user": user})
    # response.status_code = 200
    #
    # return response

    global users

    # Obtener los valores de los campos del cuerpo de la solicitud
    user_data = request.get_json()
    user = {field: user_data.get(field, default) for field, default in DEFAULT_VALUES.items()}

    # Si no se informa id, generar el id del usuario
    # if "id" in user_data:
    #     user["id"] = user_data["id"]
    # else:
    #     user["id"] = users["id"].max() + 1
    # user["id"] = user_data.get("id", users["id"].max() + 1)

    if "id" not in user:
        max_id = users.index.tolist()[-1]
        user["id"] = max_id + 1

    # Agregar el usuario al DataFrame de usuarios

    users = users.append(user, ignore_index=True)

    # Crear la respuesta
    response = jsonify({"result": "OK", "user": user})
    response.status_code = 200

    return response


@app.route("/users/<int:id_user>", methods=["GET"])
def get_user_by_id(id_user: int):
    if id_user in users.index:
        result = users.loc[id_user].to_dict()
        result["id"] = id_user
        response = jsonify({"result": "OK", "user": result})
        response.status_code = 200
    else:
        response = jsonify({"result": "KO", "message": "Not found"})
        response.status_code = 404
    return response


@app.route("/users/<int:id_user>", methods=["DELETE"])
def delete_user(id_user: int):
    if id_user in users.index:
        users.drop(id_user, inplace=True)
        return jsonify({"result": "OK", "message": "User deleted"}), 200
    else:
        return jsonify({"result": "KO", "message": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=4000)
