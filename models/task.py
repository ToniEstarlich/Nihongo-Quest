from extensions import db

class TaskImagen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    japanese_word = db.Column(db.String(100), nullable=False)
    pronunciation = db.Column(db.String(100), nullable=False) 