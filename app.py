from flask import Flask
from learning import learning_blueprint


app=Flask(__name__)

app.register_blueprint(learning_blueprint, url_prefix="/greetings") #done to make app.py access the blueprint


# @app.route("/")
# def home():
#     return "Hello world"

if __name__ == '__main__':
    app.run()