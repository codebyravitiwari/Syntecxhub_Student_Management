# Student Management System

An industry-level CLI application for managing student records built with Python using Object-Oriented Programming (OOP) principles.

## Features

- **Add Student**: Create new student records with unique ID, name, and grade
- **View All Students**: Display all students in a formatted table
- **Update Student**: Modify existing student information
- **Delete Student**: Remove student records
- **Search Student**: Find students by ID or name (bonus feature)

## Project Structure

```
student_management/
├── __init__.py             # Package initialization
├── main.py                 # CLI interface (entry point)
├── models/
│   ├── __init__.py
│   └── student.py          # Student class
├── services/
│   ├── __init__.py
│   └── manager.py          # Business logic (StudentManager)
├── storage/
│   ├── __init__.py
│   └── data_handler.py      # JSON file handling
├── utils/
│   ├── __init__.py
│   └── validators.py       # Input validation
└── data/
    └── students.json      # Data storage file
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

No installation required. Simply navigate to the project directory.

## Usage

Run the application:

```bash
cd /path/to/student_management
python3 main.py
```

### Menu Options

1. **Add Student**: Enter student ID (unique), name, and grade (A/B/C/D/F)
2. **View All Students**: Display all students in table format
3. **Update Student**: Search by ID and update name/grade
4. **Delete Student**: Remove student by ID (type "yes" to confirm)
5. **Search Student**: Search by ID or name
6. **Exit**: Quit the application

## Validation Rules

- **Student ID**: Must be unique (no duplicates allowed)
- **Name**: Cannot be empty
- **Grade**: Must be one of: A, B, C, D, F

## Data Storage

All student data is persisted in JSON format at `data/students.json`. The file is automatically created when adding the first student.

## Example Data

The system comes with sample data:

```json
[
  {
    "student_id": "STU001",
    "name": "John Smith",
    "grade": "A"
  },
  {
    "student_id": "STU002",
    "name": "Jane Doe",
    "grade": "B"
  },
  {
    "student_id": "STU003",
    "name": "Bob Johnson",
    "grade": "C"
  }
]
```

## Architecture

- **Separation of Concerns**: Logic is separated into models, services, storage, and utils
- **OOP Design**: Uses classes (Student, StudentManager, DataHandler, CLI)
- **Error Handling**: try/except blocks for graceful error handling
- **Validation**: Input validation before processing
- **Persistence**: Automatic save/load from JSON file

## License

MIT License
