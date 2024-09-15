from connection import get_connection

class Concert:

    @staticmethod
    def band(concert_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.id, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.id = ?
        """, (concert_id,))
        band = cursor.fetchone()
        conn.close()
        return band

    @staticmethod
    def venue(concert_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT venues.id, venues.title, venues.city
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (concert_id,))
        venue = cursor.fetchone()
        conn.close()
        return venue

    @staticmethod
    def hometown_show(concert_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (concert_id,))
        hometown, city = cursor.fetchone()
        conn.close()
        return hometown == city

    @staticmethod
    def introduction(concert_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.id = ?
        """, (concert_id,))
        venue_city, band_name, band_hometown = cursor.fetchone()
        conn.close()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
