from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField

class HoursForm(FlaskForm):
    date = StringField("Date")
    begins = DecimalField("Begins")
    ends = DecimalField("Ends")
 
    class Meta:
        csrf = False
