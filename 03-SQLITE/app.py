from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask("sqlite")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'
db = SQLAlchemy(app)

class Kanna(db.Model) :
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    remarks = db.Column(db.Text)

    def __init__(self , name , age , remarks):
        self.name = name
        self.age = age 
        self.remarks = remarks



    #CREATE
db.create_all()
Tom = Kanna("tom" , 21 , "ok")
db.session.add(Tom)
db.session.commit()
app.run(5000 , debug = True)

    # Read
r1 = Kanna.query.get(1)
print(r1.name , r1.age)
rall = Kanna.query.all()
print(rall[0].name)
rage = Kanna.query.filter_by(remarks = "ok")
print(rage.all[1].name)

    #update

r2 = Kanna.query.get(1)
r2.age = 15
db.session.add(r2)
db.session.commit()

    # delete

r3 = Kanna.query.get(1)
db.session.delete(r3)
db.session.commit()

