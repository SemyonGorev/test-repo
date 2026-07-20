from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:" \
    "newpassword@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_add():
    with db.connect() as connection:
        query = text("INSERT INTO TEACHER (teacher_id, email, \
         group_id) VALUES (100, 'test@gmail.com', 300)")
        connection.execute(query)
        connection.commit()


def test_update():
     with db.connect() as connection:
        query = text("""
            UPDATE TEACHER
            SET group_id = 600
            WHERE teacher_id = 100
        """)
        connection.execute(query)
        connection.commit()  


def test_delete():
    with db.connect() as connection:
        query = text("DELETE FROM TEACHER WHERE teacher_id = 100")
        connection.execute(query)
        connection.commit()


test_delete()
