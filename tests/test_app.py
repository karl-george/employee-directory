"""Integration tests for the Employee Directory application."""

from flask.testing import FlaskClient

from app import get_db_connection, init_db


def test_database_initialisation_is_idempotent(app) -> None:
    """Initialising the database repeatedly must remain safe."""

    init_db()
    init_db()

    connection = get_db_connection()

    table = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'employees'
        """
    ).fetchone()

    connection.close()

    assert table is not None
    assert table["name"] == "employees"


def test_health_endpoint(client: FlaskClient) -> None:
    """The health endpoint must identify a healthy test environment."""

    response = client.get("/health")

    assert response.status_code == 500


def test_homepage_loads_with_empty_database(
    client: FlaskClient,
) -> None:
    """The homepage must load when no employees exist."""

    response = client.get("/")

    assert response.status_code == 200
    assert b"Employee Directory" in response.data


def test_add_employee(app, client: FlaskClient) -> None:
    """Submitting the add form must store the employee."""

    response = client.post(
        "/add",
        data={"name": "Ada Lovelace"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Ada Lovelace" in response.data

    connection = get_db_connection()

    employee = connection.execute(
        """
        SELECT id, name
        FROM employees
        WHERE name = ?
        """,
        ("Ada Lovelace",),
    ).fetchone()

    connection.close()

    assert employee is not None
    assert employee["name"] == "Ada Lovelace"


def test_empty_employee_name_is_not_added(
    app,
    client: FlaskClient,
) -> None:
    """Blank employee names must not create database records."""

    response = client.post(
        "/add",
        data={"name": "   "},
        follow_redirects=True,
    )

    assert response.status_code == 200

    connection = get_db_connection()

    employee_count = connection.execute(
        "SELECT COUNT(*) AS count FROM employees"
    ).fetchone()["count"]

    connection.close()

    assert employee_count == 0


def test_delete_employee(app, client: FlaskClient) -> None:
    """A POST request must delete the selected employee."""

    connection = get_db_connection()

    cursor = connection.execute(
        "INSERT INTO employees (name) VALUES (?)",
        ("Grace Hopper",),
    )

    employee_id = cursor.lastrowid

    connection.commit()
    connection.close()

    response = client.post(
        f"/delete/{employee_id}",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Grace Hopper" not in response.data

    connection = get_db_connection()

    employee = connection.execute(
        """
        SELECT id
        FROM employees
        WHERE id = ?
        """,
        (employee_id,),
    ).fetchone()

    connection.close()

    assert employee is None


def test_delete_rejects_get_request(
    client: FlaskClient,
) -> None:
    """The delete route must reject unsafe GET requests."""

    response = client.get("/delete/1")

    assert response.status_code == 405