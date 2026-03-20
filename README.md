# Lunch Voting API

Lunch Voting API is a Django REST Framework application for managing daily restaurant menus and employee voting. It supports semantic versioning for API endpoints and JWT authentication.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started (Development)](#getting-started-development)
- [Running in Production-like Environment](#running-in-production-like-environment)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Manual Testing](#manual-testing)

---

## Features

- Restaurants and daily menus management
- Employee voting for daily menu
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
docker compose up --build api
```

> This will run migrations automatically and start the development server on `0.0.0.0:8000`.

3. Access the API:

```
http://127.0.0.1:8000/
```

4. Optional: Access Django Debug Toolbar, ruff, pytest inside container if `DEVELOPMENT=1`.

---

## Running in Production-like Environment

To test a production-like setup without full deployment:

```bash
docker compose build --build-arg DEVELOPMENT=0 api
docker compose up api
```

> This uses a slimmed-down Python environment, only installing production dependencies via `uv sync --no-dev --frozen --no-cache`.

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

## Manual Testing

* Create a user via admin or shell.
* Add restaurants and menus.
* Test voting via Postman, curl, or similar tools.
* Automated tests are not included due to time constraints.

### Example: Fetch today's results with versioning

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/votes/results/today/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'X-App-Version: 2.0.0'
```

> Replace `<ACCESS_TOKEN>` with the JWT access token obtained from `/api/token/`.
> The `X-App-Version` header allows testing different API versions (e.g., `1.0.0` vs `2.0.0`).

---

## Notes

* Ensure Docker containers are healthy before accessing the API.
* Semantic versioning ensures backward-compatible API responses.
* Menus cannot be modified once voting has started.