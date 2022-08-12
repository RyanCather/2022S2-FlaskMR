from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config.from_object(Config)  # loads the configuration for the ngunnawal.db
db = SQLAlchemy(app)            # creates the db object using the configuration

from models import Contact, todo
from forms import ContactForm

@app.route("/")
def homepage():
    return render_template("index.html", title = "homepage")
@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data,message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
    return render_template("contact.html", title ="Contact Us", form=form)



@app.route("/todoedit/<todo_id>", methods=["POST", "GET"])
def edit_note(todo_id):
    if request.method == "POST":
        db.session.query(todo).filter_by(id=todo_id).update({
            "text": request.form['text'],
            "done": True if request.form['done'] == "on" else False
        })
        db.session.commit()
    elif request.method == "GET":
        db.session.query(todo).filter_by(id=todo_id).delete()
        db.session.commit()
    return redirect("/todo", code=302)

if __name__ == '__main__':
    app.run()