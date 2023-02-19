import json

import requests


def test_ping():
    response = requests.get("http://localhost:4000/")
    result = json.loads(response.text)
    assert response.status_code == 200
    assert "ve a /users" == result["body"]


def test_insert_update_delete_user():
    # Get all users
    response = requests.get("http://localhost:4000/users")
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 200
    keys = set(result.keys())
    assert keys <= result.keys()

    # Create a new user without external id ( autoincrement by system )
    expected = {
        "email": "hola@ya.com",
        "password": "cucu",
        "country": "valencia",
        "name": "que pasa rei"
    }
    response = requests.post("http://localhost:4000/users", json=expected)
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 201
    id_new_user = result["id"]

    # Get new user data
    expected["id"] = id_new_user
    response = requests.get(f"http://localhost:4000/users/{id_new_user}")
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 200
    assert result == expected

    # Change user's data
    expected_changed = {
        "email": "hola@ya.com modificado",
        "password": "cucu modificado",
        "country": "valencia modificado",
        "name": "que pasa rei modificado"
    }

    # Get error because I did not set the user id
    response = requests.put("http://localhost:4000/users", json=expected_changed)
    result = json.loads(response.text)
    assert response.status_code == 400

    # Set the user id and now I can update the user info
    expected_changed["id"] = id_new_user
    response = requests.put("http://localhost:4000/users", json=expected_changed)
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 200
    assert result == expected_changed

    # New user appears in the total users list
    keys.add(id_new_user)
    response = requests.get("http://localhost:4000/users")
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 200
    keys = set(result.keys())
    assert keys <= result.keys()

    # I delete the user
    response = requests.delete(f"http://localhost:4000/users/{id_new_user}")
    result = json.loads(response.text)
    result = result["body"]
    assert response.status_code == 200
    assert result == id_new_user

    # I cannot delete it twice
    response = requests.delete(f"http://localhost:4000/users/{id_new_user}")
    assert response.status_code == 404
