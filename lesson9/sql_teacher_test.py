from sqlalchemy import create_engine, text
import pytest


DB_CONNECTION_STRING = "postgresql://postgres:" \
    "newpassword@localhost:5432/postgres"
engine = create_engine(DB_CONNECTION_STRING)


@pytest.fixture
def db_conn():
    with engine.connect() as connection:
        with connection.begin():
            yield connection


def test_add(db_conn):
    query = text(
        "INSERT INTO TEACHER (teacher_id, email, group_id) VALUES"
        "(100, 'test@gmail.com', 300)"
    )
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * FROM TEACHER"
                                  " WHERE teacher_id = 100")).fetchone()
    assert result is not None


def test_update(db_conn):
    db_conn.execute(text(
        "INSERT INTO TEACHER (teacher_id, email, group_id)"
        "VALUES (105, 'gtest@gmail.com', 1)"
    ))
    query = text("""
        UPDATE TEACHER
        SET group_id = 300
        WHERE teacher_id = 105
    """)
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT group_id"
                                  " FROM TEACHER WHERE"
                                  " teacher_id = 105")).scalar()
    assert result == 300


def test_delete(db_conn):
    db_conn.execute(text("INSERT INTO TEACHER (teacher_id,"
                         " email, group_id)"
                         "VALUES (115, 'gimtest@gmail.com', 1)"))
    query = text("DELETE FROM TEACHER WHERE teacher_id = 115")
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * "
                                  "FROM TEACHER WHERE"
                                  " teacher_id = 115")).fetchone()
    assert result is None
