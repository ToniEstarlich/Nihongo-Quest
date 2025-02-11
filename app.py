from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the SQLAlchemy instance
db = SQLAlchemy()
db.init_app(app)  # Link SQLAlchemy to the Flask app

# Import models after db initialization
from models import word

@app.route('/')
def index():
    words = word.Word.query.all()
    return render_template("index.html", words=words)

@app.route('/quiz')
def quiz():
    words = word.Word.query.all()
    return render_template("quiz.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)
