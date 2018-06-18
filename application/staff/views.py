from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.staff.models import Staff
from application.staff.forms import StaffForm


@app.route("/staff", methods=["GET"])
@login_required
def staff_index():
    return render_template("staff/list.html", staff = Staff.your_staff(current_user.id))

@app.route("/staff/new/")
@login_required
def staff_form():
    return render_template("staff/new.html", form = StaffForm())

@app.route("/staff/<staff_id>/", methods=["POST"])
@login_required
def staff_work(staff_id):

    t = Staff.query.get(staff_id)
    t.work_hours += 1
    db.session().commit()
  
    return redirect(url_for("staff_index"))

@app.route("/staff/delete/<staff_id>/", methods=["POST"])
@login_required
def staff_delete(staff_id):
    t = Staff.query.get(staff_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("staff_index"))

@app.route("/staff/", methods=["POST"])
@login_required
def staff_create():
    form = StaffForm(request.form)
  
    if not form.validate():
        return render_template("staff/new.html", form = form)

    n = Staff(request.form.get("name"), request.form.get("position"))
    n.account_id = current_user.id

    db.session().add(n)
    db.session().commit()

    return redirect(url_for("staff_index"))
