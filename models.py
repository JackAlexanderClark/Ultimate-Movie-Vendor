from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql import func

# using sql alchemy
db = SQLAlchemy()

# every model will be a class
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)                      # id will be an integer
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(40))
    country = db.Column(db.String())
    password = db.Column(db.String(40))

    def __init__(self, firstname, lastname, email, country, password):         # initialise the model by calling self
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.country = country
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Dvd(db.Model):
    __tablename__ = "dvd"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    description = db.Column(db.String())
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())                      # image will be a URL
    image_url = db.Column(db.String())
    genre = db.Column(db.String(10))
    created_date = db.Column(db.Date, default=func.now())       # get datetime for now

    def __init__(self, name, description, price, quantity, image_url, genre):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image_url = image_url
        self.genre = genre

class DvdReview(db.Model):
    __tablename__ = "dvd_review"
    id = db.Column(db.Integer, primary_key=True)
    dvd_id = db.Column(db.Integer, db.ForeignKey("dvd.id"))
    dvd = db.relationship("Dvd", backref=backref("dvd", uselist=False))             # relation of foreign key to dvd table
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref=backref("user", uselist=False))          # related to USER table
    review = db.Column(db.String())
    rating = db.Column(db.Integer())

    def __init__(self, dvd_id, user_id, review, rating):
        self.dvd_id = dvd_id
        self.user_id = user_id
        self.review = review
        self.rating = rating


