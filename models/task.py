from extensions import db

class TaskImagen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    japanese_word = db.Column(db.String(100), nullable=False)
    pronunciation = db.Column(db.String(100), nullable=False) 

    
    def __init__(self, image_path, category, japanese_word, pronunciation):
        self.image_path = image_path
        self.category = category
        self.japanese_word = japanese_word
        self.pronunciation = pronunciation