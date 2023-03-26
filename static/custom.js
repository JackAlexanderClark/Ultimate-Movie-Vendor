// custom javascript
function alertUser() {

  const confirmDelete = confirm("Are you sure you want to delete?");

  if (!confirmDelete) {
    // Cancel the button click
    return false;
  }
}
