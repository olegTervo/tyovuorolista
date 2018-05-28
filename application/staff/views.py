from application import app, db
from flask import redirect, render_template, request, url_for
from application.staff.models import Staff


@app.route("/staff", methods=["GET"])
def staff_index():
    return render_template("staff/list.html", staff = Staff.query.all())

@app.route("/staff/new/")
def staff_form():
    return render_template("staff/new.html")

@app.route("/staff/<staff_id>/", methods=["POST"])
def staff_work(staff_id):

    t = Staff.query.get(staff_id)
    t.work_hours += 1
    db.session().commit()
  
    return redirect(url_for("staff_index"))

@app.route("/staff/", methods=["POST"])
def staff_create():
    n = Staff(request.form.get("name"), request.form.get("position"))

    db.session().add(n)
    db.session().commit()

    return redirect(url_for("staff_index"))
