Simple Test Case Management (TCM) CLI Tool

A lightweight, command-line interface (CLI) tool for managing test cases, built with Python and SQLite. Perfect for QA engineers, developers, or small teams needing a simple, local solution to track testing efforts directly from the terminal.
🚀 Overview
In fast-paced software development, organized test case management is essential. While robust platforms exist, smaller projects or individual testers often need a straightforward, no-fuss tool. The Simple TCM CLI fills this gap, offering a portable, database-driven solution to create, view, update, and delete test cases—all stored locally in a single SQLite database (data/tcm_database.db).
✨ Features

Database Initialization: Automatically sets up an SQLite database and table structure on first run or via --init-db.
Add Test Cases: Create test cases with a title, optional description, and priority (High, Medium, Low).
List Test Cases: View a tabular summary of test cases, filterable by status (Not Tested, Passed, Failed, Blocked) or priority.
View Details: Display detailed information for a test case by its unique ID, including title, description, priority, status, timestamps, and execution notes.
Update Test Cases: Modify title, description, priority, status, or execution notes for existing test cases.
Delete Test Cases: Permanently remove test cases by ID.

🛠️ Installation
Get started in just a few steps. You'll need Python 3.6+ installed.

Clone the Repository:
git clone https://github.com/<your-username>/simple-tcm.git
cd simple-tcm


Install Dependencies:The tool uses the tabulate library for formatted output. Install it with:
pip install tabulate
# Or use the requirements file:
pip install -r requirements.txt


Initialize the Database:Run the following to create the data/tcm_database.db file and set up the table structure:
python main.py --init-db



📖 Usage
Run the tool using:
python main.py [command] [options]

If no command is provided, a help message lists available commands and options.
Commands

addAdd a new test case.Options:  

--title, -t (required): Test case title.  
--description, -d (optional): Test case description.  
--priority, -p (optional): Priority (High, Medium, Low; default: Medium).Example:

python main.py add -t "Verify login functionality" -d "Test login with valid/invalid credentials" -p High


listList test cases, optionally filtered by status or priority.Options:  

--status: Filter by Not Tested, Passed, Failed, or Blocked.  
--priority: Filter by High, Medium, or Low.Examples:

python main.py list
python main.py list --status Failed --priority High


viewView details of a test case by ID.Arguments:  

id (required): Test case ID.Example:

python main.py view 5


updateUpdate an existing test case.Arguments:  

id (required): Test case ID.Options:  
--title, -t: New title.  
--description, -d: New description.  
--priority, -p: New priority (High, Medium, Low).  
--status, -s: New status (Not Tested, Passed, Failed, Blocked).  
--notes, -n: Add or update execution notes.Example:

python main.py update 12 -s Passed -n "Tested on Chrome v105. Passed."


deleteDelete a test case by ID.Arguments:  

id (required): Test case ID.Example:

python main.py delete 8


--init-dbInitialize the SQLite database (run once during setup).Example:
python main.py --init-db



📂 Project Structure
/simple-tcm
├── data/
│   └── tcm_database.db   # SQLite database (created automatically)
├── src/
│   ├── __init__.py
│   ├── cli.py            # CLI argument parsing and command dispatching
│   ├── database.py       # SQLite database interactions (CRUD)
│   └── models.py         # Database schema documentation
├── main.py               # Main application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

🔮 Future Enhancements

Keyword-based search for test cases.
Tagging or grouping test cases.
Confirmation prompts for destructive actions (e.g., deletion).
Export/import test cases (e.g., CSV format).
Detailed reporting and statistics.
Packaging for PyPI distribution.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m "Add YourFeature").
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

Please follow the Contributor Covenant Code of Conduct.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙏 Acknowledgments
Built with ❤️ for QA engineers and developers looking for a simple, effective test case management solution.
