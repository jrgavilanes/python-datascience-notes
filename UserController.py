from model.UserRepository import UserRepository
from domain.UserUseCase import UserUseCase
from config import users_csv_filepath

try:
    from __main__ import app
except:
    from main import app

from flask import jsonify, request

userUseCase = UserUseCase(user_repository=UserRepository(csv_file=users_csv_filepath))


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"message": "ve a /users"})


@app.route("/users", methods=["GET"])
def get_all_users():
    result = userUseCase.get_all_records()
    return jsonify({"result": "OK", "users": result}), 200


@app.route("/users", methods=["POST", "PUT"])
def upsert_user():
    try:
        # Obtener los valores de los campos del cuerpo de la solicitud
        user_data = request.get_json()
        new_user = userUseCase.upsert(user_data, request.method)

        return jsonify({"result": "OK", "body": new_user.to_dict()}), 200

    except Exception as e:
        return jsonify({"result": "KO", "body": str(e)}), 400


@app.route("/users/<int:id_user>", methods=["GET"])
def get_user_by_id(id_user: int):
    result = userUseCase.get_by_id(id_user)
    if result:
        return jsonify({"result": "OK", "body": result}), 200
    else:
        return jsonify({"result": "KO", "body": []}), 404


@app.route("/users/<int:id_user>", methods=["DELETE"])
def delete_user(id_user: int):
    result = userUseCase.delete_by_id(id_user)
    if result:
        return jsonify({"result": "OK", "body": result}), 200
    else:
        return jsonify({"result": "KO", "body": []}), 404


@app.route("/users/commit", methods=["GET"])
def commit_users():
    is_ok, error_message = userUseCase.commit()
    if is_ok:
        return jsonify({"result": "OK", "body": "saved ok"}), 200
    else:
        return jsonify({"result": "KO", "body": error_message}), 500
