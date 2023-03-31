from models import DvdReview

# order and sort functions
def sort_dvd(Dvd, param):
    if param == "newest":
        # descending order
        dvd_model = Dvd.query.order_by(Dvd.created_date.desc()).all()
    elif param == "highest_rating":
        # join tables on the primary key
        dvd_model = Dvd.query.join(DvdReview).order_by(DvdReview.rating.desc()).all()
    elif param == "lowest_rating":
        dvd_model = Dvd.query.join(DvdReview).order_by(DvdReview.rating.asc()).all()
    else:
        raise ValueError("Do you have any DVD's in your collection?")
    return dvd_model

