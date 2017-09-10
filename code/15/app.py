from flask import Flask, render_template, redirect, request, url_for, session, flash
from forms import LoginForm, NewItem
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'redsfsfsfsfis'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
Bootstrap(app)

@app.route('/', methods=["GET", "POST"])
def index():
    form = NewItem(request.form)

    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            flash(f"Field : {error_field}; error : {error_message}")

    if request.method == 'POST':
        t = Todos(task=request.form[form.item.name])
        db.session.add(t)
        db.session.commit()
        #flash("Added new task")
        return redirect(url_for("index"))
        # return render_template('template.html', data=data, form=form)

    data = Todos.query.all()
    return render_template('template.html', data=data, form=form)

@app.route('/delete')
def delete():
    pass


if __name__ == '__main__':
    app.run(debug=True)
