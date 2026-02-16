# Tests for your routes go here

"""
When I call GET /albums,
I am returned a full list of albums
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/records_store.sql")
    response = web_client.get("/albums")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == (
        "Album(1, Neon Skies, 2020, 1)"
        "Album(2, Broken Satellites, 2016, 2)"
        "Album(3, Midnight Echoes, 2018, 3)"
        "Album(4, Golden Static, 2022, 4)"
    )

"""
When I call POST /albums with album info,
I can see it this new album in the list in GET /albums 
"""
def test_post_new_album(db_connection, web_client):
    db_connection.seed("seeds/records_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Voyage', 
        'release_year': '2022', 
        'artist_id': '2'}
        )
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
        "Album(1, Neon Skies, 2020, 1)"
        "Album(2, Broken Satellites, 2016, 2)"
        "Album(3, Midnight Echoes, 2018, 3)"
        "Album(4, Golden Static, 2022, 4)"
        "Album(5, Voyage, 2022, 2)"
    )