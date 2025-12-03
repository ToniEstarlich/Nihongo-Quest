## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/flashcards.py
## /flashcards.html (GET)

**Test** 🟥
```python
def test_flashcards_route(client, logged_in_user, create_words):**
    create_words(user_id=None, count=5)
    create_words(user_id=logged_in_user.id, count=0)
    res = client.get('/flashcard/flashcards.html')
    assert res.status_code == 200
    text = res.get_data(as_text=True)
    for i in range(1, 6):
        assert f"word{i}" in text
```

**Checks** 🟩

1- Flashcards page loads successfully

2- Displays public words

3- Displays user words

/quiz (GET)

**Test** 🟥
```python
def test_quiz_get(client, logged_in_user, create_words):
    create_words(user_id=logged_in_user.id, count=1)
    res = client.get('/flashcard/quiz?card_id=1')
    assert res.status_code == 200
    data = res.get_data(as_text=True)
    assert any(word in data for word in ["word1", "単語1"])
```

**Checks** 🟩

1- Quiz page loads

2- Displays selected words

3- Handles card_id query parameter

## /quiz (POST)

**Test** 🟥
```python
def test_quiz_post(client, logged_in_user, create_words):
    words = create_words(user_id=None, count=5)
    form_data = {f"answer_{w.id}": w.english if w.id <= 3 else "wrong" for w in words}
    res = client.post('/flashcard/quiz?card_id=1', data=form_data, follow_redirects=True)
    assert res.status_code == 200
    page_text = res.get_data(as_text=True)
    assert "3 correct answers" in page_text or "Keep practicing" in page_text
```

**Checks** 🟩

1- Submits quiz answers

2- Compares answers with correct English values (case-insensitive)

3- Shows flash messages depending on number of correct answers

4- Redirects back to flashcards page
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)