from application import db

class Hours(db.Model):
   id = db.Column(db.Integer, primary_key=True)

   staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
   hour = db.Column(db.Integer, nullable=False)
   
   def __init__(self, hour):
       self.hour = hour

