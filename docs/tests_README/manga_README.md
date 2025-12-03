## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_manga.py
## /manga — GET
**Test** 🟥
```python
@patch('routes.manga_routes.requests.get')
def test_manga_route(mock_get, client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'data': [
            {
                'title': 'Mock Manga 1',
                'images': {'jpg': {'image_url': 'http://example.com/mock1.jpg'}}
            },
            {
                'title': 'Mock Manga 2',
                'images': {'jpg': {'image_url': 'http://example.com/mock2.jpg'}}
            }
        ]
    }
    mock_get.return_value = mock_response

    response = client.get('/manga')
    assert response.status_code == 200
    assert b'Mock Manga 1' in response.data or b'Mock Manga 2' in response.data
```
**Checks** 🟩

1- Manga list page loads

2- External API request is mocked

3- Renders manga titles returned by the API

4- Template handles images from mocked response

## /search (GET) — With query
**Test** 🟥
```python
@patch('routes.manga_routes.requests.get')
def test_search_route_with_query(mock_get, client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'data': [
            {
                'title': 'Search Result Manga',
                'images': {'jpg': {'image_url': 'http://example.com/search.jpg'}}
            }
        ]
    }
    mock_get.return_value = mock_response

    response = client.get('/search?query=naruto')
    assert response.status_code == 200
    assert b'Search Result Manga' in response.data
```
**Checks** 🟩

1- Search page returns 200

2-  API is called with query

3-  Displays manga results from mocked API

4- Template handles correctly the search request

## /search (GET) — Without query
**Test** 🟥
```python
def test_search_route_without_query(client):
    response = client.get('/search')
    assert response.status_code == 200
    assert b'<title>' in response.data
```
**Checks** 🟩

1- Page loads without errors

2-  No API call performed

3-  Returns an empty or default page

4- Template renders even with no query
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)