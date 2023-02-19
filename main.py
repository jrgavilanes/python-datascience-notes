from flask import Flask

app = Flask(__name__)

import features.users.UserController as userController

print(f"Route loaded: {userController}")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)
