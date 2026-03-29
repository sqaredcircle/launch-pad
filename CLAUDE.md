# launch-pad

## Project Overview
A Python CLI + FastAPI API for tracking product launches and release briefs.

## Architecture
- FastAPI backend in app/ with async routes
- Typer CLI in cli/ that talks to the API via httpx
- SQLite database via SQLAlchemy (async)

## Code Conventions
- All FastAPI route handlers must be async
- Route handlers go in app/routers/ as separate files (NOT in app/main.py)
- app/main.py only contains app initialization and router includes
- Pydantic models for ALL request/response schemas in app/schemas.py
- SQLAlchemy models stay in app/models.py
- Type hints on every function signature
- Docstrings on all public functions
- Use f-strings for string formatting (never .format() or %)

## Linting & Formatting
- Use ruff: "ruff check ." for linting, "ruff format ." for formatting
- Run both before committing

## Testing
- pytest with pytest-asyncio
- Use httpx.AsyncClient for API endpoint tests
- Test files go in tests/ with test_ prefix
- Every new feature needs at least one test

## Git Conventions
- Conventional commits: feat:, fix:, docs:, refactor:, test:, chore:
- Feature branches off main
- PRs required for all changes

## Commands
- python -m venv .venv && source .venv/bin/activate  (setup)
- pip install -e ".[dev]"  (install with dev deps)
- uvicorn app.main:app --reload  (dev server)
- python -m pytest -v  (run tests)
- ruff check . && ruff format .  (lint and format)
