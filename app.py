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
        return render_template("add_dvd.html", dvd=False)
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
@app.route('/add_dvd_review/<int:id>', methods=["GET", "POST"])
def submit_dvd_review(id):
    dvd = Dvd.query.filter_by(id=id).first()
    # build authentication to pick the currently logged in and pass into the USer
    user = User.query.first()
    if request.method == "GET":
        return render_template("dvd_review_submit.html", dvd=dvd, user=user)
    if request.method == "POST":
        review = request.form.get("review")
        rating = request.form.get("rating")
        dvd_review = DvdReview(
            review=review,
            rating=rating,
            user_id=user.id,
            dvd_id=dvd.id,
        )
        db.session.add(dvd_review)          # add to database
        db.session.commit()                 # commit
        return redirect('/')

# update and send id
@app.route('/update_dvd/<int:id>', methods=["GET", "POST"])
def update_dvd(id):
    dvd = Dvd.query.filter_by(id=id).first()
    if request.method == "GET":
        return render_template("add_dvd.html", dvd=dvd)
    if request.method == "POST":
        dvd.name = request.form.get("name")
        dvd.description = request.form.get("description")
        dvd.price = request.form.get("price")
        dvd.quantity = request.form.get("quantity")
        dvd.genre = request.form.get("genre")
        file = request.files["image"]

        # if wish to keep same image, check if user submits new file
        if file:
            extension = os.path.splitext(file.filename)[1]
            image_name = str(uuid.uuid4()) + extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        else:
            image_name = dvd.image

        dvd.image = image_name

        db.session.commit()
        return redirect("/")

@app.route('/delete_dvd/<int:id>', methods=["GET"])
def delete_dvd(id):
    dvd = Dvd.query.filter_by(id=id).first()
    db.session.delete(dvd)
    db.session.commit()

    # return a delete successful pop up
    return redirect("/")

# display all reviews
@app.route('/reviews', methods=["GET"])
def reviews():
    reviews = DvdReview.query.all()
    return render_template("view_dvd_reviews.html", reviews=reviews)

# help page to illustrate how to use the app for users
@app.route('/help', methods=["GET"])
def help():
    return render_template("help.html")

# display the amount of gold stars on the DVD card

if __name__ == '__main__':
    app.run()
















