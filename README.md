# Lunch Voting API

Lunch Voting API is a Django REST Framework application for managing daily restaurant menus and employee voting. It supports semantic versioning for API endpoints and JWT authentication.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started (Development)](#getting-started-development)
- [Running UV / Dev Commands](#running-dev-commands)
- [Running in Production-like Environment](#running-in-production-like-environment)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Manual Testing](#manual-testing)

---

## Features

- Restaurants and daily menus management
- Employee voting for daily menus
- Versioned API endpoints (`v1`, `v2`, etc.)
- JWT-based authentication
- Swagger / OpenAPI documentation via drf-spectacular

---

## Requirements

- Docker & Docker Compose
- Python 3.12+
- PostgreSQL 16

---

## Getting Started (Development)

1. Copy `.env.sample` to `.env` and fill in the values:

```bash
cp .env.sample .env
````

2. Build and start the development container:

```bash
docker compose up --build
```

> This will run migrations automatically and start the development server on `0.0.0.0:8000`.

3. Access the API:

```
http://127.0.0.1:8000/
```

4. Optional: If `DEVELOPMENT=1` you can use Django Debug Toolbar, `ruff`, `pytest`, etc. inside the container.

---

## Running DEV Commands

### Install dependencies outside of docker:

```bash
uv sync
```

### Create superuser:

```bash
docker compose run --rm api sh -c "python manage.py createsuperuser"
```

### Linting

```bash
# Using Docker
docker compose exec api ruff check .
docker compose exec api ruff check . --fix

# Using uv locally
uv run ruff check .
uv run ruff check . --fix
```

### Formatting

```bash
# Using Docker
docker compose exec api ruff format .

# Using uv locally
uv run ruff format .
```

### Testing

Run `pytest` in the container:

```bash
docker compose exec api pytest
```

> Automated tests are minimal / not included for some endpoints due to time constraints.

---

## Running in Production-like Environment

To test a production-like setup without full deployment:

```bash
docker compose up --build
```

> This uses a slimmed-down Python environment, installing only production dependencies via `uv sync --no-dev --frozen --no-cache`.

---

## Environment Variables

### API

```
DEVELOPMENT=
SECRET_KEY=
API_PORT=
```

### JWT

```
ACCESS_TOKEN_LIFETIME=
REFRESH_TOKEN_LIFETIME=
```

### Database

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
```

---

## API Documentation

* OpenAPI schema is generated via **drf-spectacular**
* Access Swagger UI at:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## API Endpoints

| Resource        | Method    | Endpoint                       | Description                                         | Example cURL                                                                                                                                                                                                                  |
| --------------- | --------- | ------------------------------ | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Register        | POST      | `/api/auth/register/`          | Public endpoint to create a new user                | `curl -X POST [http://127.0.0.1:8000/api/auth/register/](http://127.0.0.1:8000/api/auth/register/) -H "Content-Type: application/json" -d '{"email":"[user@example.com](mailto:user@example.com)","password":"strongpass"}"'  |
| Login           | POST      | `/api/auth/login/`             | Obtain JWT tokens (access & refresh)                | `curl -X POST [http://127.0.0.1:8000/api/auth/login/](http://127.0.0.1:8000/api/auth/login/) -H "Content-Type: application/json" -d '{"email":"[user@example.com](mailto:user@example.com)","password":"strongpass"}"'        |
| Refresh Token   | POST      | `/api/auth/token/refresh/`     | Refresh access token using refresh token            | `curl -X POST [http://127.0.0.1:8000/api/auth/token/refresh/](http://127.0.0.1:8000/api/auth/token/refresh/) -H "Content-Type: application/json" -d '{"refresh":"<REFRESH_TOKEN>"}"'                                          |
| Current User    | GET       | `/api/users/me/`               | Get current authenticated user profile              | `curl -X GET http://127.0.0.1:8000/api/users/me/ -H "Authorization: Bearer <ACCESS_TOKEN>"`                                                                                                                                   |
| Current User    | PUT/PATCH | `/api/users/me/`               | Update current authenticated user                   | `curl -X PATCH [http://127.0.0.1:8000/api/users/me/](http://127.0.0.1:8000/api/users/me/) -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"first_name":"John"}"'                           |
| Restaurants     | GET       | `/api/restaurants/`            | List all restaurants                                | `curl -X GET http://127.0.0.1:8000/api/restaurants/ -H "Authorization: Bearer <ACCESS_TOKEN>"`                                                                                                                                |
| Restaurants     | POST      | `/api/restaurants/`            | Create a restaurant (Admin only)                    | `curl -X POST [http://127.0.0.1:8000/api/restaurants/](http://127.0.0.1:8000/api/restaurants/) -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"name":"Pizza House"}"'                     |
| Upload Menu     | POST      | `/api/restaurants/<id>/menus/` | Upload menu for a restaurant for today (Admin only) | `curl -X POST [http://127.0.0.1:8000/api/restaurants/1/menus/](http://127.0.0.1:8000/api/restaurants/1/menus/) -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"items":{"dish":"Pizza"}}"' |
| Today's Menus   | GET       | `/api/restaurants/today/`      | List today's menus (versioned response)             | `curl -X GET http://127.0.0.1:8000/api/restaurants/today/ -H "Authorization: Bearer <ACCESS_TOKEN>" -H "X-App-Version: 2.0.0"`                                                                                                |
| Cast Vote       | POST      | `/api/votes/`                  | Cast a vote for a menu                              | `curl -X POST http://127.0.0.1:8000/api/votes/ -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"menu_id":1}'`                                                                              |
| Today's Results | GET       | `/api/votes/results/today/`    | Get today's voting results (versioned response)     | `curl -X GET http://127.0.0.1:8000/api/votes/results/today/ -H "Authorization: Bearer <ACCESS_TOKEN>" -H "X-App-Version: 2.0.0"`                                                                                              |

> Notes:
>
> * Replace `<ACCESS_TOKEN>` with a valid JWT access token.
> * `X-App-Version` header allows testing different API versions (`1.0.0`, `2.0.0`, etc.).
> * Admin endpoints require the user to have `is_staff=True`.
> * Menus cannot be modified once voting has started.

---

## Manual Testing

* Create a user via admin or shell.
* Add restaurants and menus.
* Test voting via Postman, curl, or similar tools.

### Example: Fetch today's results with versioning

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/votes/results/today/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'X-App-Version: 2.0.0'
```