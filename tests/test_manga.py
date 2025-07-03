import pytest
from unittest.mock import patch, MagicMock

# Test /manga route
@patch('routes.manga_routes.requests.get')
def test_manga_route(mock_get, client):
    # Mock API response con estructura esperada en template
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'data': [
            {
                'title': 'Mock Manga 1',
                'images': {
                    'jpg': {
                        'image_url': 'http://example.com/mock1.jpg'
                    }
                }
            },
            {
                'title': 'Mock Manga 2',
                'images': {
                    'jpg': {
                        'image_url': 'http://example.com/mock2.jpg'
                    }
                }
            }
        ]
    }
    mock_get.return_value = mock_response

    response = client.get('/manga')
    assert response.status_code == 200
    assert b'Mock Manga 1' in response.data or b'Mock Manga 2' in response.data

# Test /search with query
@patch('routes.manga_routes.requests.get')
def test_search_route_with_query(mock_get, client):
    # Mock API search response con estructura esperada
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'data': [
            {
                'title': 'Search Result Manga',
                'images': {
                    'jpg': {
                        'image_url': 'http://example.com/search.jpg'
                    }
                }
            }
        ]
    }
    mock_get.return_value = mock_response

    response = client.get('/search?query=naruto')
    assert response.status_code == 200
    assert b'Search Result Manga' in response.data

# Test /search without query
def test_search_route_without_query(client):
    response = client.get('/search')
    assert response.status_code == 200
    # No query means empty data
    assert b'<title>' in response.data  # Page loads
