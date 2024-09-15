# app.py
from schema import create_schema
from seed import seed_data
from band import Band
from concert import Concert
from venue import Venue

if __name__ == '__main__':
    create_schema()
    seed_data()

    # Band operations
    print("Band concerts:", Band.concerts(1))
    print("Band venues:", Band.venues(1))
    print("All Introductions:", Band.all_introductions(1))
    print("Band with most performances:", Band.most_performances())

    # Venue operations
    print("Venue concerts:", Venue.concerts(1))
    print("Venue bands:", Venue.bands(1))
    print("Concert on date:", Venue.concert_on(1, '21-09-2024'))
    print("Most frequent band at venue:", Venue.most_frequent_band(1))

    # Concert operations
    print("Concert band:", Concert.band(1))
    print("Concert venue:", Concert.venue(1))
    print("Is hometown show:", Concert.hometown_show(1))
    print("Concert introduction:", Concert.introduction(1))
