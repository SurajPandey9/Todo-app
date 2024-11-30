
# FOR ANY QUERY VISIT MY ANOTHER GITHUB PROFILE @surcs18
# To-Do List Application

## Description
A web application for creating and managing a personal to-do list. This application has both frontend and backend components, uses a database for data persistence, and exposes APIs for interacting with the data.
## PREREQUISITES
you must have:

Set up a local programming environment for python3

Set up Node.js on your Local Development Environment.

## Technologies
- **Frontend:** React
- **Backend:** Django, Django REST framework
- **Database:** SQLite (default with Django)
- **API:** RESTful APIs for CRUD operations on tasks in the to-do list

## Features
1. Users can create new tasks with a title and optional description.
2. Users can mark tasks as completed or uncompleted.
3. Users can edit the title and description of tasks.
4. Users can delete tasks.
5. The application persists data even after refreshing the page.
6. (Optional) User authentication (basic authentication or social login).

## Setup Instructions

#### Setting Up the Backend
- Open a new terminal window and run the following command to create a new project directory:
<pre><code>mkdir Todo-app</code></pre>
- Next, navigate into the directory:
<pre><code>cd Todo-app</code></pre>
- Now install Pipenv using pip:
<pre><code>pip install pipenv</code></pre>
- And activate a new virtual environment:
<pre><code>pipenv shell</code></pre>
- Install Django using Pipenv:
<pre><code>pipenv install django</code></pre>
- Then create a new project called backend:
<pre><code>django-admin startproject backend</code></pre>
- Next, navigate into the newly created backend directory:
<pre><code>cd backend</code></pre>
- Start a new application called todo:
<pre><code>python manage.py startapp todo</code></pre>
- Run migrations:
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
- The next step is to create a "superuser" account to access the admin interface. Run the command in the terminal::
<pre><code>python manage.py createsuperuser</code></pre>
This command sends a prompt that requests for 'username', 'email address', and 'password'.Enter a username and password you will remember because you will use it to log into the admin dashboard interface
- And start up the server:
<pre><code>python manage.py runserver</code></pre>
Navigate to the link http://localhost:8000/admin in your browser to access the admin interface and log in with the username and password you created earlier.
Navigate to http://localhost:8000 in your web browser:
<br>
It is now possible to CRUD the Todo items from this dashboard.

You can now add items to the admin dashboard.
### SETTING UP APIs

In this part, Django REST framework will be used to create the API(Application Programming Interface).
While still in the virtual environment, install the djangorestframework and django cross origin resource sharing headers with the commands:
<pre><code>pipenv install djangorestframework django-cors-headers</code></pre>



#### Setting Up the Frontend
- To set up the frontend, this tutorial will rely upon Create React App. 
There are several approaches to using create-react-app. 
One approach is to use npx to run the package and create the project:
<pre><code>npx create-react-app frontend</code></pre>
- After the project is created, you can change into the newly created frontend directory:
 <pre><code>cd frontend</code></pre>
- Then, start the application:
 <pre><code>npm start</code></pre>
 - Next, install bootstrap and reactstrap to provide user interface tools.
  <pre><code>npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps</code></pre>
- Finally install:
<pre><code>npm install axios@0.21.1</code></pre>

### Additional Most Important Notes :
<li>We need two Terminals one for Backend and another for frontend </li>
<li>We first run the backend server and it must necessary to run always before frontend server  and then run the Frontend server</li>
<li>we run two server at same time http://localhost:8000/admin for backend and http://localhost:3000 for frontent and our data store on http://localhost:8000/admin</li>
<li>for admin login you must have username and password which enter during after createsuperuser command </li>

