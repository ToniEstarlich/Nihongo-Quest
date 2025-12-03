## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_alphabet.py

### /alphabet/ (GET) — alphabet overview

**Test** 🟥
```python
def test_alphabet_home(client):
    res = client.get("/alphabet/")
    assert res.status_code == 200
    assert b"alphabet" in res.data.lower()
```

**Checks** 🟩

1- Alphabet overview page loads

2- Contains "alphabet" text

### /alphabet/hiragana (GET)

**Test** 🟥
```python
def test_hiragana_page(client):
    res = client.get("/alphabet/hiragana")
    assert res.status_code == 200
    assert b"hiragana" in res.data.lower()
```

**Checks** 🟩

1- Hiragana page loads successfully

2- Contains "hiragana" text

### /alphabet/katakana (GET)

**Test** 🟥
```python
def test_katakana_page(client):
    res = client.get("/alphabet/katakana")
    assert res.status_code == 200
    assert b"katakana" in res.data.lower()
```

**Checks** 🟩

1- Katakana page loads successfully

2- Contains "katakana" text

### /alphabet/kanji (GET)

**Test** 🟥
```python
def test_kanji_page(client):
    res = client.get("/alphabet/kanji")
    assert res.status_code == 200
    assert b"kanji" in res.data.lower()
```


**Checks** 🟩

1- Kanji page loads successfully

2- Contains "kanji" text
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)