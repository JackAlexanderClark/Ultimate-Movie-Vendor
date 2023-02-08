import os
import uuid

from flask import Flask, render_template, request, redirect
from models import db, Dvd, User, DvdReview



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jack_movie:4576@localhost:5432/movie"       # connect to db with me as owner
# tell flask where we want to upload images
app.config["UPLOAD_FOLDER"] = "static/images"
# initialise the app and connect to the database
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def homepage():  # put application's code here
    # tell index.html we will receive object dvd_reviews that needs to be looped over
    dvds = Dvd.query.all()              # query db call all dvd
    return render_template("index.html", dvds=dvds)

# get user information and store in database
@app.route('/user_register', methods=["GET", "POST"])
def register_user():
    if request.method == "GET":
        return render_template("user_registration.html")
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        country = request.form.get("country")
        user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            country=country,
        )
        db.session.add(user)                # add to database
        db.session.commit()                 # commit
        return redirect('/')

# add movies into database
@app.route('/add_dvd', methods=["GET", "POST"])
def add_dvds():
    if request.method == "GET":
        return render_template("add_dvd.html")
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        quantity = request.form.get("quantity")
        genre = request.form.get("genre")
        file = request.files["image"]
        extension = os.path.splitext(file.filename)[1]
        # f_name generate random string + "png"
        image_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        dvd = Dvd(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            image=image_name,
            genre=genre
        )
        db.session.add(dvd)                # add to database
        db.session.commit()                 # commit
        return redirect('/')

# submit users review for movies
# need to fix and set up foreign keys
@app.route('/dvd_review_register', methods=["GET", "POST"])
def submit_dvd_review():
    if request.method == "GET":
        return render_template("dvd_review_submit.html")
    if request.method == "POST":
        review = request.form.get("review")
        rating = request.form.get("rating")
        dvd_review = DvdReview(
            review=review,
            rating=rating,
        )
        db.session.add(dvd_review)          # add to database
        db.session.commit()                 # commit
        return redirect('/')#

# import function from scripts.py to delete a dvd record
@app.route('/')
def delete_dvd():


if __name__ == '__main__':
    app.run()
















