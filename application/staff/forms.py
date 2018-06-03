from flask_wtf import FlaskForm
from wtforms import StringField

class StaffForm(FlaskForm):
    name = StringField("Staff name")
    position = StringField("Staff position")
 
    class Meta:
        csrf = False
