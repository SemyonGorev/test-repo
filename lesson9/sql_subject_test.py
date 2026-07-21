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
        "INSERT INTO SUBJECT (subject_id, \
         subject_title) VALUES (16, 'Archery')")
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * FROM SUBJECT "
                                  "WHERE subject_id = 16")).fetchone()
    assert result is not None


def test_update(db_conn):
    db_conn.execute(text(
        "INSERT INTO SUBJECT (subject_id, \
         subject_title) VALUES (17, 'Pilgrimage')"
    ))
    query = text("""
        UPDATE SUBJECT
        SET subject_title = 'Fencing'
        WHERE subject_id = 17
    """)
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT "
                                  "subject_title FROM SUBJECT"
                                  " WHERE subject_id = 17")).scalar()
    assert result == 'Fencing'


def test_delete(db_conn):
    db_conn.execute(text(
        "INSERT INTO SUBJECT (subject_id, \
         subject_title) VALUES (18, 'Fishnig')"
    ))
    query = text("DELETE FROM SUBJECT WHERE subject_id = 18")
    db_conn.execute(query)
    result = db_conn.execute(text("SELECT * FROM SUBJECT WHERE "
                                  "subject_id = 18")).fetchone()
    assert result is None
