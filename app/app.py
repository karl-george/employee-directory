from pathlib import Path
import sqlite3
import os
from sqlite3 import Connection

from flask import Flask, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=str(BASE_DIR / "employees.db"),
    DEPLOYMENT_ENVIRONMENT=os.getenv(
        "DEPLOYMENT_ENVIRONMENT",
        "development",
    ),
)

def get_db_connection() -> Connection:
    """Create and configure a connection to the active database."""

    connection = sqlite3.connect(app.config["DATABASE"])
    connection.row_factory = sqlite3.Row

    return connection


def init_db() -> None:
    """Create the application database schema when it does not exist."""

    connection = get_db_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


@app.route("/")
def index():
    """Display all employees."""

    connection = get_db_connection()

    employees = connection.execute(
        """
        SELECT id, name
        FROM employees
        ORDER BY id
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        employees=employees,
    )


@app.route("/add", methods=["POST"])
def add_employee():
    """Add an employee submitted through the form."""

    name = request.form.get("name", "").strip()

    if name:
        connection = get_db_connection()

        connection.execute(
            "INSERT INTO employees (name) VALUES (?)",
            (name,),
        )

        connection.commit()
        connection.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id: int):
    """Delete an employee by ID."""

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,),
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/health")
def health():
    """Return application and environment health information."""

    return {
        "status": "healthy",
        "environment": app.config["DEPLOYMENT_ENVIRONMENT"],
    }, 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)