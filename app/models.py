from flask_security import UserMixin
from . import db

class Owner(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    mycars = db.relationship('Cars', backref='owner', cascade="all,delete")
    
    def __str__(self):
        return self.name

class Cars(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(25), nullable=False)
    model = db.Column(db.String(25), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    myowner = db.relationship('Owner')

    def __str__(self):
        return self.owner

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    active = db.Column(db.Boolean, default=True)

