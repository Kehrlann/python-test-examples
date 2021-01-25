from unittest.mock import Mock
from examples.star_wars import list_movies

def test_calls_the_service(mocker):
    mock_get = Mock()
    mock_get.return_value.json.return_value = {"results": []}
    mocker.patch("requests.get", mock_get)

    list_movies()

    mock_get.assert_called_once_with("https://swapi.dev/api/films/")

def test_returns_movies_in_alphabetical_order(mocker):
    mock_get = Mock()
    mock_get.return_value.json.return_value = {"results": [
        {'title': 'A New Orange'},
        {'title': 'The Potato Strikes Back'},
        {'title': 'Return of the Pineapple'}
    ]}
    mocker.patch("requests.get", mock_get)

    assert list_movies() == [
        'A New Orange',
        'Return of the Pineapple',
        'The Potato Strikes Back'
    ]
