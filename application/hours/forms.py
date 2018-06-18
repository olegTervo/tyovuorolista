from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField

class HoursForm(FlaskForm):
    date = DateField("Date")
    begins = DecimalField("Begins")
    ends = DecimalField("Ends")
 
    class Meta:
        csrf = False
