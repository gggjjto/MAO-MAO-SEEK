from flask import Flask

import config
from controller.GitHubController import github_routes

app = Flask(__name__)
github_routes(app)
app.secret_key = config.secret_key

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
