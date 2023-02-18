from flask import Flask

app = Flask(__name__)

import UserController

if __name__ == '__main__':
    app.run(debug=True, port=4000)
