from flask import Flask, jsonify, request

from UserRepository import UserRepository, user_default_values, User

userRepository = UserRepository(csv_file="users.csv")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"message": "ve a /users"})


@app.route("/users", methods=["GET"])
def get_all_users():
    result = userRepository.get_all_records()
    return jsonify({"result": "OK", "users": result}), 200


@app.route("/users", methods=["POST", "PUT"])
def upsert_user():
    try:
        # Obtener los valores de los campos del cuerpo de la solicitud
        user_data = request.get_json()
        user = {field: user_data.get(field, default) for field, default in user_default_values().items()}

        if user["id"] is None and request.method == "POST":
            user["id"] = userRepository.get_next_id()

        new_user = User(user_id=user["id"],
                        name=user["name"],
                        email=user["email"],
                        password=user["password"],
                        country=user["country"]
                        )

        userRepository.upsert(new_user)

        return jsonify({"result": "OK", "body": new_user.to_dict()}), 200

    except Exception as e:
        return jsonify({"result": "KO", "body": str(e)}), 400


@app.route("/users/<int:id_user>", methods=["GET"])
def get_user_by_id(id_user: int):
    result = userRepository.get_by_id(id_user)
    if result:
        return jsonify({"result": "OK", "body": result}), 200
    else:
        return jsonify({"result": "KO", "body": []}), 404


@app.route("/users/<int:id_user>", methods=["DELETE"])
def delete_user(id_user: int):
    result = userRepository.delete_by_id(id_user)
    if result:
        return jsonify({"result": "OK", "body": result}), 200
    else:
        return jsonify({"result": "KO", "body": []}), 404


@app.route("/users/commit", methods=["GET"])
def commit_users():
    is_ok, error_message = userRepository.commit()
    if is_ok:
        return jsonify({"result": "OK", "body": "saved ok"}), 200
    else:
        return jsonify({"result": "KO", "body": error_message}), 500


if __name__ == '__main__':
    app.run(debug=True, port=4000)
