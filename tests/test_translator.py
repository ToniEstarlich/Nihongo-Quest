import pytest
from flask import Flask
import routes.translator as translator_module

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING']= True
    # blueprint registration and other setup can go here if needed
    app.register_blueprint(translator_module.translator_bp)
    return app

@pytest.fixture
def cliente(app):
    return app.test_client()

# Helpers // Mocks

class DummyResponse:
    def __inint__(self, data=None, raise_exc=False):
        self.data = data or {}
        self.raise_exc = raise_exc

    def raise_for_status(self):
        if self.raise_exc:
            raise Exception("HTTP Error simulated")
        
    def json(self):
        return self._data
    

def test_get_translation_returns_dict(app):
    with app.app_context():
        result = translator_module.get_translation("cat")
        assert isinstance(result, dict)
        for key in ["english", "japanese", "kana", "romaji", "image"]:
            assert key in result

def test_get_translation_handles_empty(app):
    with app.app_context():
        result = translator_module.get_translation("")
        assert isinstance(result, dict)
        assert result["english"] == ""
        assert isinstance(result["japanese"], str)
        assert isinstance(result["kana"], str)
        assert isinstance(result["romaji"], str)
        assert isinstance(result["image"], str)
       