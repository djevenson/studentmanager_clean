# Student Manager

This is a simple student management system implemented in Python.

## Features
- add students with their details
- show all students
- search for students by name
- search for students by ID


## Structure of the project
```
studentmanager_clean/
├── READme.md
├── main.py
├── requirements.txt
├── src/
│   ├── entities/
│   │   └── student_entitie.py
│   ├── framework/
│   │   ├── cli_app.py
│   │   └── web_app.py
│   ├── interface_adapter/
│   │   ├── controller/
│   │   │   └── controller.py
│   │   ├── presenters/
│   │   │   └── presenter.py
│   │   └── repositories/
│   │       ├── memory_repo.py
│   │       └── sql_repo.py
│   └── use_case/
│       ├── add_student.py
│       ├── delete_student.py
│       ├── interface/
│       │   └── interface.py
│       ├── search_student.py
│       └── show_student.py
└── test/
    └── pytest.py
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/djevenson/studentmanager_clean
    ```

2. Navigate to the project directory:
   ```bash
   cd studentmanager_clean
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Data Structure
### entities
- Student (ID, firstname, lastname, faculty, grade, gpa)

### use_case
- add_student (add a student to the repository)
- delete_student (delete a student from the repository)
- search_student (search for a student by name or ID)
- show_student (display information about a all students or a specific student)

### interface_adapter
- controller (handle user input and call the appropriate use case)
- presenters (format the output for display)
- repositories (store and retrieve student data)

### framework
- cli_app (command line interface for the application)
- web_app (web interface for the application)

### Testing
- pytest (test the application using pytest)

### main.py
- entry point for the application, runs the CLI or web interface based on user input

### requirements.txt
- list of required dependencies for the application
* pytest
* uvicorn
* fastapi
* psycopg2
* pydantic
* python-dotenv

## Usage
1. Run the application:
   ```bash
   python main.py
    ```
2. Follow the prompts to add, delete, search, or show students.
3. To run the tests, use pytest:
   ```bash
   pytest test/pytest.py
   ```
3. To run the web application, use uvicorn:
   ```bash
   uvicorn src.framework.web_app:app --reload
   ```
4. Open your web browser and go to http://localhost:8000






