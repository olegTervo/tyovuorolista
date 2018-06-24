from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("/auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("/auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("staff_index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_new():
    return render_template("/auth/newUserForm.html", form = LoginForm())

@app.route("/auth/", methods=["POST"])
def user_create():
    form = LoginForm(request.form)
  
    if not form.validate():
        return render_template("/auth/newUserForm.html", form = form)

    n = User(request.form.get("username"), request.form.get("username"), request.form.get("password"))

    db.session().add(n)
    db.session().commit()

    return redirect(url_for("index"))
