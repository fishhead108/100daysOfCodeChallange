from flask import Flask, render_template, redirect, request, url_for, session, flash
from forms import LoginForm, NewItem
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'redsfsfsfsfis'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def index():

    form = NewItem(request.form)

    print(f"Starting data Value : {form.starting.data}")
    print(f"Ending data Value : {form.ending.data}")
    flash(f'You submitted name {form.item.data} via button {"Starting" if form.starting.data else "Ending"}')

    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            flash(f"Field : {error_field}; error : {error_message}")
    # no such table: todos [SQL: 'INSERT INTO todos (task) VALUES (?)'] [parameters: (None,)]
    if request.method == 'POST':
        t = Todos(task=request.form[form.item.name])
        db.session.add(t)
        db.session.commit()
        flash("Added new task")
        return redirect(url_for("index"))
        #data[last_element] = request.form[form.item.name]
        # return redirect("/")
        #return render_template('template.html', data=data, form=form)

    data = Todos.query.all()
    return render_template('template.html', data=data, form=form)


if __name__ == '__main__':
    app.run(debug=True)
