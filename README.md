# Library Management System API

## Overview

The Library Management System API is a RESTful API built using Django and Django REST Framework. This API allows users to manage library resources, including the ability to borrow, return, and view books. It supports user management and tracks transactions, providing a complete solution for library management.

## Features

- **Books Management**: Create, Read, Update, and Delete (CRUD) operations for books.
- **Users Management**: CRUD operations for library users.
- **Check-Out and Return Books**: Users can check out and return books while ensuring that only available copies can be borrowed.
- **View Available Books**: Endpoint to view all books with optional filters for title, author, or ISBN.
- **User Authentication**: Basic authentication to secure user data and transactions.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework 3.x

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-system-api.git
   cd library-management-system-api

2. **Create a Virtual Environment (optional but recommended)**:
python -m venv venv
source venv/bin/activate  # On Windows use `ven

3. **Install Dependencies**:
pip install -r requirements.txt

4. **Apply Migrations**:
python manage.py migrate

5. **Run the Development Server**:
python manage.py runserver

***API ENDPOINTS***:
**Books**:
List All Books: GET /api/books/

Create a Book: POST /api/books/

Retrieve a Book: GET /api/books/<id>/

Update a Book: PUT /api/books/<id>/

Delete a Book: DELETE /api/books/<id>/

**Users**:
List All Users: GET /api/users/

Create a User: POST /api/users/

Retrieve a User: GET /api/users/<id>/

Update a User: PUT /api/users/<id>/

Delete a User: DELETE /api/users/<id>/

**Transactions**:
List User Transactions: GET /api/transactions/ (Authenticated users only)
Check Out a Book: POST /api/transactions/
Return a Book: DELETE /api/transactions/<id>/ (ID of the transaction)

