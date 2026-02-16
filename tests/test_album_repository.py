from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data
"""
def test_get_all_album_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
    Album(1, "Doolittle", 1989, 1),
    Album(2, "Surfer Rosa", 1988, 1),
    Album(3, "Waterloo", 1974, 2),
    Album(4, "Super Trouper", 1980, 2),
    Album(5, "Bossanova", 1990, 1),
    Album(6, "Lover", 2019, 3),
    Album(7, "Folklore", 2020, 3),
    Album(8, "I Put a Spell on You", 1965, 4),
    Album(9, "Baltimore", 1978, 4),
    Album(10, "Here Comes the Sun", 1971, 4),
    Album(11, "Fodder on My Wings", 1982, 4),
    Album(12, "Ring Ring", 1973, 2)
]

"""
When we call AlbumRepository#find_album
We get a single Album object reflecting the seed data.
"""
def test_get_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find_album(3)
    assert album == Album(3, "Waterloo", 1974, 2)

"""
When I call #find on the AlbumRepository with an id
I am returned an artist with a corresponding id
"""
def test_find_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_album(4) == Album(4, "Super Trouper", 1980, 2)

"""
When we call AlbumRepository#create_album
We get a new record in the database.
"""
def test_create_single_album(db_connection):
   db_connection.seed("seeds/music_library.sql")
   repository = AlbumRepository(db_connection)

   repository.create_album(Album(None, "The Life of a Showgirl", 2025, 3))
   assert repository.all() == [
    Album(1, "Doolittle", 1989, 1),
    Album(2, "Surfer Rosa", 1988, 1),
    Album(3, "Waterloo", 1974, 2),
    Album(4, "Super Trouper", 1980, 2),
    Album(5, "Bossanova", 1990, 1),
    Album(6, "Lover", 2019, 3),
    Album(7, "Folklore", 2020, 3),
    Album(8, "I Put a Spell on You", 1965, 4),
    Album(9, "Baltimore", 1978, 4),
    Album(10, "Here Comes the Sun", 1971, 4),
    Album(11, "Fodder on My Wings", 1982, 4),
    Album(12, "Ring Ring", 1973, 2),
    Album(13, "The Life of a Showgirl", 2025, 3)
   ]

"""
When we call AlbumRepository#delete_album
We delete a record in the database.
"""
def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete_album(13)
    assert repository.all() == [
    Album(1, "Doolittle", 1989, 1),
    Album(2, "Surfer Rosa", 1988, 1),
    Album(3, "Waterloo", 1974, 2),
    Album(4, "Super Trouper", 1980, 2),
    Album(5, "Bossanova", 1990, 1),
    Album(6, "Lover", 2019, 3),
    Album(7, "Folklore", 2020, 3),
    Album(8, "I Put a Spell on You", 1965, 4),
    Album(9, "Baltimore", 1978, 4),
    Album(10, "Here Comes the Sun", 1971, 4),
    Album(11, "Fodder on My Wings", 1982, 4),
    Album(12, "Ring Ring", 1973, 2),
   ]