from connection import get_connection

class Band:

    @staticmethod
    def get_band(band_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bands WHERE id = ?", (band_id,))
        band = cursor.fetchone()
        conn.close()
        return band

    @staticmethod
    def concerts(band_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT concerts.date, venues.title, venues.city
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        """, (band_id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def venues(band_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT venues.id, venues.title, venues.city
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        """, (band_id,))
        venues = cursor.fetchall()
        conn.close()
        return venues

    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
        conn.commit()
        conn.close()

    @staticmethod
    def all_introductions(band_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT concerts.date, venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.band_id = ?
        """, (band_id,))
        introductions = cursor.fetchall()
        conn.close()
        return [f"Hello {venue[1]}!!!!! We are {venue[2]} and we're from {venue[3]}" for venue in introductions]

    @staticmethod
    def most_performances():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.id, bands.name, COUNT(concerts.id) AS num_concerts
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            GROUP BY bands.id, bands.name
            ORDER BY num_concerts DESC
            LIMIT 1
        """)
        band = cursor.fetchone()
        conn.close()
        return band
