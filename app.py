import os

from flask import Flask

from controller.GitHubController import github_routes

app = Flask(__name__)
github_routes(app)
app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run()
