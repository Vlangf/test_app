import sqlite3


def prepare_test_db():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY, role TEXT, name TEXT)
    ''')

    c.execute("INSERT INTO users (role, name) VALUES ('admin', 'John')")
    c.execute("INSERT INTO users (role, name) VALUES ('user', 'Alice')")
    c.execute("INSERT INTO users (role, name) VALUES ('user', 'Bob')")

    conn.commit()
    conn.close()
