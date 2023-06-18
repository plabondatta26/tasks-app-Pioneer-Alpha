# Task Management App

A simple task management application that allows users to create, update, and delete tasks organized within directories.

## Image:

[//]: # (<img src="https://prnt.sc/bDLZTlVWfbiG" alt="home page">)
![home page](https://prnt.sc/bDLZTlVWfbiG)
## Features

- **Create:** Create new tasks with a title, description, directory, importance, completion status and target completion date.
- **Update:** Update existing tasks by modifying their title, description, directory, importance, completion status and target completion date.
- **Delete:** Delete tasks that are no longer needed.
- **List:** View a list of all tasks and their details.
- **Mark Complete:** Mark tasks as completed to track progress.
- **Mark Important:** Flag tasks as important for prioritization.
- **Filtering:** Filter tasks based on specific criteria, such as directory or completion status.

## Getting Started

To run the application on your local machine, follow these steps:

1. Clone the repository: <br>
`git clone https://github.com/plabondatta26/tasks-app-Pioneer-Alpha.git`

2. Install dependencies:

- Frontend:
  ```
  cd task-management-app/frontend
  npm install
  ```

- Backend: create virtual environment
  ```
  cd task-management-app/backend
  pip install -r requirements.txt
  ```

3. Start the application:

- Frontend:
  ```
  cd task-management-app/frontend
  npm start
  ```

  The frontend application will be accessible at http://localhost:3000.

- Backend:
  ```
  cd task-management-app/backend
  python manage.py runserver localhost:8000
  ```

  The backend server will be accessible at http://localhost:8000.
- Swagger Link: http://localhost:8000/swagger/
- Swagger doc: http://localhost:8000/redoc/

4. Open your web browser and visit http://localhost:3000 to access the application.

## Technologies Used

- Frontend: React, JavaScript, HTML, CSS
- Backend: Django, Python
- Database: SQLite (sqlite used to avoid database dependency )

## File structure
![File structure](https://prnt.sc/5Qhs-8Yb-s34)