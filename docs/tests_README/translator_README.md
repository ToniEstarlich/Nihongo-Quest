## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# tests/test_translator.py
## get_translation — normal input
**Tes**t 🟥
```python
def test_get_translation_returns_dict(app):
    with app.app_context():
        result = translator_module.get_translation("cat")
        assert isinstance(result, dict)
        for key in ["english", "japanese", "kana", "romaji", "image"]:
            assert key in result
```
**Checks** 🟩

1- Function returns a dictionary

2-  All expected fields are present

3- Handles normal input without errors

4- Returns image placeholder or generated URL

## get_translation — empty input
**Test** 🟥
```python
def test_get_translation_handles_empty(app):
    with app.app_context():
        result = translator_module.get_translation("")
        assert isinstance(result, dict)
        assert result["english"] == ""
        assert isinstance(result["japanese"], str)
        assert isinstance(result["kana"], str)
        assert isinstance(result["romaji"], str)
        assert isinstance(result["image"], str)
```
**Checks** 🟩

1- Handles empty string safely

2- Returns a valid dict instead of crashing

3- All values are still strings

4- Ensures API logic degrades gracefully
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)