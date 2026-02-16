from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data
"""
def test_get_all_album_records(db_connection):
    db_connection.seed("seeds/records_store.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
    Album(1, 'Neon Skies', 2020, 1),
    Album(2, 'Broken Satellites', 2016, 2),
    Album(3, 'Midnight Echoes', 2018, 3),
    Album(4, 'Golden Static', 2022, 4)
]

"""
When we call AlbumRepository#find_album
We get a single Album object reflecting the seed data.
"""
def test_get_single_album(db_connection):
    db_connection.seed("seeds/records_store.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find_album(3)
    assert album == Album(3, 'Midnight Echoes', 2018, 3)

"""
When I call #find on the AlbumRepository with an id
I am returned an artist with a corresponding id
"""
def test_find_album(db_connection):
    db_connection.seed("seeds/records_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_album(4) == Album(4, 'Golden Static', 2022, 4)

"""
When we call AlbumRepository#create_album
We get a new record in the database.
"""
def test_create_single_album(db_connection):
   db_connection.seed("seeds/records_store.sql")
   repository = AlbumRepository(db_connection)

   repository.create_album(Album(None, "Voyage", 2022, 2))
   assert repository.all() == [
    Album(1, 'Neon Skies', 2020, 1),
    Album(2, 'Broken Satellites', 2016, 2),
    Album(3, 'Midnight Echoes', 2018, 3),
    Album(4, 'Golden Static', 2022, 4),
    Album(5, 'Voyage', 2022, 2)
   ]

"""
When we call AlbumRepository#delete_album
We delete a record in the database.
"""
def test_delete_album(db_connection):
    db_connection.seed("seeds/records_store.sql")
    repository = AlbumRepository(db_connection)

    repository.delete_album(5)
    assert repository.all() == [
    Album(1, 'Neon Skies', 2020, 1),
    Album(2, 'Broken Satellites', 2016, 2),
    Album(3, 'Midnight Echoes', 2018, 3),
    Album(4, 'Golden Static', 2022, 4),
   ]