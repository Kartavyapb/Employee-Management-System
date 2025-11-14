# Employee-Management-System
A fully functional web-based Employee Management System built with Django, featuring Add, View, Update, Delete, and Search functionalities. Includes audio feedback, pagination, and a modern animated UI using Bootstrap and Animate.css.

The Employee Management System is a Django based web application designed to simplify the management of employee records within an organization.
It allows administrators to add, view, update, delete and search employee details efficiently through an intuitive and visually applealing interface.
## Features
* Add Employee :-      Easily add a neew employee with details like name, gender, contact info, salary, designation and photo.
* List View :-         Displays all employees in a paginated and searchable table.
* Employee :-          View all details about an employee, including their uploaded profile photo.
* Update Employee Details :-   Update Employee details directly from the details page.
* Delete Employee Details :-   Delete Employee with a confirmation alert and sound effect.
* Sound Effects :-             Interactive audio feedback when saving or deleting records.
* Search Functionality :-      Quickly find employees and their details by name.
* Pagination :-                Neatly organized employee listing for better user experience.
* Attractive UI :-             Beautiful and responsive pages built with Bootstrap, CSS animations and static image backgrounds.

## Technologies Used
##### <pre> Technology                          Description </pre>
<pre> Python:-                    Backend Logic and Data handling. </pre>
<pre> Django:-                    Web Framework used for routing, views and models. </pre>
<pre> HTML5 / CSS3 / Bootstrap:-  Frontend design and responsive UI. </pre>
<pre> SQLite3:-                   Default Django database used for data storage. </pre>
<pre> JavaScript:-                Audio control and dynamic interactions. </pre>
<pre> Static Files:-              Images and audio effects (Save/Update/Delete sounds). </pre>

## Project Structure
employee_management/ <br>
│ <br>
├── employeeapp/ <br>
│   ├── templates/ <br>
│   │   ├── employeeapp/ <br>
│   │   │   ├── home.html <br>
│   │   │   ├── add.html <br>
│   │   │   ├── list.html <br>
│   │   │   ├── details.html <br>
│   │   │   ├── update.html <br>
│   │   │   └── delete.html <br>
│   ├── models.py <br>
│   ├── views.py <br>
│   ├── urls.py <br>
│ <br>
├── static/ <br>
│   ├── images/ <br>
│   │   ├── employee-network.jpg <br>
│   │   ├── emp_mngmnt.jpg <br>
│   ├── sounds/ <br>
│   │   ├── Save audio.mp3 <br>
│   │   ├── Delete_audio.mp3 <br>
│ <br>
├── db.sqlite3 <br>
├── manage.py <br>

## Home Page <br>
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/b2e744e0-fa4e-4c09-a6bc-09cdaece3fe8" /> <br>

## Add Employee Page <br>
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/1a1d2039-9b50-4396-9427-0fb3880e96c9" /> <br>

## Employees List Page <br>
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/a1088307-3323-43e6-b15e-a5ab39797c31" /> <br>

## Employee Details Page <br>
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/1503cf04-040b-4fdb-b0ee-9213986409b2" /> <br>

## Future Enhancements
* Add Authentication System (Admin Login)
* Generate Employee Reports
* Export Employee data as PDF or CSV
* Build responsive mobile view

## Author <br>
### Kartavya Badge <br>
📧 Email: kartavyabadge2011@gmail.com <br>
🔗 LinkedIn – www.linkedin.com/in/kartavya-badge-b1541b243

## Conclusion
This Project demonstrate how Django can be used to build a fully functional CRUD web application with elegant UI design and smooth interactivity.
It's a great project for beginners exploring Full-Stack development using Python and Django.
