from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost/flasktutorialBabyTracker"
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
