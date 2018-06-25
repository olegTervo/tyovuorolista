from application import db
from application.staff.models import Staff
from sqlalchemy.sql import text

class Hours(db.Model):

   id = db.Column(db.Integer, primary_key=True)
   staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
   #staff_name = db.Column(db.String(100))

   date = db.Column(db.String(50), nullable = False )
   begins = db.Column(db.Integer)
   ends = db.Column(db.Integer)
   workHours = db.Column(db.Integer)

      
   def __init__(self, pvm, alk, loppu, staff_id):
       self.date = pvm
       self.begins = int(alk)
       self.ends = int(loppu)
       self.workHours = int(loppu) - int(alk)
       self.staff_id = staff_id

   @staticmethod
   def your_hours(staff_id):
      stmt = text("SELECT Hours.id, Hours.date, Hours.begins, Hours.ends FROM Hours"
                     " WHERE (staff_id = " + str(staff_id) + ")")
      res = db.engine.execute(stmt)

      response = []
      for row in res:
         response.append({"date":row[1], "begins":row[2], "ends":row[3], "id":row[0]})
      
      return response
