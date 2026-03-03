from app.database import get_connection
from app.models import TaskCreate, TaskUpdate
from fastapi import HTTPException
from datetime import datetime


def row_to_dict(row, cursor) -> dict:
    """Convert a database row (tuple) into a dictionary using column names."""
    columns = [desc[0] for desc in cursor.description]
    return dict(zip(columns, row))


# ---------- CREATE ----------

def create_task(data: TaskCreate) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, status, due_date)
        VALUES (%s, %s, %s, %s)
        RETURNING *;
        """,
        (data.title, data.description, data.status, data.due_date)
    )

    task = row_to_dict(cursor.fetchone(), cursor)
    conn.commit()
    cursor.close()
    conn.close()
    return task


# ---------- READ ALL ----------

def get_all_tasks(status: str = None) -> list:
    conn = get_connection()
    cursor = conn.cursor()

    if status:
        cursor.execute("SELECT * FROM tasks WHERE status = %s ORDER BY created_at DESC;", (status,))
    else:
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC;")

    rows = cursor.fetchall()
    tasks = [row_to_dict(row, cursor) for row in rows]
    cursor.close()
    conn.close()
    return tasks


# ---------- READ ONE ----------

def get_task_by_id(task_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = %s;", (task_id,))
    row = cursor.fetchone()

    if not row:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found.")

    task = row_to_dict(row, cursor)
    cursor.close()
    conn.close()
    return task


# ---------- UPDATE ----------

def update_task(task_id: int, data: TaskUpdate) -> dict:
    # Get existing task first (raises 404 if not found)
    existing = get_task_by_id(task_id)

    # Only update fields that were actually provided
    new_title       = data.title       if data.title is not None       else existing["title"]
    new_description = data.description if data.description is not None else existing["description"]
    new_status      = data.status      if data.status is not None      else existing["status"]
    new_due_date    = data.due_date    if data.due_date is not None    else existing["due_date"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = %s,
            description = %s,
            status = %s,
            due_date = %s,
            updated_at = %s
        WHERE id = %s
        RETURNING *;
        """,
        (new_title, new_description, new_status, new_due_date, datetime.utcnow(), task_id)
    )

    task = row_to_dict(cursor.fetchone(), cursor)
    conn.commit()
    cursor.close()
    conn.close()
    return task


# ---------- DELETE ----------

def delete_task(task_id: int) -> dict:
    # Verify task exists first
    get_task_by_id(task_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": f"Task {task_id} deleted successfully."}
