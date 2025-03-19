from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class TaskImagen(db.Model):
    __tablename__ = 'task_imagen'

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    japanese_word = db.Column(db.String(100), nullable=False)
    pronunciation = db.Column(db.String(100), nullable=False) 