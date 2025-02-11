from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Word {self.japanese} - {self.english}>"
