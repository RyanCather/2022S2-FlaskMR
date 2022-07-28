from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object(Config)  # loads the configuration for the ngunnawal.db
db = SQLAlchemy(app)            # creates the db object using the configuration

@app.route('/')
def homepage():  # put application's code here
    return render_template("index.html", title="Ngunnawal Country")


if __name__ == '__main__':
    app.run()
