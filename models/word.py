#from app import db
from flask import current_app
from extensions import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    pronunciation = db.Column(db.String(100))

    def __repr__(self):
        return f"<Word {self.japanese} - {self.english} - Pronunciation: {self.pronunciation}>"
