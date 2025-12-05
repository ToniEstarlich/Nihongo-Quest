from flask import Blueprint, render_template
from extensions import db  # Import db from db.py
from models.alphabet import Hiragana, Katakana, Kanji  # Import models

# Define Blueprint
alphabet_bp = Blueprint("alphabet", __name__, url_prefix="/alphabet")


# Route for the main overview page
@alphabet_bp.route("/")
def alphabet():
    return render_template("alphabet/alphabet.html")


# Route for Hiragana page
@alphabet_bp.route("/hiragana")
def hiragana():
    # Query all Hiragana characters from the database
    hiragana_characters = Hiragana.query.all()
    return render_template("alphabet/hiragana.html", characters=hiragana_characters)


# Route for Katakana page
@alphabet_bp.route("/katakana")
def katakana():
    # Query all Katakana characters from the database
    katakana_characters = Katakana.query.all()
    return render_template("alphabet/katakana.html", characters=katakana_characters)


# Route for Kanji page
@alphabet_bp.route("/kanji")
def kanji():
    # Query all Kanji characters from the database
    kanji_characters = Kanji.query.all()
    return render_template("alphabet/kanji.html", characters=kanji_characters)
