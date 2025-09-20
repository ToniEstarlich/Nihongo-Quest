
from extensions import db

# Define the Hiragana table
class Hiragana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(5), nullable=False)
    romaji = db.Column(db.String(10), nullable=False)
    pronunciation = db.Column(db.String(100), nullable=False)  # Added pronunciation
    meaning = db.Column(db.String(100))

    def __repr__(self):
        return f'<Hiragana {self.character}>'
    
# Define the Katakana table
class Katakana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(5), nullable=False)
    romaji = db.Column(db.String(10), nullable=False)
    pronunciation = db.Column(db.String(100), nullable=False)  # Added pronunciation
    meaning = db.Column(db.String(100))

    def __repr__(self):
        return f'<Katakana {self.character}>'
    
# Define the Kanji table
class Kanji(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(10), nullable=False)
    onyomi = db.Column(db.String(100), nullable=False)  # Chinese reading
    kunyomi = db.Column(db.String(100), nullable=True)  # Japanese reading
    meaning = db.Column(db.String(100))

    def __repr__(self):
        return f'<Kanji {self.character}>'