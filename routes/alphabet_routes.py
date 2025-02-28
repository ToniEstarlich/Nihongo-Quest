from flask import Flask, render_template
from db import db  # Import db from db.py
from models.alphabet import Hiragana, Katakana, Kanji  # Import models
import os

app = Flask(__name__)  # Define Flask app instance

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Toni2207@localhost/alphabet_japanese')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Ensure the tables are created
with app.app_context():
    db.create_all()

# Route for the main overview page
@app.route('/alphabet')
def alphabet():
    return render_template('alphabet/alphabet.html')

# Route for Hiragana page
@app.route('/hiragana')
def hiragana():
    # Query all Hiragana characters from the database
    hiragana_characters = Hiragana.query.all()
    return render_template('alphabet/hiragana.html', characters=hiragana_characters)

# Route for Katakana page
@app.route('/katakana')
def katakana():
    # Query all Katakana characters from the database
    katakana_characters = Katakana.query.all()
    return render_template('alphabet/katakana.html', characters=katakana_characters)

# Route for Kanji page
@app.route('/kanji')
def kanji():
    # Query all Kanji characters from the database
    kanji_characters = Kanji.query.all()
    return render_template('alphabet/kanji.html', characters=kanji_characters)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
