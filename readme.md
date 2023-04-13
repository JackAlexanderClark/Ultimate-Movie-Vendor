<h1>Project 3 - Data Centric Development</h1>

<h2>Ultimate Movie Vendor</h2>

<h3>Author: Jack Clark</h3>

<h3>Technologies: Python, PostgreSQL, SQLAlchemy, Flask, javaScript, CSS and HTML</h3>

<h3>1. Project Goals</h3>
<ul>
<li>The purpose of this project is to create an application that allows users to enter their own dvds details.</li>
<li>Users will be able to add a DVD, update the DVD and delete it from their dashboard.</li>
<li>The dashboards will function as the primary display for their catalogue of DVDs and their respective reviews.</li>
</ul>


<h3>2. Data Models</h3>
<ul>
    <li>The app is based around 3 principles the "user", the "dvd" a user can own and a "dvd review" a user can write about a dvd.</li>
    <li>This is intrinsic to the business logic of the app.</li>
    <li></li>
    <li>As seen below, this ERD diagram shows the relationships between the database tables, we can see that the DVD_REVIEW references the primary key of DVD id.</li>
    <li>Similarly we can see that the DVD_REVIEW references the primary key of user id from USER table.</li>
    
</ul>
<img src="static/images/ERD diagram of tables.jpg">

    <h3>What does this achieve?</h3>
    <p>This means users can log into the App with an email and password and start straight away adding their DVD collection, they can review each DVD and then use CRUD (create, read, update, delete) each record to personalise their DVD collections</p>.

<h3> Business Goals </h3>
- To allow a User to store the quantity of DVD's in their inventory for stock purposs.
- To store the price per DVD.
- To allow Users to review DVD's.


- Users can compile a collection of DVD's and then order them based on their preferences such as from highest rating to lowest.
- Users can also order their collection by the date they purchased the DVD.

- This app could be the basis for communities such as movie and books clubs, who wish to remember and store all their reviews and favourite DVD's.
![image](https://user-images.githubusercontent.com/97599832/228037084-5e519704-9511-4c7e-9821-b97b1432d9f9.png)



<h3>3. Features and Development Process</h3>

<h4> Wireframes and Concepts: </h4>

- Early on I want a DVD to be a self-contained object that could be looped over or iterated upon. It would contain all the information pertaining to each DVD and would then display on the dashboard in whatever ordered they are stored within the database.
![image](https://user-images.githubusercontent.com/97599832/228220314-76894dcd-2492-4336-82fc-69f4c75070e0.png)


- This app is built with Flask and Python, using templates.
- These templates render HTML that has in-built python scripts that call from the PostgreSQL Database.
- Users can input data straight into the forms and then manipulate the data around the domain of DVDs and Users.

![image](https://user-images.githubusercontent.com/97599832/228033308-b57220f2-1862-490d-aeef-518e8aaa47c2.png)

- If a user changes the inventory they can use the update button to change data on the DVD such as the quantity, they can also delete the DVD if it is no longer available.
- Similarly, they can add a review to the particular DVD by using the add review button.


<h3>4. Bugs and Testing</h3>

     -While testing my application I came across a major bug when trying to delete a DVD. Because I have a second table called DVD_REVIEW, it has a foreign key                  relationship with the primary key of DVD, the "DVD ID". So if you create a DVD and then add a DVD review and then try to delete the DVD, the application                 will return a 500 critical error, as seen below:         
    [image](https://user-images.githubusercontent.com/97599832/227781558-7f0e1e34-2468-4eaa-ba16-33ded95038fe.png)
    
    - From here we are taken to the submit DVD review form. We can then add a review which will create a record in the DVD review table with a dvd id.
    - Attempting to delete will then error.
    
    ![image](https://user-images.githubusercontent.com/97599832/227781676-a482c273-f966-4523-b5d0-855f36aafde7.png)
    
    - As you can see in the above URL, "/delete_dvd/9" we are passing in the dvd id - 9 to the delete dvd, however, we have no built in functionality to also delete the record from the child table of the parent DVD table.
    - The solution I decided upon came across during research, PostgreSQL has a feature called "cascading delete" which will delete the child records when the parent record is deleted if they have a foreign key relationship".
    
    - An example query would be "ALTER TABLE child_table ADD CONSTRAINT child_fk FOREIGN KEY (parent_id) REFERENCES parent_table(id) ON DELETE CASCADE;".

    Solution:
   ![image](https://user-images.githubusercontent.com/97599832/227782249-084ee5ce-761f-4f04-8174-d244941c3293.png)
   
   - I also changed my buttons to be wrapped in POST forms which prior the href tag was causing bugs.
   
   - I encountered another major bug when I tried to save images to my elephantSQL database. Whenever, the app would restart the dynos would restart which would cause the database instance to 
   
   - Unresponsive Navigation Bar Bug
   - I used the w3 Schools nav bar as my previous nav bar would go out of line and break at certain breakpoints.
   ![image](https://user-images.githubusercontent.com/97599832/231490168-f89a3909-c2a3-418e-8b91-7b49d5ee4f50.png)

    - Bug - Incorrect inputs for tables
    - If you enter letters for the "price" column in the form if will crash as the column is expecting integers.
    ![image](https://user-images.githubusercontent.com/97599832/231492321-e109fd41-6b72-4a8a-9d3b-2ab6436080cd.png)
    - To solve this error we need a validation check:
    
    - Add an error message.
    
    - Check using regex.
    ![image](https://user-images.githubusercontent.com/97599832/231492997-ac32c32a-462d-4c10-9be3-71b832811bce.png)


### Checking Code through Validators:
### CSS w3 Schools Jigsaw:

![image](https://user-images.githubusercontent.com/97599832/228552574-b6fe0e9c-2e27-44ad-8937-291d16f54fd4.png)

### HTML Validator
#### Page 1 - Index.html
![image](https://user-images.githubusercontent.com/97599832/230635519-99be8721-e205-452e-8dee-ac462373550b.png)

### Deployment
Deployment to Heroku Pages:

1. In terminal you need to copy the requirements.txt and create a Procfile for Heroko to build you app.
2. pip3 freeze --local > requirements.txt.
3. echo web: python app.py > Procfile.
4. Go to the Deploy tab and then Deployment Method and use GitHub.
5. Connect your GitHub repo you wish to clone and use for the App.
6. Set up env.py file: IP : 0.0.0.0, PORT : 5000, DATABASE_URI : DATABASE_URI", SECRET_KEY {your secret key}
7. Use Heroku/Python build package.
8. Connect your database instance such as elephantSQL and use the database URL.
9. You can read the logs by using "heroko logs --tail" in the project directory.

To Clone this Repository:
Terminal: $ git clone https://github.com/JackAlexanderClark/Ultimate-Movie-Vendor

### Credits 
1. Jack Clark
