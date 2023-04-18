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