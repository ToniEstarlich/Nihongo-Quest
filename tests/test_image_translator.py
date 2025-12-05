import pytest
from flask import Flask
import routes.image_translator as visual_module


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    # Configure PEXEL API
    app.config["PEXEL_API_KEY"] = "FAKE_KEY"
    return app


def test_get_image_for_word_returns_dict(app):
    with app.app_context():
        word = "cat"
        result = visual_module.get_image_for_word(word)
        assert isinstance(result, dict)
        for key in ["english", "japanese", "kana", "romaji", "image"]:
            assert key in result
            assert result["english"] == word
            assert isinstance(result["image"], str)


def test_get_image_for_word_empty_query(app):
    with app.app_context():
        result = visual_module.get_image_for_word("")
        assert isinstance(result, dict)
        assert result["english"] == ""
        for key in ["japanese", "kana", "romaji", "image"]:
            assert isinstance(result[key], str)
