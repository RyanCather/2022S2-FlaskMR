from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object(Config)  # loads the configuration for the ngunnawal.db
db = SQLAlchemy(app)            # creates the db object using the configuration

from models import Contact
from forms import ContactForm

@app.route("/")
def homepage():
    return render_template("index.html", title = "homepage")
@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = contact(name=form.name.data, email=form.email.data,message=form.message.data)
    return render_template("contact.html", title ="Contact Us", form=form)


if __name__ == '__main__':
    app.run()
