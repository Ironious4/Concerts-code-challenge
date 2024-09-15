import sqlite3

def create_schema():
    conn=sqlite3.connect('concerts.db')
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            hometown VARCHAR(255)
        );

    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            city VARCHAR(255)
        );

    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_id INTEGER,
            venue_id INTEGER,
            date VARCHAR(255),
            FOREIGN KEY (band_id) REFERENCES bands(id) ON DELETE CASCADE,
            FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
        );

    """)

    conn.commit()
    conn.close()