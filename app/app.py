from pathlib import Path
import sqlite3
import os

from flask import Flask, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "employees.db"

app = Flask(__name__)


def get_db_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
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
    connection = get_db_connection()

    employees = connection.execute(
        "SELECT id, name FROM employees ORDER BY id"
    ).fetchall()

    connection.close()

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["POST"])
def add_employee():
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
    environment = os.getenv("DEPLOYMENT_ENVIRONMENT", "development")
    return {
        "status": "healthy",
        "environment": environment,
    }, 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)