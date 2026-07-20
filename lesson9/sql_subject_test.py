from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:" \
    "newpassword@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_add():
    with db.connect() as connection:
        query = text("INSERT INTO SUBJECT (subject_id, \
         subject_title) VALUES (16, 'Archery')")
        connection.execute(query)
        connection.commit()


def test_update():
     with db.connect() as connection:
        query = text("""
            UPDATE SUBJECT
            SET subject_title = 'fencing'
            WHERE subject_id = 16
        """)
        connection.execute(query)
        connection.commit()  


def test_delete():
    with db.connect() as connection:
        query = text("DELETE FROM SUBJECT WHERE subject_id = 16")
        connection.execute(query)
        connection.commit()


test_update()
