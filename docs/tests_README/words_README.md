## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_words.py
## /words — Access protection

**Test** 🟥
```python
def test_words_access_protection(client):
    response = client.get("/words")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
```

**Checks** 🟩

1- Unauthenticated users are redirected to login (302)

2- Login URL present in Location header

## /add_word (GET)

**Test** 🟥
```python
def test_add_word_get(client, logged_in_user):
    response = client.get("/add_word")
    assert response.status_code == 200
```

**Checks** 🟩

1- Authenticated user can load add-word form

2- Page returns 200

## /add_word (POST)

**Test** 🟥
```python
def test_add_word_post(client, logged_in_user, new_word_data):
    response = client.post("/add_word", data=new_word_data, follow_redirects=True)
    assert response.status_code == 200
    assert b"New word added successfully!" in response.data
    # DB check
    word = Word.query.filter_by(japanese=new_word_data["japanese"]).first()
    assert word is not None
```

**Checks** 🟩

1- Form submission creates a Word in DB

2- Success flash message displayed

3- Redirects after successful POST

## /edit_word/<id> (GET)

**Test** 🟥
```python
def test_edit_word_get(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word); db.session.commit()
    response = client.get(f"/edit_word/{word.id}")
    assert response.status_code == 200
    assert b"form" in response.data
```

**Checks** 🟩

1- Edit form loads for owner

2- Response includes the form markup

## /edit_word/<id> (POST)

**Test** 🟥
```python
def test_edit_word_post(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word); db.session.commit()

    data = {"japanese": "編集済み", "english": "edited", "pronunciation": "henshuu"}
    response = client.post(f"/edit_word/{word.id}", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Word updated successfully!" in response.data

    updated_word = Word.query.get(word.id)
    assert updated_word.japanese == "編集済み"
```

**Checks** 🟩

1- POST updates DB record for owner

2- Success flash message shown

3- Data persisted in DB

/delete_word/<id> (GET)

**Test** 🟥
```python
def test_delete_word_get(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word); db.session.commit()
    response = client.get(f"/delete_word/{word.id}")
    assert response.status_code == 200
    assert b"Are you sure" in response.data or b"form" in response.data
```

**Checks** 🟩

1- Confirmation page loads for owner

2- Shows confirmation prompt or form

## /delete_word/<id> (POST)

**Test** 🟥
```python
def test_delete_word_post(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word); db.session.commit()

    response = client.post(f"/delete_word/{word.id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Word deleted successfully!" in response.data

    deleted_word = Word.query.get(word.id)
    assert deleted_word is None
```

**Checks** 🟩

1- POST deletes the word record (DB)

2- Success flash message displayed

3- Redirects after delete
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)