"""Shared pytest fixtures for the Employee Directory test suite."""

from collections.abc import Generator
from pathlib import Path
import sys

import pytest
from flask import Flask
from flask.testing import FlaskClient

APPLICATION_DIRECTORY = ( Path(__file__).resolve().parents[1] / "app" )

if str(APPLICATION_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(APPLICATION_DIRECTORY))
    
from app import app as employee_app
from app import init_db

@pytest.fixture()
def app(tmp_path: Path) -> Generator[Flask, None, None]:
    """Provide a Flask application using an isolated driver"""
    
    test_database = tmp_path / "test-employees.db"

    original_database = employee_app.config["DATABASE"]
    original_environment = employee_app.config["DEPLOYMENT_ENVIRONMENT"]
    original_secret_key = employee_app.config["SECRET_KEY"]

    employee_app.config.update(
        TESTING=True,
        DATABASE=str(test_database),
        DEPLOYMENT_ENVIRONMENT="testing",
        SECRET_KEY="testing-only-secret-key"
    )

    init_db()

    yield employee_app

    employee_app.config.update(
        DATABASE=original_database,
        DEPLOYMENT_ENVIRONMENT=original_environment,
        SECRET_KEY=original_secret_key,
        TESTING=False
    )

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    """Provide Flask's HTTP test client"""

    return app.test_client()