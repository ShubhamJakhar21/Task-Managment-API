import psycopg2 # type: ignore
import os

# Read database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/taskdb")

def get_connection():
    """Open and return a new database connection."""
    return psycopg2.connect(DATABASE_URL)

def create_tables():
    """Create the tasks table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id          SERIAL PRIMARY KEY,
            title       VARCHAR(255) NOT NULL,
            description TEXT,
            status      VARCHAR(50)  NOT NULL DEFAULT 'pending',
            due_date    TIMESTAMP,
            created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
            updated_at  TIMESTAMP NOT NULL DEFAULT NOW()
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Tables ready.")
