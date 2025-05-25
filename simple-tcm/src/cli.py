# src/cli.py

"""Handles Command Line Interface logic using argparse."""

import argparse
from . import database
from tabulate import tabulate # For nice table formatting

def setup_parser():
    """Sets up the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Simple Test Case Management Tool (TCM)")
    parser.add_argument("--init-db", action="store_true", help="Initialize the database (create table if not exists)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: add
    parser_add = subparsers.add_parser("add", help="Add a new test case")
    parser_add.add_argument("-t", "--title", required=True, help="Test case title")
    parser_add.add_argument("-d", "--description", help="Test case description")
    parser_add.add_argument("-p", "--priority", choices=["High", "Medium", "Low"], default="Medium", help="Test case priority")

    # Command: list
    parser_list = subparsers.add_parser("list", help="List test cases")
    parser_list.add_argument("--status", choices=["Not Tested", "Passed", "Failed", "Blocked"], help="Filter by status")
    parser_list.add_argument("--priority", choices=["High", "Medium", "Low"], help="Filter by priority")
    # parser_list.add_argument("--all", action="store_true", help="Show all details") # Maybe implement later

    # Command: update
    parser_update = subparsers.add_parser("update", help="Update an existing test case")
    parser_update.add_argument("id", type=int, help="ID of the test case to update")
    parser_update.add_argument("-t", "--title", help="New test case title")
    parser_update.add_argument("-d", "--description", help="New test case description")
    parser_update.add_argument("-p", "--priority", choices=["High", "Medium", "Low"], help="New test case priority")
    parser_update.add_argument("-s", "--status", choices=["Not Tested", "Passed", "Failed", "Blocked"], help="New test case status")
    parser_update.add_argument("-n", "--notes", help="Add or update execution notes")

    # Command: delete
    parser_delete = subparsers.add_parser("delete", help="Delete a test case")
    parser_delete.add_argument("id", type=int, help="ID of the test case to delete")

    # Command: view
    parser_view = subparsers.add_parser("view", help="View details of a specific test case")
    parser_view.add_argument("id", type=int, help="ID of the test case to view")

    return parser

def handle_command(args):
    """Handles the parsed command and arguments."""
    if args.init_db:
        database.initialize_database()
        return # Stop further processing if only initializing DB

    if args.command == "add":
        database.add_test_case(args.title, args.description, args.priority)
    elif args.command == "list":
        test_cases = database.list_test_cases(args.status, args.priority)
        if test_cases:
            headers = ["ID", "Title", "Status", "Priority", "Created", "Updated"]
            # Convert Row objects to lists for tabulate
            data = [[tc["id"], tc["title"], tc["status"], tc["priority"], tc["created"], tc["updated"]] for tc in test_cases]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No test cases found matching the criteria.")
    elif args.command == "update":
        database.update_test_case(args.id, args.title, args.description, args.priority, args.status, args.notes)
    elif args.command == "delete":
        # Maybe add a confirmation prompt here in a future version
        database.delete_test_case(args.id)
    elif args.command == "view":
        test_case = database.get_test_case_by_id(args.id)
        if test_case:
            # Print details in a more readable format
            print(f"--- Test Case Details (ID: {test_case["id"]}) ---")
            print(f"Title:       {test_case["title"]}")
            print(f"Description: {test_case["description"] or "N/A"}")
            print(f"Priority:    {test_case["priority"]}")
            print(f"Status:      {test_case["status"]}")
            print(f"Created At:  {test_case["created"]}")
            print(f"Updated At:  {test_case["updated"]}")
            print(f"Notes:       {test_case["notes"] or "N/A"}")
            print("----------------------------------------")
        # Error message is handled within get_test_case_by_id
    elif args.command is None and not args.init_db:
        # No command was provided, print help
        parser = setup_parser()
        parser.print_help()

