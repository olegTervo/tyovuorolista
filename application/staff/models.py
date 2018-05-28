from application import db

class Staff(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
   date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
   onupdate=db.func.current_timestamp())

   name = db.Column(db.String(150), nullable=False)
   position = db.Column(db.String(100), nullable=False)
   work_hours = db.Column(db.Integer, nullable=False)

   def __init__(self, name, position):
      self.name = name
      self.position = position
      self.work_hours = 0
