FROM python:3.12.8-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

FROM python:3.12.8-slim

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

COPY core users restaurants voting manage.py ./

RUN adduser --disabled-password --no-create-home django-user && \
  chown -R django-user:django-user /app/ && \
  chmod -R 755 /app/

USER django-user

EXPOSE 8000
