from connection import get_connection

class Venue:

    @staticmethod
    def get_venue(venue_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM venues WHERE id = ?", (venue_id,))
        venue = cursor.fetchone()
        conn.close()
        return venue

    @staticmethod
    def concerts(venue_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT concerts.date, bands.name
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
        """, (venue_id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def bands(venue_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT bands.id, bands.name
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
        """, (venue_id,))
        bands = cursor.fetchall()
        conn.close()
        return bands

    @staticmethod
    def concert_on(venue_id, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT concerts.id, bands.name
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ? AND concerts.date = ?
            LIMIT 1
        """, (venue_id, date))
        concert = cursor.fetchone()
        conn.close()
        return concert

    @staticmethod
    def most_frequent_band(venue_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.id, bands.name, COUNT(concerts.id) AS num_concerts
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id, bands.name
            ORDER BY num_concerts DESC
            LIMIT 1
        """, (venue_id,))
        band = cursor.fetchone()
        conn.close()
        return band
