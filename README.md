

# To-Do List Application

## Description
A web application for creating and managing a personal to-do list. This application has both frontend and backend components, uses a database for data persistence, and exposes APIs for interacting with the data.

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
<pre><code>python manage.py migrate</code></pre>
- And To create a super user:
<pre><code>python manage.py migrate</code></pre>
- And start up the server:
<pre><code>python manage.py runserver</code></pre>
Navigate to http://localhost:8000 in your web browser:
<br>

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

### Additional Notes :
<li>We need two Terminals one for Backend and another for frontend </li>
<li>We first run the backend server and then the Frontend server</li>
