# Simple Test Case Management (TCM) CLI Tool
A lightweight, command-line interface (CLI) tool for managing test cases, built with Python and SQLite. Perfect for QA engineers, developers, or small teams needing a simple, local solution to track testing efforts directly from the terminal.

## Table of Contents
- [🚀 Overview](#-overview)
- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [🔧 Usage](#-usage)
- [📂 Project Structure](#-project-structure)
- [🛠 Future Enhancements](#-future-enhancements)


## 🚀 Overview

In fast-paced software development, organized test case management is essential. While robust platforms exist, smaller projects or individual testers often need a straightforward, no-fuss tool. The Simple TCM CLI fills this gap, offering:

- **Portable** solution with SQLite backend
- **Zero configuration** setup
- **Terminal-friendly** interface
- **Local data storage** (`data/tcm_database.db`)

## ✨ Features

### Core Functionality
- **Database Initialization**: 
  - Automatic setup on first run
  - Manual initialization via `--init-db` flag
  - SQLite database stored in `data/tcm_database.db`

### Test Case Management
| Feature | Command | Description |
|---------|---------|-------------|
| **Add** | `add` | Create test cases with title, description, and priority |
| **List** | `list` | View summary table with filtering options |
| **View** | `view` | Display detailed test case information |
| **Update** | `update` | Modify existing test cases |
| **Delete** | `delete` | Remove test cases by ID |

### Advanced Options
- Priority levels: `High`, `Medium`, `Low`
- Status tracking: `Not Tested`, `Passed`, `Failed`, `Blocked`
- Automatic timestamps for creation and updates

## 📦 Installation

### Prerequisites
- Python 3.6+
- pip package manager

### Setup Instructions
```bash
# Clone the repository
git clone https://github.com/3aed/simple-tcm.git
cd simple-tcm

# Install dependencies
pip install -r requirements.txt

# Initialize database
python main.py --init-db
