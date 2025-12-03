## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_image_translator.py
## /image_translator 
**Test** 🟥

- ``get_image_for_word`` returns full dict
```python
def test_get_image_for_word_returns_dict(app):
    with app.app_context():
        word = "cat"
        result = visual_module.get_image_for_word(word)
        assert isinstance(result, dict)
        for key in ["english", "japanese", "kana", "romaji", "image"]:
            assert key in result
            assert result["english"] == word
            assert isinstance(result["image"], str)
```

**Checks** 🟩

1- Returns a dictionary

2- Includes expected keys (english, japanese, kana, romaji, image)

3- English word is preserved

4- Image field is always a string

**Test** 🟥 ``get_image_for_word_empty_query`` empty query
```python
def test_get_image_for_word_empty_query(app):
    with app.app_context():
        result = visual_module.get_image_for_word("")
        assert isinstance(result, dict)
        assert result["english"] == ""
        for key in ["japanese", "kana", "romaji", "image"]:
            assert isinstance(result[key], str)
```
**Checks** 🟩

1- Handles empty input safely

2- Returns a valid dict

3- All fields remain strings

4- No crash or missing key when query is empty
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)