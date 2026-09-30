# Smart To-Do Manager

A simple and user-friendly **To-Do List web application** built using **Python, Streamlit, and SQLite**.
It helps users create, manage, update, search, and track their daily tasks.

## Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* Undo completed tasks
* Search tasks
* Filter tasks by status
* Filter tasks by priority
* Organize tasks using categories
* Add due dates
* View task statistics
* Clear completed tasks
* Delete all tasks
* Store task data using SQLite database

## Technologies Used

* **Python**
* **Streamlit**
* **SQLite**
* **HTML/CSS**

## Database

The application uses an SQLite database named `todo.db`.

### Tasks Table

| Field       | Data Type | Description                 |
| ----------- | --------- | --------------------------- |
| id          | INTEGER   | Unique task ID              |
| title       | TEXT      | Task title                  |
| description | TEXT      | Task description            |
| category    | TEXT      | Task category               |
| priority    | TEXT      | Task priority               |
| due_date    | TEXT      | Task due date               |
| completed   | INTEGER   | Completion status           |
| created_at  | TEXT      | Task creation date and time |

## Project Structure

```text
Smart-ToDo-Manager/
│
├── app.py
├── requirements.txt
└── README.md
```

> `todo.db` is created automatically when the application runs.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-ToDo-Manager.git
```

### 2. Open the project folder

```bash
cd Smart-ToDo-Manager
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

## Run the Application

Run the following command:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

You can also open:

```text
http://localhost:8501
```

## Project Workflow

```text
Identify Requirements
        ↓
Design Database
        ↓
Create Frontend
        ↓
Connect Frontend & Backend
        ↓
Test Application
        ↓
Fix Errors
        ↓
Prepare for Deployment
```

## CRUD Operations

The application supports the main CRUD operations:

* **Create** – Add new tasks
* **Read** – View tasks
* **Update** – Edit and update tasks
* **Delete** – Delete tasks

## Requirements

The project requires:

```text
Python
Streamlit
SQLite
```

Install Streamlit using:

```bash
pip install streamlit
```

## Future Improvements

* User login and authentication
* Task reminders
* Email notifications
* Dark mode
* Cloud database
* Mobile-friendly interface
* Online deployment

## Author

**Maha Lakshmi**

B.Tech – Computer Science and Engineering

## License

This project is created for **educational and learning purposes**.
