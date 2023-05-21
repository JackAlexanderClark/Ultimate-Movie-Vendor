// custom javascript
function alertUser() {

  const confirmDelete = confirm("Are you sure you want to delete this DVD?");

  if (!confirmDelete) {
    // Cancel the button click
    return false;
  }
}

function alertUserReview() {

  const confirmDeleteReview = confirm("Are you sure you want to delete this Review?");

  if (!confirmDeleteReview) {
    // Cancel the button click
    return false;
  }
}

function alertUserUpdate() {

  const confirmUpdate = confirm("Would you like to update this DVD?");

  if (!confirmUpdate) {

    return false;
  }
}

function alertAddReview() {

  const confirmUpdate = confirm("Would you like to add a review to this DVD?");

  if (!confirmUpdate) {

    return false;
  }
}
