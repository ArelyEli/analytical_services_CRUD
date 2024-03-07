# Technical test CRUD (Create, Reed, Update, Delete)

The goal of this project is to implement a simple CRUD (Create, Reed, Update, Delete) for a specific entity, in this case, "Product", with the addition of a user authentication system that allows only authenticated users to create , update or delete products. Using FastAPI as a Python framework, PostgreSQL as a database and Doker for the container.

## Usage
Clone this repository to your local machine: 
```sh
git clone git@github.com:ArelyEli/analytics_associates_CRUD.git
```

To run the project you can use `docker` and `docker compose` for that you run the following command in the terminal, this will start the PostgreSQL database and server in FastAPI:
```sh
docker compose up
```

This going to start the server in:
```sh
http://localhost:8000/
```

## API Documentation
The paths to the API documentation are `/docs` or `/redoc`, generated with `Swagger` and `ReDoc`.
```sh
http://localhost:8000/docs
```

The endpoints created are the following:

Login endpoint, this endpoint going to return the token for the user:
```sh
curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=my_username&password=my_password&scope=&client_id=&client_secret='
```

Signup endpoint, this endpoint is to create a new user:
```sh
curl -X 'POST' \
  'http://localhost:8000/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "my_username",
  "email": "my_email",
  "password": "my_password"
}'
```

Create new product endpoint, this endpoint recive the information for the new product and add the product to the DB.
Notice that a token is required:
```sh
curl -X 'POST' \
  'http://localhost:8000/products' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 0,
  "stock": 0
}'
```

Get all products endpoint, this endpoint return the information of all products.
Notice that a token is not required is a public endpoint:
```sh
curl -X 'GET' \
  'http://localhost:8000/products' \
  -H 'accept: application/json'
}'
```

Get a product details endpoint, this endpoint return the information of a product.
Notice that a token is not required is a public endpoint:
```sh
curl -X 'GET' \
  'http://localhost:8000/products/<id>' \
  -H 'accept: application/json'
```

Delete a produc.
Notice that a token is required, only users can delete products:
```sh
curl -X 'DELETE' \
  'http://localhost:8000/products/<id>' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>'
```

Modify a produc.
Notice that a token is required, only users can modify products and all fields are optional, that means that you can only change one field:
```sh
curl -X 'PATCH' \
  'http://localhost:8000/products/<id>' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 0,
  "stock": 0
}'
```

## Highlight
 - It was decided not to allow duplicate products, for this different verifications are carried out.
 - A verification is made on the users, in this way the users cannot be duplicated based on email.
 - It was decided to follow the PEP8 standards in code quality, for this the `flake` library was used.
 - Used `PostgreSQL` along with `SQLAlchemy` for database design.
 - A Github Action was added to verify code quality.

