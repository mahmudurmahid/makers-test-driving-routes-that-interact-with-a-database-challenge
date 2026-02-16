from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(14, "Test Album", 2000, 1)
    assert album.id == 14
    assert album.title == "Test Album"
    assert album.release_year == 2000
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def tests_albums_format_nicely():
    album = Album(14, "Test Album", 2000, 1)
    assert str(album) == "Album(14, Test Album, 2000, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def tests_albums_are_equal():
    album1 = (14, "Test Album", 2000, 1)
    album2 = (14, "Test Album", 2000, 1)
    assert album1 == album2