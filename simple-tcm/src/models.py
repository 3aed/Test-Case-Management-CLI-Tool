# src/models.py

"""Defines the data model (database schema) for test cases."""

# Database Schema (SQLite)
# Table: test_cases
# Columns:
#   id INTEGER PRIMARY KEY AUTOINCREMENT
#   title TEXT NOT NULL
#   description TEXT
#   priority TEXT DEFAULT 'Medium' CHECK(priority IN ('High', 'Medium', 'Low'))
#   status TEXT DEFAULT 'Not Tested' CHECK(status IN ('Not Tested', 'Passed', 'Failed', 'Blocked'))
#   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#   updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#   notes TEXT

# We might define a class here later if using an ORM or for structure,
# but for now, the schema definition as comments is sufficient for design.

