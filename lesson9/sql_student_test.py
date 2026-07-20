from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:" \
    "newpassword@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_add():
    with db.connect() as connection:
        query = text("INSERT INTO STUDENT (user_id, level, \
         education_form, subject_id) VALUES (7,2,3,4)")
        connection.execute(query)
        connection.commit()


def test_update():
    with db.connect() as connection:
        query = text("""
            UPDATE STUDENT
            SET level = 3, education_form = 4
            WHERE user_id = 5
        """)
        connection.execute(query)
        connection.commit()


def test_delete():
    with db.connect() as connection:
        query = text("DELETE FROM STUDENT WHERE user_id = 7")
        connection.execute(query)
        connection.commit()


test_add()
