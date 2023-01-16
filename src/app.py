from flask import Flask

app = Flask(__name__)

import src.routes

if __name__ == '__main__':
    app.run(debug=True)


def get_app():
    return app
