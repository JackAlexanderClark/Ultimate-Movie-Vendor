<h1>Project 3 - Data Centric Development</h1> 

 

<h2>Ultimate Movie Vendor</h2> 

 

<h3>Author: Jack Clark</h3> 

 

<h3>Technologies: Python, PostgreSQL, SQLAlchemy, Flask, javaScript, CSS and HTML</h3> 

 

### App Heroku: https://movie-database-project.herokuapp.com/ 

 

![desktop (1)](https://user-images.githubusercontent.com/97599832/232035145-50ec5109-4ddc-468f-ad35-09f52821f395.png) 

 

<h3>1. Project Goals</h3> 

<ul> 

<li>The purpose of this project is to create an application that allows users to enter their own dvds details.</li> 

<li>Users will be able to add a DVD, update the DVD and delete it from their dashboard.</li> 

<li>The dashboards will function as the primary display for their catalogue of DVDs and their respective reviews.</li> 

<li>Search functionality: 

One of the most useful features of the application is its search functionality. Users can search their collection based on the DVD title or filter results by the most recently added DVDs and by their review ratings.</li> 

<li>The Database can be scaled and cater for a users size and the sort function can help them quickly order and look for specific DVD's by their rating or creation date. The DVD's will neatly stack append to the latest ones you have added.</li> 

<li>The dashboard will be the primary frontpage which will display the DVD's with accessible forms found upon the nav bar to submit new DVD's or reviews. 

<li>A DVD can be updated to keep up to date with quantity changes.</li> 

<li>Similarly, DVD reviews can be added and updated whenever is required.</li> 

</ul> 

 

 

<h3>2. Data Models</h3> 

<ul> 

    <li>The app is based around 3 principles the "user", the "dvd" a user can own and a "dvd review" a user can write about a dvd.</li> 

    <li>This is intrinsic to the business logic of the app.</li> 

    <li>The DVD objects can be updated, read, created and deleted whenever is necessary by clear and well defined buttons on each DVD.</li> 

    <li>As seen below, this ERD diagram shows the relationships between the database tables, we can see that the DVD_REVIEW references the primary key of DVD id.</li> 

    <li>Similarly we can see that the DVD_REVIEW references the primary key of user id from USER table.</li> 

    

</ul> 

<img src="static/images/ERD diagram of tables.jpg"> 

 

<h3>What does this achieve?</h3> 

<p>This means users can log into the App with an email and password and start straight away adding their DVD collection, they can review each DVD and then use CRUD (create, read, update, delete) each record to personalise their DVD collections</p>. 

 

<h3> Business Goals </h3> 

- To allow a User to store the quantity of DVD's in their inventory for stock purposes. 

- To store the price per DVD. 

- To allow Users to review DVD's. 

- Users can compile a collection of DVD's and then order them based on their preferences such as from highest rating to lowest. 

- Users can also order their collection by the date they purchased the DVD. 

 

- This app could be the basis for communities such as movie and books clubs, who wish to remember and store all their reviews and favourite DVD's. 

![image](https://user-images.githubusercontent.com/97599832/228037084-5e519704-9511-4c7e-9821-b97b1432d9f9.png) 

 

- This app will scale be neatly appending DVD's within the dashboard which can then be sorted upon. 

 

<h3>3. Features and Development Process</h3> 

 

## Layout 

#### Dashboard 

![image](https://user-images.githubusercontent.com/97599832/231828650-4ffdafa4-ca4d-445a-bfdc-0e0f3c9f579d.png) 

<hr> 

 

#### A DVD object 

![image](https://user-images.githubusercontent.com/97599832/231828555-372dff6b-57c8-4dfe-9901-943cabf3fa35.png) 

<hr> 

 

#### User Login Form 

![image](https://user-images.githubusercontent.com/97599832/232009626-f6cdbcb5-3e93-44d7-99d1-dbed179b90a2.png) 

<hr> 

 

#### Submit a DVD Form 

![image](https://user-images.githubusercontent.com/97599832/232009972-96d59807-bb70-49ef-81e1-1e46904fa070.png) 

<hr> 

 

#### Add a DVD Review Form 

![image](https://user-images.githubusercontent.com/97599832/232010097-7f155657-c258-4f3d-8b7d-59b2aa32fe86.png) 

<hr> 

 

#### View Reviews 

![image](https://user-images.githubusercontent.com/97599832/232291553-9481b16e-fa9f-4bac-bdcf-5ab12bf95d2f.png) 

<hr> 

 

### User Experience 

- I have used JavaScript to query whether a user wishes to delete a DVD or a review, by alerting them and asking them to confirm or cancel their input. 

![image](https://user-images.githubusercontent.com/97599832/232767508-4dbbde34-5c66-4027-9002-11fa253cac9e.png) 

 

- User 1: "I found the buttons and navigation bar simple to use and to add DVD's. However, there was not a clear way to see which user had added a review." 

- Solution: Add the user who added a review/ 

 

- User 2: 

 

<h4> Wireframes and Concepts: </h4> 

 

- Early on I want a DVD to be a self-contained object that could be looped over or iterated upon. It would contain all the information pertaining to each DVD and would then display on the dashboard in whatever ordered they are stored within the database. 

![image](https://user-images.githubusercontent.com/97599832/228220314-76894dcd-2492-4336-82fc-69f4c75070e0.png) 

 

 

- This app is built with Flask and Python, using templates. 

- These templates render HTML that has in-built python scripts that call from the PostgreSQL Database. 

- Users can input data straight into the forms and then manipulate the data around the domain of DVDs and Users. 

 

![image](https://user-images.githubusercontent.com/97599832/228033308-b57220f2-1862-490d-aeef-518e8aaa47c2.png) 

 

- Custom CSS and JavaScript files are rendered on the templates. 

- The database instance is from ElephantSQL and uses their "Tiny" tier service. 

 

- If a user changes the inventory, they can use the update button to change data on the DVD such as the quantity, they can also delete the DVD if it is no longer available. 

- Similarly, they can add a review to the particular DVD by using the add review button. 

 

- The core app logic is stored in the app.py including the initialisation of Flask and SQL Database. 

 

- Helper.py contains the search ordering logic for the dashboard. 

 

- External CSS and JavaScript files are contained within the static directory. 

 

- HTML templates that are rendered by the routing inside of app.py are contained within the templates folder. 

 

- Models.py contains the database tables and classes. 

 

- The env.py file contains project specific hidden variables such as the database URL and secret project key, it is hidden on GitHub as it was included in the gitignore file. 

 

- The Procfile is for heroku and runs the app.py application. 

 

- The requirements.txt include all necessary packages used by the application. 

 

 

<h3>4. Bugs and Testing</h3> 

 

Different testing methods: 

<ol> 

    <li>User Testing: By asking people to try my application and check their user experiences and any issues they encounter.</li> 

    <li>Manual Testing: Using user experiences to inform my development and using logs to test key features.</li> 

    <li>Using code validators and checks to check for errors.</li> 

</ol> 

 

- Testing use Chrome Dev Tools to make sure the application is responsive for all types of devices such as Laptops, iPads and mobiles: 

![image](https://user-images.githubusercontent.com/97599832/232476672-110534e8-7275-4a30-bf3d-fc7e9a5b45ad.png) 

 

  

 

 -While testing my application I came across a major bug when trying to delete a DVD. Because I have a second table called DVD_REVIEW, it has a foreign key                  relationship with the primary key of DVD, the "DVD ID". So, if you create a DVD and then add a DVD review and then try to delete the DVD, the application                 will return a 500 critical error, as seen below:         

![image](https://user-images.githubusercontent.com/97599832/227781558-7f0e1e34-2468-4eaa-ba16-33ded95038fe.png) 

 

- From here we are taken to the submit DVD review form. We can then add a review which will create a record in the DVD review table with a dvd id. 

- Attempting to delete will then error. 

 

![image](https://user-images.githubusercontent.com/97599832/227781676-a482c273-f966-4523-b5d0-855f36aafde7.png) 

 

- As you can see in the above URL, "/delete_dvd/9" we are passing in the dvd id - 9 to the delete dvd, however, we have no built in functionality to also delete the record from the child table of the parent DVD table. 

- The solution I decided upon came across during research, PostgreSQL has a feature called "cascading delete" which will delete the child records when the parent record is deleted if they have a foreign key relationship". 

 

- An example query would be "ALTER TABLE child_table ADD CONSTRAINT child_fk FOREIGN KEY (parent_id) REFERENCES parent_table(id) ON DELETE CASCADE;". 

 

Solution: 

![image](https://user-images.githubusercontent.com/97599832/227782249-084ee5ce-761f-4f04-8174-d244941c3293.png) 

 

- I also changed my buttons to be wrapped in POST forms which prior the href tag was causing bugs. 

 

- I encountered another major bug when I tried to save images to my elephantSQL database. Whenever, the app would restart the dynos would restart which would cause the database instance to forget the images saved into the database. 

- Solution: I decided instead to save the Image URL to the database and then instead display them inside HTML <img> tags rather than trying to save a random string name for an image and then store the images in and upload folder. 

 

- Unresponsive Navigation Bar Bug 

- I used the w3 Schools nav bar as my previous nav bar would go out of line and break at certain breakpoints. 

![image](https://user-images.githubusercontent.com/97599832/231490168-f89a3909-c2a3-418e-8b91-7b49d5ee4f50.png) 

 

 

- Nav Bar buttons still not acting responsively 

- Fix: Using media queries to change font signs 

![image](https://user-images.githubusercontent.com/97599832/232306718-f392c8df-7cd3-4dfd-9760-c2537758f43d.png) 

 

 

- Bug - Incorrect inputs for tables 

- If you enter letters for the "price" column in the form if will crash as the column is expecting integers. 

![image](https://user-images.githubusercontent.com/97599832/231492321-e109fd41-6b72-4a8a-9d3b-2ab6436080cd.png) 

- To solve this error, we need a validation check: 

 

- Add an error message. 

 

- Change input type -- to number to prevent letters: <input type="text"> 

 

- Add error exceptions in try and catch to stop app crashing if a valid ID is not found: 

![image](https://user-images.githubusercontent.com/97599832/232299530-af7dcdd4-fe86-4ae8-a297-d46421a90e5a.png) 

 

 

 

### JavaScript Error - Reviews could still be deleted even though an alert allows you to cancel. 

![image](https://user-images.githubusercontent.com/97599832/232472641-42fa3e5b-92d8-4983-bc75-600c6582a4b7.png) 

 

Fix: I was using an onclick on the html input when I need to use a onsubmit on the form to return the javascript function, like such: 

![image](https://user-images.githubusercontent.com/97599832/232472873-e9ff9ad6-db62-4554-a2f2-4c72013ec80c.png) 

 

 

 

### Checking Code through Validators: 

#### Manual Testing 

<hr> 

 

### CSS w3 Schools Jigsaw: 

 

![image](https://user-images.githubusercontent.com/97599832/228552574-b6fe0e9c-2e27-44ad-8937-291d16f54fd4.png) 

 

### HTML Validator 

#### Page 1 - Index.html 

 

- Some of these errors correspond to being unable to recognise flask syntax. 

 

![image](https://user-images.githubusercontent.com/97599832/230635519-99be8721-e205-452e-8dee-ac462373550b.png) 

 

#### Page 2 - add_dvd.html 

![image](https://user-images.githubusercontent.com/97599832/232019330-a43509d9-0312-4362-bf91-fba59e1f6810.png) 

 

#### Page 3 - user_registration.html 

![image](https://user-images.githubusercontent.com/97599832/232022340-c18b7ff4-6502-4d89-a37d-663b86c43c9c.png) 

 

- Need to add a form action. 

 

#### Page 4 - edit_dvd.html 

![image](https://user-images.githubusercontent.com/97599832/232024177-27e61607-3768-4ac5-8f48-027c7335f34a.png) 

 

#### Page 5 - View_dvd_reviews.html 

![image](https://user-images.githubusercontent.com/97599832/232024886-b4579cbe-8713-497c-969f-aec078c81562.png) 

 

#### Page 6 - Login_page.html 

![image](https://user-images.githubusercontent.com/97599832/232025369-aa1a7b98-8341-4080-b26d-66e23d05821d.png) 

 

 

### JavaScript Validator 

https://jshint.com/ 

![image](https://user-images.githubusercontent.com/97599832/232025515-1fc3547f-da8f-4324-898f-8df1e679ea69.png) 

 

### Python Code Validator 

- Source: https://snyk.io/code-checker/python/ 

- Security Code Checker 

- Error detected when I send the error in the returned template 

![image](https://user-images.githubusercontent.com/97599832/232300790-a8bc9bde-d162-45e2-89f2-e546221f9755.png) 

 

- Use generic error message. 

 

![image](https://user-images.githubusercontent.com/97599832/232301727-8e6e044a-f54e-433d-a52a-ecd320853d60.png) 

 

 

### Deployment 

 

- This app was built using the Pycharm IDE and GitHub for version control. 

 

#### Deployment to Heroku Pages: 

 

1. In terminal you need to copy the requirements.txt and create a Procfile for Heroko to build you app. 

2. pip3 freeze --local > requirements.txt. 

3. echo web: python app.py > Procfile. 

4. Go to the Deploy tab and then Deployment Method and use GitHub. 

5. Connect your GitHub repo you wish to clone and use for the App. 

6. Set up env.py file: IP : 0.0.0.0, PORT : 5000, DATABASE_URI : DATABASE_URI", SECRET_KEY {your secret key} 

7. Use Heroku/Python build package. 

8. Connect your database instance to a provider such as elephantSQL and use the database URL for your given Database instance. 

9. You can read the logs by using "heroko logs --tail" in the project directory. 

 

To Clone this Repository: 

Terminal: $ git clone https://github.com/JackAlexanderClark/Ultimate-Movie-Vendor 

 

### Credits 

1. Jack Clark 

2. Thanks to my Code Institute Tutor (Ben Smith) for his help throughout this course. 

