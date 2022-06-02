import sqlite3

def connect_to_db(database):
    conn = sqlite3.connect(database)
    return conn

def create_db_table(database):
    try:
        conn = connect_to_db(database)
        conn.execute("DROP TABLE IF EXISTS users")
        conn.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()