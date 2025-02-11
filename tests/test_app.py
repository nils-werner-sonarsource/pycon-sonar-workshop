from unittest.mock import Mock

from pokedex import helper


def test_index(client):
    helper.fetch_all_pokemons = Mock(return_value=[("a", "b", "c", "d")])
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Pokedex</h1>\n" in response.data


def test_subscribe(client):
    helper.register_subscriber = Mock()
    response = client.post("/subscribe", data={"email": "blah@example.com"})
    assert response.status_code == 302
