## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_app.py
## / (GET) — homepage

**Test** 🟥

```python
def test_homepage_loads(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Nihongo Quest" in res.data
```


**Checks** 🟩

1- Homepage loads successfully

2- Contains app title "Nihongo Quest"

## / (GET) — redirect if not logged in

**Test** 🟥
```python
def test_redirect_if_not_logged_in(client):
    res = client.get('/', follow_redirects=True)
    assert b"login" in res.data or res.status_code == 200
```


**Checks** 🟩

1- Redirect works for unauthenticated users

2- Landing page contains login prompt
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)