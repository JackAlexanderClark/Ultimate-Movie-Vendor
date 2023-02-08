from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

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

class Dvd(db.Model):
    __tablename__ = "dvd"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    description = db.Column(db.String())
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())
    image = db.Column(db.String())                          # image will be a URL
    genre = db.Column(db.String(10))

    def __init__(self, name, description, price, quantity, image, genre):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image = image
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

    def __init__(self, dvd_id, dvd, user_id, user, review, rating):
        self.dvd_id = dvd_id
        self.dvd = dvd
        self.user_id = user_id
        self.user = user
        self.review = review
        self.rating = rating


