from application import db

from sqlalchemy.sql import text

class Staff(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
   date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
   onupdate=db.func.current_timestamp())

   name = db.Column(db.String(150), nullable=False)
   position = db.Column(db.String(100), nullable=False)
   work_hours = db.Column(db.Integer, nullable=False)

   account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
      nullable=False)

   def __init__(self, name, position):
      self.name = name
      self.position = position
      self.work_hours = 0

   @staticmethod
   def your_staff(account_id):
      stmt = text("SELECT Staff.id, Staff.name FROM Staff"
                     " WHERE (Staff.id == " + str(account_id) + ")")
      res = db.engine.execute(stmt)

      response = []
      for row in res:
         response.append({"id":row[0], "name":row[1]})
      
      return response