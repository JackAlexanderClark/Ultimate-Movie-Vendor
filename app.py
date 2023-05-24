import os
from sqlalchemy import text
from flask import Flask, render_template, request, redirect, url_for
from models import db, Dvd, User, DvdReview
from helper import sort_dvd
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from urllib.parse import urlparse

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL")       # connect to db with me as owner

# tell flask our secret key from env.py
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

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
        user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
        )
        db.session.add(user)                # add to database
        db.session.commit()                 # commit
        return redirect('/')

@app.route('/')
@login_required
def index():
    dvd_added = request.args.get('dvd_added', False, type=bool)
    dvd_id = request.args.get('dvd_id', None, type=int)

    return render_template("index.html", dvd_added=dvd_added, dvd_id=dvd_id)


@app.route('/add_dvd', methods=["GET", "POST"])
@login_required
def add_dvds():

    if request.method == "GET":
        dvd = Dvd(name="", description="", price="", quantity="", genre="", image_url="")
        return render_template("add_dvd.html", dvd=dvd)

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        quantity = request.form.get("quantity")
        genre = request.form.get("genre")
        image_url = request.form.get("image_url")

        # Verify that the URL starts with http:// or https://
        parsed_url = urlparse(image_url)
        if parsed_url.scheme not in ['http', 'https']:
            message = "Invalid image URL. Please make sure it starts with http:// or https://."
            dvd = Dvd(name="", description="", price="", quantity="", genre="", image_url="")
            return render_template("add_dvd.html", dvd=dvd, message=message)

        dvd = Dvd(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            image_url=image_url,
            genre=genre
        )
        db.session.add(dvd)  # add to database
        db.session.commit()  # commit

        return redirect(url_for('index', dvd_added=True, dvd_id=dvd.id))


# submit users review for movies
@app.route('/add_dvd_review/<int:id>', methods=["GET", "POST"])
@login_required
def submit_dvd_review(id):
    dvd = Dvd.query.filter_by(id=id).first()

    if request.method == "GET":
        return render_template("dvd_review_submit.html", id=id, dvd=dvd)
        #user=user
    if request.method == "POST":
        review = request.form.get("review")
        rating = request.form.get("rating")
        #user_fullname = request.form.get("user_fullname")  # Getting user fullname from the request
        dvd_review = DvdReview(
            review=review,
            rating=rating,
            #user_id=user.id,
            dvd_id=dvd.id,
        )
        db.session.add(dvd_review)          # add to database
        db.session.commit()                 # commit
        return redirect(url_for('show_review', dvd_id=dvd.id))


# start of logic for user reviews
    #### finish and build upon
    @app.route('/show_review', methods=["GET"])
    @login_required
    def show_review():
        user_fullname = request.args.get('fullname')
        dvd_id = request.args.get('dvd_id')
        dvd_review = DvdReview.query.filter_by(dvd_id=dvd_id).first()

        if dvd_review is None:
            return "No review found for this DVD."

        return render_template("review_display.html", fullname=user_fullname, review=dvd_review.review,
                               dvd=dvd_review.dvd.name)


# update and send dvd id
@app.route('/update_dvd/<int:id>', methods=["GET", "POST"])
@login_required
def update_dvd(id):
    dvd = Dvd.query.get(id)

    if not dvd:
        return render_template("index.html", message="DVD not found")

    # Remove spaces around the price and quantity values
    dvd.price = str(dvd.price).strip()
    dvd.quantity = str(dvd.quantity).strip()

    if request.method == "GET":
        return render_template("edit_dvd.html", id=id, dvd=dvd)

    if request.method == "POST":
        dvd.name = request.form.get("name")
        dvd.description = request.form.get("description")
        dvd.price = request.form.get("price")
        dvd.quantity = request.form.get("quantity")
        dvd.genre = request.form.get("genre")
        dvd.image_url = request.form.get("image_url")

        # Verify that the URL starts with http:// or https://
        parsed_url = urlparse(dvd.image_url)
        if parsed_url.scheme not in ['http', 'https']:
            message = "Invalid image URL. Please make sure it starts with http:// or https://."
            dvd = Dvd(name="", description="", price="", quantity="", genre="", image_url="")
            return render_template("add_dvd.html", dvd=dvd, message=message)

        dvd.image_url = dvd.image_url

        db.session.commit()
        message = f"DVD {dvd.id} has been successfully updated."
        return render_template("index.html", dvd=dvd, message=message)





@app.route('/delete_dvd/<int:id>', methods=["POST"])
@login_required
def delete_dvd(id):
    dvds = Dvd.query.all()

    if id is not None:
        try:
            dvds = Dvd.query.get(id)  # Retrieve the DVD object with the given ID
            if dvds:
                db.session.delete(dvds)  # Delete
                db.session.commit()
                message = f"Deleted DVD with id {id}"
                return render_template("index.html", dvds=dvds, message=message)
            else:
                error = "DVD not found"
                return render_template("index.html", error=error)
        except Exception as e:
            db.session.rollback()
            print("Error during deletion:", e)  # Print the exception message
            error = "Invalid DVD ID"
            return render_template("index.html", error=error)

    else:
        error = "Please enter a valid DVD ID"
        return render_template('index.html', error=error)


@app.route('/dvd_reviews/delete_by_dvd_id', methods=['POST'])
@login_required
def delete_dvd_reviews_by_dvd_id():

    dvd_id = request.form.get('dvd_id')
    dvds = Dvd.query.all()  # query db call all dvd

    if dvd_id is not None:
        dvd_review = DvdReview.query.filter_by(dvd_id=dvd_id).first()

        if dvd_review is not None:
            review_user = load_user(dvd_review.user_id)

            if review_user == current_user:
                try:
                    db.session.delete(dvd_review)
                    db.session.commit()
                    message = "DVD review successfully deleted"
                    return render_template("index.html", dvds=dvds, message=message)
                except Exception as e:
                    db.session.rollback()
                    error = "An error occurred while deleting this DVD review. Please try again later."
                    return render_template("index.html", dvds=dvds, error=error)
            else:
                error = "Incorrect user"
                return render_template("index.html", dvds=dvds, error=error)
        else:
            error = "DVD review not found"
            return render_template("index.html", dvds=dvds, error=error)

    else:
        error = "Please enter a valid DVD ID"
        return render_template('view_dvd_reviews.html', error=error)



# display all reviews
@app.route('/reviews', methods=["GET"])
@login_required
def reviews():

    reviews = DvdReview.query.all()
    dvd = Dvd.query.all()
    user = User.query.all()

    return render_template("view_dvd_reviews.html", dvd=dvd, reviews=reviews, user=user)

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

# @app.route('/get_current_user')
# def get_current_user():
#     if current_user.is_authenticated:
#         return {
#             "user_id": current_user.id,
#             "first_name": current_user.firstname,
#             "last_name": current_user.lastname,
#             "email": current_user.email
#         }
#         print(user_data)  # prints the user details to the terminal
#         return user_data
#     else:
#         print("No user is currently logged in")  # prints the message to the terminal
#         return {"error": "No user is currently logged in"}
#
# get_current_user()

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













