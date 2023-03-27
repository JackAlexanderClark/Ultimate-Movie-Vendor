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
</ul>
<img src="static/images/ERD diagram of tables.jpg">

<h3> Business Goals </h3>
- To allow a User to store the quantity of DVD's in their inventory for stock purposs.
- To store the price per DVD.
- To allow Users to review DVD's.


- Users can compile a collection of DVD's and then order them based on their preferences such as from highest rating to lowest.
- Users can also order their collection by the date they purchased the DVD.

- This app could be the basis for communities such as movie and books clubs, who wish to remember and store all their reviews and favourite DVD's.
![image](https://user-images.githubusercontent.com/97599832/228037084-5e519704-9511-4c7e-9821-b97b1432d9f9.png)



<h3>3. Features and Development Process</h3>

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
