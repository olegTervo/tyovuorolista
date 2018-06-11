from flask import Flask, render_template
from application import app
from application.staff.models import Staff
from flask_login import login_required, current_user

@app.route("/")
@login_required
def index():

    return render_template("index.html", your_staff = Staff.your_staff(current_user.id))
