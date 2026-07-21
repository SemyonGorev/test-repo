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
        "INSERT INTO STUDENT (user_id, level,"
        " education_form, subject_id) "
        "VALUES (7, 2, 3, 4)"
    )
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * FROM STUDENT"
                                  " WHERE user_id = 7")).fetchone()
    assert result is not None


def test_update(db_conn):
    db_conn.execute(text(
        "INSERT INTO STUDENT (user_id,"
        " level, education_form, subject_id) "
        "VALUES (5, 1, 1, 1)"
    ))
    query = text("""
        UPDATE STUDENT
        SET level = 3, education_form = 4
        WHERE user_id = 5
    """)
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT level"
                                  " FROM STUDENT WHERE user_id = 5")).scalar()
    assert result == '3'


def test_delete(db_conn):
    db_conn.execute(text(
        "INSERT INTO STUDENT (user_id, level,"
        " education_form, subject_id) "
        "VALUES (7, 2, 3, 4)"
    ))
    query = text("DELETE FROM STUDENT WHERE user_id = 7")
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * FROM STUDENT WHERE"
                                  " user_id = 7")).fetchone()
    assert result is None
