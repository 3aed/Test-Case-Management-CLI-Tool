# src/database.py

"""Handles database interactions (SQLite)."""

import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DATABASE_PATH = os.path.join(DATABASE_DIR, 'tcm_database.db')

def ensure_db_dir_exists():
    """Ensures the directory for the database file exists."""
    os.makedirs(DATABASE_DIR, exist_ok=True)

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    ensure_db_dir_exists()
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row # Return rows as dictionary-like objects
    return conn

def initialize_database():
    """Initializes the database by creating the test_cases table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT DEFAULT 'Medium' CHECK(priority IN ('High', 'Medium', 'Low')),
        status TEXT DEFAULT 'Not Tested' CHECK(status IN ('Not Tested', 'Passed', 'Failed', 'Blocked')),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes TEXT
    )
    """)
    # Add a trigger to update updated_at timestamp automatically
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS update_test_case_updated_at
    AFTER UPDATE ON test_cases
    FOR EACH ROW
    BEGIN
        UPDATE test_cases SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
    END;
    """)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DATABASE_PATH}")

# --- CRUD Operations --- 

# Functions for add, list, update, delete, view will be added here.

if __name__ == '__main__':
    # Initialize DB when script is run directly (for setup)
    initialize_database()



def add_test_case(title: str, description: str | None = None, priority: str = 'Medium'):
    """Adds a new test case to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO test_cases (title, description, priority)
        VALUES (?, ?, ?)
        """, (title, description, priority))
        conn.commit()
        print(f"Successfully added test case: '{title}'")
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()



def list_test_cases(status_filter: str | None = None, priority_filter: str | None = None):
    """Lists test cases from the database, optionally filtering by status or priority."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT id, title, status, priority, strftime('%Y-%m-%d %H:%M', created_at) as created, strftime('%Y-%m-%d %H:%M', updated_at) as updated FROM test_cases"
    filters = []
    params = []

    if status_filter:
        filters.append("status = ?")
        params.append(status_filter)
    if priority_filter:
        filters.append("priority = ?")
        params.append(priority_filter)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY id"

    try:
        cursor.execute(query, params)
        test_cases = cursor.fetchall()
        return test_cases
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()



def update_test_case(case_id: int, title: str | None = None, description: str | None = None, priority: str | None = None, status: str | None = None, notes: str | None = None):
    """Updates an existing test case in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    fields_to_update = []
    params = []

    if title is not None:
        fields_to_update.append("title = ?")
        params.append(title)
    if description is not None:
        fields_to_update.append("description = ?")
        params.append(description)
    if priority is not None:
        fields_to_update.append("priority = ?")
        params.append(priority)
    if status is not None:
        fields_to_update.append("status = ?")
        params.append(status)
    if notes is not None:
        fields_to_update.append("notes = ?")
        params.append(notes)

    if not fields_to_update:
        print("No fields provided for update.")
        conn.close()
        return False

    # Add the case_id to the parameters list for the WHERE clause
    params.append(case_id)

    query = f"UPDATE test_cases SET {', '.join(fields_to_update)} WHERE id = ?"

    try:
        cursor.execute(query, params)
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Error: Test case with ID {case_id} not found.")
            return False
        else:
            print(f"Successfully updated test case ID: {case_id}")
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()



def delete_test_case(case_id: int):
    """Deletes a test case from the database by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM test_cases WHERE id = ?", (case_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Error: Test case with ID {case_id} not found.")
            return False
        else:
            print(f"Successfully deleted test case ID: {case_id}")
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_test_case_by_id(case_id: int):
    """Retrieves a single test case by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT *, strftime('%Y-%m-%d %H:%M', created_at) as created, strftime('%Y-%m-%d %H:%M', updated_at) as updated FROM test_cases WHERE id = ?", (case_id,))
        test_case = cursor.fetchone()
        if test_case is None:
            print(f"Error: Test case with ID {case_id} not found.")
            return None
        return test_case
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

