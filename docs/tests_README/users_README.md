## Comeback [README](../../README.m#nihongo-quest--routes-functions--tests-overviewd)
# tests/test_user.py
## /register (POST)

**Test** 🟥
```python
def test_register_user(client):
    res = client.post("...
    }, follow_redirects=True)
    assert b"Account created!" in res.data
```

**Checks** 🟩

1- Form submits correctly

2- User is created

3- Flash message appears

## /login (POST) — valid

**Test** 🟥
```python
def test_login_valid_user(client, create_user):
    create_user()
    ...
    assert b"Login successful!" in res.data
```

**Checks** 🟩

1- Valid credentials authenticate

2- Session starts

3- Success flash message

## /login (POST) — invalid

**Test** 🟥
```python
def test_login_invalid_user(client, create_user):
    create_user()
    res = client.post("/login", {
        ...
    }, follow_redirects=True)
    assert b"Login successful!" in res.data
```

**Checks** 🟩

1- Wrong credentials fail

2- Error flash message

## /logout (GET)

**Test** 🟥
```python
def test_logout(client, create_user):
    user = create_user()
    client.post("/login", {
        ...
    })
    res = client.get("/logout", follow_redirects=True)
    assert b"Logged out!" in res.data
```

**Checks** 🟩

1- Requires login

2- Logs out user

3- Flash message shown

4- Root page

**Test** 🟥
```python
def test_something(client):
    assert client.get('/').status_code == 200
```


**Checks** 🟩

- App loads successfully
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)