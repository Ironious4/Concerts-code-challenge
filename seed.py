import sqlite3

def seed_data():
    conn=sqlite3.connect('concerts.db')
    cursor=conn.cursor()

    cursor.execute("INSERT INTO bands(name,hometown) VALUES('Tyrone','Texas');")
    cursor.execute("INSERT INTO bands(name,hometown) VALUES('Tyler','California');")

    cursor.execute("INSERT INTO venues(title,city) VALUES('Michigan stadium','Michigan');")
    cursor.execute("INSERT INTO venues(title,city) VALUES('Ohio stadium','Ohio');")

    cursor.execute("INSERT INTO concerts(band_id,venue_id,date) VALUES(1,1, '21-09-2024');")
    cursor.execute("INSERT INTO concerts(band_id,venue_id,date) VALUES(1,1, '28-09-2024');")

    conn.commit()
    conn.close()

