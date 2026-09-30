import streamlit as st
import sqlite3
from datetime import date


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart To-Do Manager",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DATABASE
# =========================================================

DATABASE = "todo.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority TEXT,
            due_date TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# =========================================================
# DATABASE FUNCTIONS
# =========================================================

def add_task(title, description, category, priority, due_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, description, category, priority, due_date, completed, created_at)
        VALUES (?, ?, ?, ?, ?, 0, datetime('now'))
    """, (
        title,
        description,
        category,
        priority,
        due_date
    ))

    conn.commit()
    conn.close()


def get_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            description,
            category,
            priority,
            due_date,
            completed,
            created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def update_task(
    task_id,
    title,
    description,
    category,
    priority,
    due_date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET
            title = ?,
            description = ?,
            category = ?,
            priority = ?,
            due_date = ?
        WHERE id = ?
    """, (
        title,
        description,
        category,
        priority,
        due_date,
        task_id
    ))

    conn.commit()
    conn.close()


def complete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


def uncomplete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed = 0
        WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


def delete_completed_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE completed = 1
    """)

    conn.commit()
    conn.close()


def delete_all_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")

    conn.commit()
    conn.close()


# =========================================================
# CREATE DATABASE
# =========================================================

create_database()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main page */
.stApp {
    background-color: #f5f7fa;
}


/* Main content */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}


/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white !important;
    background: #1f4e78;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 5px;
}


/* Subtitle */
.subtitle {
    text-align: center;
    color: #444444;
    font-size: 18px;
    margin-bottom: 30px;
}


/* Cards */
.card {
    background: rgba(255, 255, 255, 0.94);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.20);
}


/* Task card */
.task-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.18);
}


/* Task title */
.task-title {
    font-size: 22px;
    font-weight: bold;
    color: #222222;
}


/* Task text */
.task-text {
    color: #444444;
    font-size: 15px;
}


/* Statistics */
.stat-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}


.stat-number {
    font-size: 32px;
    font-weight: bold;
    color: #222222;
}


.stat-label {
    font-size: 14px;
    color: #555555;
}


/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1f2937;
}


/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}


/* Buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: bold;
}


/* Form */
[data-testid="stForm"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
}


/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">✅ Smart To-Do Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Plan • Organize • Complete • Track'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📚 Project Information")

    st.write("### Required Project Features")

    st.write("""
    ✅ Add tasks  
    ✅ View tasks  
    ✅ Edit tasks  
    ✅ Complete tasks  
    ✅ Delete tasks  
    ✅ Search tasks  
    ✅ Filter tasks  
    ✅ Priority management  
    ✅ Category management  
    ✅ Due dates  
    """)

    st.divider()

    st.write("### 🗄️ Database Design")

    st.write("""
    **Database:** SQLite

    **Table:** tasks

    **Fields:**
    - ID
    - Title
    - Description
    - Category
    - Priority
    - Due Date
    - Completed
    - Created At
    """)

    st.divider()

    st.write("### 🔗 Frontend + Backend")

    st.write("""
    **Frontend:** Streamlit UI

    **Backend:** Python

    **Database:** SQLite

    Streamlit sends user actions to
    Python functions, which update the
    SQLite database.
    """)

    st.divider()

    st.write("### 🧪 Testing")

    st.write("""
    Test cases:

    1. Add a task
    2. Add multiple tasks
    3. Edit a task
    4. Complete a task
    5. Uncomplete a task
    6. Delete a task
    7. Search a task
    8. Filter tasks
    9. Empty task validation
    """)

    st.divider()

    st.write("### 🚀 Deployment")

    st.write("""
    This application can be deployed
    using a Streamlit-compatible hosting
    service after preparing the required
    files and dependencies.
    """)


# =========================================================
# GET ALL TASKS
# =========================================================

tasks = get_tasks()


# =========================================================
# STATISTICS
# =========================================================

total_tasks = len(tasks)

completed_tasks = sum(
    1 for task in tasks if task[6] == 1
)

pending_tasks = total_tasks - completed_tasks

today = date.today().isoformat()

overdue_tasks = sum(
    1
    for task in tasks
    if task[5]
    and task[5] < today
    and task[6] == 0
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="stat-box">
            <div class="stat-number">{total_tasks}</div>
            <div class="stat-label">Total Tasks</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="stat-box">
            <div class="stat-number">{pending_tasks}</div>
            <div class="stat-label">Pending</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="stat-box">
            <div class="stat-number">{completed_tasks}</div>
            <div class="stat-label">Completed</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="stat-box">
            <div class="stat-number">{overdue_tasks}</div>
            <div class="stat-label">Overdue</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# ADD TASK
# =========================================================

st.header("➕ Add New Task")


with st.form("add_task_form"):

    col1, col2 = st.columns(2)

    with col1:

        title = st.text_input(
            "Task Title *",
            placeholder="Example: Complete Python assignment"
        )

        category = st.selectbox(
            "Category",
            [
                "Study",
                "College",
                "Personal",
                "Project",
                "Work",
                "Other"
            ]
        )

    with col2:

        priority = st.selectbox(
            "Priority",
            [
                "Low",
                "Medium",
                "High"
            ]
        )

        due_date = st.date_input(
            "Due Date",
            value=date.today()
        )

    description = st.text_area(
        "Description",
        placeholder="Enter task details..."
    )

    submitted = st.form_submit_button(
        "➕ Add Task"
    )


    if submitted:

        if title.strip() == "":

            st.error(
                "Please enter a task title."
            )

        else:

            add_task(
                title.strip(),
                description.strip(),
                category,
                priority,
                due_date.isoformat()
            )

            st.success(
                "Task added successfully!"
            )

            st.rerun()


# =========================================================
# SEARCH AND FILTER
# =========================================================

st.header("🔍 Search & Filter")


col1, col2, col3 = st.columns(3)


with col1:

    search_text = st.text_input(
        "Search",
        placeholder="Search task..."
    )


with col2:

    status_filter = st.selectbox(
        "Status",
        [
            "All",
            "Pending",
            "Completed"
        ]
    )


with col3:

    priority_filter = st.selectbox(
        "Priority",
        [
            "All",
            "Low",
            "Medium",
            "High"
        ]
    )


# =========================================================
# FILTER TASKS
# =========================================================

filtered_tasks = []


for task in tasks:

    task_id = task[0]
    title = task[1]
    description = task[2] or ""
    category = task[3]
    priority = task[4]
    due_date = task[5]
    completed = task[6]


    # Search filter
    if search_text:

        search_value = (
            title + " " +
            description + " " +
            category
        ).lower()

        if search_text.lower() not in search_value:
            continue


    # Status filter
    if status_filter == "Pending" and completed == 1:
        continue

    if status_filter == "Completed" and completed == 0:
        continue


    # Priority filter
    if priority_filter != "All":

        if priority != priority_filter:
            continue


    filtered_tasks.append(task)


# =========================================================
# TASK LIST
# =========================================================

st.header("📋 My Tasks")


if len(filtered_tasks) == 0:

    st.info(
        "No tasks found. Add a new task above."
    )

else:

    for task in filtered_tasks:

        task_id = task[0]
        task_title = task[1]
        task_description = task[2] or ""
        task_category = task[3]
        task_priority = task[4]
        task_due_date = task[5]
        task_completed = task[6]


        st.markdown(
            '<div class="task-card">',
            unsafe_allow_html=True
        )


        # Task title
        if task_completed == 1:

            st.markdown(
                f'<div class="task-title">✅ '
                f'<s>{task_title}</s></div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<div class="task-title">⏳ '
                f'{task_title}</div>',
                unsafe_allow_html=True
            )


        if task_description:

            st.write(
                task_description
            )


        # Task information
        info1, info2, info3, info4 = st.columns(4)


        with info1:

            st.write(
                f"📁 **Category:** {task_category}"
            )


        with info2:

            st.write(
                f"🔥 **Priority:** {task_priority}"
            )


        with info3:

            st.write(
                f"📅 **Due:** {task_due_date}"
            )


        with info4:

            if task_completed == 1:

                st.write(
                    "✅ **Completed**"
                )

            else:

                st.write(
                    "⏳ **Pending**"
                )


        # Buttons
        b1, b2, b3 = st.columns(3)


        with b1:

            if task_completed == 0:

                if st.button(
                    "✅ Complete",
                    key=f"complete_{task_id}"
                ):

                    complete_task(task_id)

                    st.rerun()

            else:

                if st.button(
                    "↩️ Undo",
                    key=f"undo_{task_id}"
                ):

                    uncomplete_task(task_id)

                    st.rerun()


        with b2:

            if st.button(
                "🗑️ Delete",
                key=f"delete_{task_id}"
            ):

                delete_task(task_id)

                st.success(
                    "Task deleted."
                )

                st.rerun()


        with b3:

            edit_key = f"edit_mode_{task_id}"

            if st.button(
                "✏️ Edit",
                key=f"edit_{task_id}"
            ):

                st.session_state[edit_key] = True


        # Edit section
        if st.session_state.get(
            f"edit_mode_{task_id}",
            False
        ):

            st.subheader(
                "✏️ Edit Task"
            )

            edit_title = st.text_input(
                "Title",
                value=task_title,
                key=f"edit_title_{task_id}"
            )


            edit_description = st.text_area(
                "Description",
                value=task_description,
                key=f"edit_description_{task_id}"
            )


            edit_category = st.selectbox(
                "Category",
                [
                    "Study",
                    "College",
                    "Personal",
                    "Project",
                    "Work",
                    "Other"
                ],
                index=[
                    "Study",
                    "College",
                    "Personal",
                    "Project",
                    "Work",
                    "Other"
                ].index(task_category),
                key=f"edit_category_{task_id}"
            )


            edit_priority = st.selectbox(
                "Priority",
                [
                    "Low",
                    "Medium",
                    "High"
                ],
                index=[
                    "Low",
                    "Medium",
                    "High"
                ].index(task_priority),
                key=f"edit_priority_{task_id}"
            )


            edit_date = st.date_input(
                "Due Date",
                value=date.fromisoformat(task_due_date),
                key=f"edit_date_{task_id}"
            )


            save_col, cancel_col = st.columns(2)


            with save_col:

                if st.button(
                    "💾 Save Changes",
                    key=f"save_{task_id}"
                ):

                    if edit_title.strip() == "":

                        st.error(
                            "Title cannot be empty."
                        )

                    else:

                        update_task(
                            task_id,
                            edit_title.strip(),
                            edit_description.strip(),
                            edit_category,
                            edit_priority,
                            edit_date.isoformat()
                        )

                        st.success(
                            "Task updated successfully!"
                        )

                        st.session_state[
                            f"edit_mode_{task_id}"
                        ] = False

                        st.rerun()


            with cancel_col:

                if st.button(
                    "❌ Cancel",
                    key=f"cancel_{task_id}"
                ):

                    st.session_state[
                        f"edit_mode_{task_id}"
                    ] = False

                    st.rerun()


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# MANAGEMENT
# =========================================================

st.divider()

st.header("⚙️ Task Management")


col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🧹 Clear Completed Tasks"
    ):

        delete_completed_tasks()

        st.success(
            "Completed tasks removed."
        )

        st.rerun()


with col2:

    if st.button(
        "⚠️ Delete All Tasks"
    ):

        delete_all_tasks()

        st.success(
            "All tasks deleted."
        )

        st.rerun()


# =========================================================
# PROJECT WORKFLOW
# =========================================================

st.divider()

st.header("📌 Project Development Workflow")


step1, step2, step3 = st.columns(3)


with step1:

    st.info("""
    **1. Identify Features**

    Add, view, edit, complete,
    delete, search, filter,
    priority and due dates.
    """)


with step2:

    st.info("""
    **2. Design Database**

    SQLite database stores
    all tasks permanently
    while the application runs.
    """)


with step3:

    st.info("""
    **3. Create Frontend**

    Streamlit provides forms,
    buttons, filters, cards
    and dashboard components.
    """)


step4, step5, step6 = st.columns(3)


with step4:

    st.info("""
    **4. Connect Frontend & Backend**

    Streamlit UI calls Python
    database functions to
    perform CRUD operations.
    """)


with step5:

    st.info("""
    **5. Test Application**

    Test adding, editing,
    completing, deleting,
    searching and filtering.
    """)


with step6:

    st.info("""
    **6. Prepare Deployment**

    Keep app.py and requirements.txt
    ready for deployment to a
    Streamlit-compatible platform.
    """)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;color:#444444;">
        <b>Smart To-Do Manager</b><br>
        Built with Python + Streamlit + SQLite
    </div>
    """,
    unsafe_allow_html=True
)