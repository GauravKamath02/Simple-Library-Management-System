# Library Management System

## Introduction

The Library Management System is a web application built using Flask, a Python web framework. It is designed to assist in the management of books and users in a library setting. This project serves as a submission for the cloud computing assignment in the 7th semester of engineering.

## Features

- **Book Management**: Add and remove books from the library's collection.
- **User Management**: Add new members to the library.
- **User Interface**: A user-friendly web interface for interacting with the system.
- **Custom Jinja2 Filter**: Utilizes a custom Jinja2 filter to emulate the behavior of Python's `enumerate` function in templates.
- **Responsive Design**: The application's UI is designed to work seamlessly on different screen sizes.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/GauravKamath02/Simple-Library-Management-System.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Simple-Library-Management-System
    ```

3. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Start the Flask development server:

    ```bash
    python app.py
    ```

7. Access the application in your web browser at `http://localhost:5000`.


## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.


---

*Note: This project is a submission for the cloud computing assignment in the 7th semester of engineering.*
