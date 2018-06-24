from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class StaffForm(FlaskForm):
    name = StringField("Staff name")
    position = SelectField(choices=[('Tarjoilija', 'Tarjoilija'), ('Chef', 'Chef'), ('Administrator', 'Administrator')])

    class Meta:
        csrf = False
