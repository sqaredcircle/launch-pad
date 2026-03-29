# launch-pad

A training project for learning Claude Code, built with FastAPI and Typer.

## What it does

launch-pad is a release-tracking application with:

- **FastAPI backend** — REST API with SQLite persistence via SQLAlchemy
- **Typer CLI** — command-line interface for interacting with the app
- **Release model** — tracks software releases through `draft → active → shipped` states

## Project structure

```
app/
  main.py       # FastAPI app and routes
  database.py   # SQLAlchemy engine, session, and init
  models.py     # Release ORM model
cli/
  main.py       # Typer CLI entry point
tests/
  test_health.py
pyproject.toml
```

## Getting started

```bash
# Install dependencies (requires uv)
uv sync

# Run the API server
uv run uvicorn app.main:app --reload

# Run the CLI
uv run launch-pad hello

# Run tests
uv run pytest
```

## API

| Method | Path      | Description        |
|--------|-----------|--------------------|
| GET    | /health   | Health check       |
