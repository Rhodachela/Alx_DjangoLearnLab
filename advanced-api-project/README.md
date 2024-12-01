# Advanced API Project

This project demonstrates advanced API development using Django REST Framework, including custom views, generic views, and serializers.

## Features
- Models: `Author` and `Book` with nested relationships.
- CRUD operations for `Book` via generic views.
- Custom validation for book creation.
- Permission control for API endpoints.

## API Endpoints

| Method | Endpoint             | Description               |
|--------|----------------------|---------------------------|
| GET    | `/api/books/`        | List all books.           |
| GET    | `/api/books/<id>/`   | Retrieve a specific book. |
| POST   | `/api/books/`        | Create a new book.        |
| PUT    | `/api/books/<id>/`   | Update a book.            |
| DELETE | `/api/books/<id>/`   | Delete a book.            |

## Setup Instructions

### Prerequisites
- Python 3.9+ and `pip` installed.
- Virtual environment installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/advanced_api_project
