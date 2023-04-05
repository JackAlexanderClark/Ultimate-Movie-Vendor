import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from models import db, Dvd, User, DvdReview
from helper import sort_dvd
from flask_login import LoginManager, login_required, login_user, logout_user

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL")       # connect to db with me as owner

# tell flask where we want to upload images
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
UPLOAD_FOLDER = 'static/images/'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



# initialise the app and connect to the database

# initialise login manager
login_manager = LoginManager()
login_manager.login_view = "sign_in"
login_manager.init_app(app)
db.init_app(app)

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku



# initialise login manager
@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
@login_required
def homepage():  # put application's code here
    # tell index.html we will receive object dvd_reviews that needs to be looped over
    sort_param = request.args.get("sort")
    dvds = Dvd.query.all()  # query db call all dvd

    if sort_param:
        dvds = sort_dvd(Dvd, sort_param)

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
@login_required
def add_dvds():
    if request.method == "GET":
        dvd = Dvd(name="", description="", price="", quantity="", genre="", image="")
        return render_template("add_dvd.html", dvd=dvd)
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
@app.route('/add_dvd_review/<int:id>', methods=["GET", "POST"])
@login_required
def submit_dvd_review(id):
    dvd = Dvd.query.filter_by(id=id).first()
    # build authentication to pick the currently logged in and pass into the USer
    user = User.query.first()
    if request.method == "GET":
        return render_template("dvd_review_submit.html", id=id, dvd=dvd, user=user)
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
@login_required
def update_dvd(id):
    dvd = Dvd.query.get(id)

    if not dvd:
        return render_template("index.html", message="DVD not found")

    if request.method == "GET":
        return render_template("edit_dvd.html", id=id, dvd=dvd)

    if request.method == "POST":
        dvd.name = request.form.get("name")
        dvd.description = request.form.get("description")
        dvd.price = request.form.get("price")
        dvd.quantity = request.form.get("quantity")
        dvd.genre = request.form.get("genre")

        file = request.files.get("image")

        if file:
            extension = os.path.splitext(file.filename)[1]
            image_name = str(uuid.uuid4()) + extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
            dvd.image = image_name

        db.session.commit()
        return redirect("/")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete_dvd/<int:id>', methods=["POST"])
@login_required
def delete_dvd(id):

    # id = request.form.get('id')
    dvd = Dvd.query.all()

    if id is not None:
        try:
            db.session.execute(text("DELETE FROM dvd WHERE id = :id"), {"id": id})
            db.session.commit()
            return render_template("index.html", message=f"Deleted all DVD with id {id}")
        except Exception as e:
            db.session.rollback()
            return render_template("index.html")
            #return render_template("index.html", dvd=dvd, error=f"An error occurred while deleting this DVD: {e}")

    else:
        return render_template('index.html', error="Please enter a valid DVD ID")



@login_required
@app.route('/dvd_reviews/delete_by_dvd_id', methods=['POST'])
def delete_dvd_reviews_by_dvd_id():

    dvd_id = request.form.get('dvd_id')
    dvds = Dvd.query.all()  # query db call all dvd

    if dvd_id is not None:
        try:
            db.session.execute(text("DELETE FROM dvd_review WHERE dvd_id = :dvd_id"), {"dvd_id": dvd_id})
            db.session.commit()
            return render_template("index.html", dvds=dvds)
        except Exception as e:
            db.session.rollback()
            return render_template("index.html", dvds=dvds, error=f"An error occurred while deleting this DVD review: {e}")
    # do i need to enter id into text input instead of button?
    else:
        return render_template('view_dvd_reviews.html', error="Please enter a valid DVD ID")



# display all reviews
@app.route('/reviews', methods=["GET"])
@login_required
def reviews():
    reviews = DvdReview.query.all()
    dvd = Dvd.query.all()
    user = User.query.all()

    return render_template("view_dvd_reviews.html", dvd=dvd, reviews=reviews, user=user)

# help page to illustrate how to use the app for users
@app.route('/help', methods=["GET"])
@login_required
def help():
    return render_template("help.html")

@app.route('/credits', methods=["GET"])
@login_required
def credits():
    return render_template("credits.html")

@app.route('/sign_in', methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("login_page.html", error=False)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect("/")
        else:
            return render_template("login_page.html", error=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.route('/log_out', methods=["GET"])
@login_required
def log_out():
    logout_user()
    return redirect("/sign_in")

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )













