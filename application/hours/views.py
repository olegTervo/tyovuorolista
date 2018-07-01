from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.hours.models import Hours
from application.staff.models import Staff
from application.hours.forms import HoursForm
from sqlalchemy.sql import text

@app.route("/hours/index/<staff_id>/", methods=["GET"])
def hours_index(staff_id):
    return render_template("hours/list.html", hours = Hours.your_hours(staff_id), staff_id = staff_id)

@app.route("/hours/form/<staff_id>/", methods=["GET"])
@login_required
def hours_form(staff_id):
    return render_template("/hours/new.html", form = HoursForm(), staff_id = staff_id)

@app.route("/hours/new/<staff_id>/", methods=["POST"])
@login_required
def hours_create(staff_id):
    form = HoursForm(request.form)
  
    if not form.validate():
        return render_template("hours/new.html", form = form, staff_id=staff_id)

    n = Hours(request.form.get("date"), request.form.get("begins"), request.form.get("ends"), staff_id)
    #n.staff_id = staff_id
    
    db.session().add(n)
    db.session().commit()

    return redirect(url_for("hours_index", staff_id = staff_id))

@app.route("/hours/delete/<staff_id>/", methods=["POST"])
@login_required
def hours_delete(staff_id):
    stmt = text("DELETE FROM Hours WHERE (staff_id = " + staff_id + ")")
    allHours = db.engine.execute(stmt)

    return redirect(url_for("staff_delete", staff_id=int(staff_id)))

@app.route("/hours/deleteHour/<hour_id>/", methods=["POST"])
@login_required
def hour_delete(hour_id):
    hour = Hours.query.get(hour_id)
    staff_id = hour.staff_id

    db.session().delete(hour)
    db.session().commit()

    return redirect(url_for("hours_index", staff_id=int(staff_id)))


@app.route("/calendar/")
def calendar():
    return render_template("Month.html")
