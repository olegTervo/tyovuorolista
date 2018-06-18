from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.hours.models import Hours
from application.staff.models import Staff
from application.hours.forms import HoursForm

@app.route("/hours/<staff_id>/", methods=["GET"])
def hours_index(staff_id):
    return render_template("hours/list.html", hours = Hours.your_hours(staff_id))

@app.route("/hours/<staff_id>")
@login_required
def hours_form(staff_id):
    return render_template("hours/new/" + str(staff_id), form = HoursForm())

@app.route("/hours/new/<staff_id>", methods=["POST"])
@login_required
def hours_create(staff_id):
    form = HoursForm(request.form)
  
    if not form.validate():
        return render_template("hours/new.html", form = form)

    n = Hours(request.form.get("date"), request.form.get("begins"), request.form.get("ends"), staff_id)
    #n.staff_id = staff_id
    
    db.session().add(n)
    db.session().commit()

    return redirect(url_for("hours_index"))
