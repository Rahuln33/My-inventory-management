```markdown
# Inventory Management System with JWT Authentication

This is a Django REST API project that allows users to manage an inventory of items. The project includes features for creating, reading, updating, and deleting inventory items (CRUD) while ensuring secure access using JWT (JSON Web Token) authentication.

## Features

- **JWT Authentication**: Secure access to API endpoints using token-based authentication.
- **CRUD Operations**: Create, read, update, and delete items in the inventory.
- **Caching**: Cached item data for optimized read performance.
- **Token Refresh**: Option to refresh the JWT tokens to maintain authenticated sessions.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Authentication**: Simple JWT (`rest_framework_simplejwt`)
- **Database**:  mysql database (can be changed to other databases)
- **Caching**: Django's default caching mechanism

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.10 or above
- Django 5.1 or above
- Virtualenv (optional but recommended)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
```

### 2. Set up the virtual environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### 3. Install dependencies

Install the required dependencies listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Run the following commands to apply the migrations and create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin user.

### 6. Run the development server

Start the Django development server using:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

- **Obtain Token**: `/api/token/` (POST)
  - Use this endpoint to obtain a JWT token by providing valid user credentials.
  
- **Refresh Token**: `/api/token/refresh/` (POST)
  - Use this endpoint to refresh your JWT token.

### CRUD Operations

- **Create Item**: `POST /api/items/`
  - Add a new item to the inventory.
  
- **Read Items**: `GET /api/items/`
  - Retrieve the list of all items in the inventory.
  
- **Read Item by ID**: `GET /api/items/{id}/`
  - Retrieve details of a specific item by its ID.
  
- **Update Item**: `PUT /api/items/{id}/`
  - Update the details of an existing item by its ID.
  
- **Delete Item**: `DELETE /api/items/{id}/`
  - Delete an item from the inventory by its ID.

### Example Usage

#### 1. Obtain a Token

```bash
POST /api/token/
{
    "username": "root",
    "password": "root"
}
```

#### 2. Use the Token for Authentication

Include the JWT token in the `Authorization` header for all authenticated requests:

```bash
Authorization: Bearer your_token
```

#### 3. Create a New Item

```bash
POST /api/items/
{
    "name": "New Item",
    "description": "Description of the new item"
}
```

#### 4. Get All Items

```bash
GET /api/items/
```

#### 5. Update an Item

```bash
PUT /api/items/1/
{
    "name": "Updated Item Name",
    "description": "Updated description"
}
```

#### 6. Delete an Item

```bash
DELETE /api/items/1/
```

## Caching

To improve performance, item details are cached when retrieved. If an item is requested, it is first checked in the cache. If not found, the item is fetched from the database and stored in the cache for 15 minutes.

## Running Tests

To run the tests for the project, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you'd like to contribute, feel free to submit a pull request or open an issue.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!
```

### Instructions to follow:
1. **Update the GitHub URL**: Replace `https://github.com/Rahuln33/My-inventory-management` with your GitHub username in the clone command.
2. **Fill in Project-Specific Details**:   My inventory management project is a backend API built with Django REST Framework. It allows users to manage items in an inventory system with full CRUD functionality. I implemented JWT-based authentication for secure access, and caching for optimized data retrieval. The project handles all common item management tasks such as creating, updating, reading, and deleting inventory items while maintaining high security through token-based user verification. This project helped me strengthen my skills in RESTful API development, authentication, caching, and performance optimization."
