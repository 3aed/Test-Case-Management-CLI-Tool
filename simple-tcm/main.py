# main.py

"""Main entry point for the Simple TCM CLI application m."""
"""" made by Aaed Hany FarajAllah """

import sys
from src import cli
from src import database

def main():
    """Parses arguments and executes the corresponding command."""
    # Ensure database is initialized before running commands that need it
    # This check could be more sophisticated, e.g., checking file existence
    # but initialize_database() is idempotent (uses CREATE TABLE IF NOT EXISTS)
    # We added --init-db flag, so maybe only call it explicitly?
    # Let's rely on the --init-db flag for explicit initialization.
    # database.initialize_database() # Removed automatic initialization

    parser = cli.setup_parser()
    args = parser.parse_args()

    # Check if the database file exists if a command other than init-db is run
    if not args.init_db and args.command:
        try:
            # Attempt a simple connection to check if DB exists and is accessible
            conn = database.get_db_connection()
            # Check if the table exists, if not, prompt user to init
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'test_cases\';")
            if cursor.fetchone() is None:
                print("Error: Database table not found. Please run with --init-db first.")
                conn.close()
                sys.exit(1)
            conn.close()
        except Exception as e:
            print(f"Error accessing database: {e}")
            print("Please ensure the database is initialized using --init-db")
            sys.exit(1)

    cli.handle_command(args)

if __name__ == "__main__":
    main()

