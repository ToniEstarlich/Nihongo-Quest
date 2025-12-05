import os

# foms.py
from forms import WordForm, DeleteWordForm, AddWordFromResultForm

# translator.py
from urllib.parse import quote
from flask import (
    Blueprint,
    request,
    jsonify,
    current_app,
    redirect,
    url_for,
    render_template,
    flash,
)
from forms import WordForm, DeleteWordForm
import requests
import pykakasi

# Pixels API Key from environment variable
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
PEXELS_KEY = os.environ.get("PEXELS_KEY")

# For CRUD operations on Word model
from flask_login import login_required, current_user
from models.word import Word
from extensions import db

translator_bp = Blueprint("translator", __name__, template_folder="templates")
kks = pykakasi.kakasi()

# Helper function: English → Japanese translation + Kana + Romaji + Image


def get_translation(text_en):
    jp_text = ""
    try:
        resp = requests.post(
            "https://api.mymemory.translated.net/get",
            params={"q": text_en, "langpair": "en|ja"},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        jp_text = data.get("responseData", {}).get("translatedText", "")
    except Exception as e:
        current_app.logger.exception("Translation failed")
        jp_text = ""

    conv = kks.convert(jp_text or "")
    reading_kana = "".join([item.get("hira", "") for item in conv]).strip()
    reading_romaji = " ".join([item.get("hepburn", "") for item in conv]).strip()

    # --- Pexels API Integration ---
    headers = {"Authorization": PEXELS_KEY}
    image_url = f"https://via.placeholder.com/400x300?text={quote(text_en)}" # fallback
    try:
        pexels_resp = requests.get(
            "https://api.pexels.com/v1/search",
            params={"query": text_en, "per_page": 1},
            headers=headers,
            timeout=10,
        )
        pexels_resp.raise_for_status()
        data = pexels_resp.json()
        if data["photos"]:
            image_url = data["photos"][0]["src"]["medium"]
    except Exception as e:
        current_app.logger.warning(f"Pexels fetch failed for {text_en}: {e}")

    return {
        "english": text_en,
        "japanese": jp_text,
        "kana": reading_kana,
        "romaji": reading_romaji,
        "image": image_url,
    }


# Show all words added by the current user.
@translator_bp.route("/words")
@login_required
def words():

    user_words = Word.query.filter_by(user_id=current_user.id).all()
    current_app.logger.debug(
        f"User {current_user.id} words: {[w.japanese for w in user_words]}"
    )
    return render_template("add_words/words.html", words=user_words)


# Main translation page (with form and lookup feature)
@translator_bp.route("/add_words")
def word_lookup_page():
    word = request.args.get("q")
    result = get_translation(word) if word else None
    form = WordForm()
    add_result_form = AddWordFromResultForm()
    return render_template(
        "add_words/add_words.html",
        result=result,
        form=form,
        add_result_form=add_result_form,
    )


# CRUD for Words integrated into translator blueprint
@translator_bp.route("/add_word_from_result", methods=["POST"])
@login_required
def add_word_from_result():
    japanese = request.form.get("japanese", "").strip()
    english = request.form.get("english", "").strip()
    pronunciation = request.form.get("pronunciation", "").strip()

    if not japanese or not english:
        flash("Missing word data.", "danger")
        return redirect(url_for("translator.word_lookup_page", q=english))

    new_word = Word(
        japanese=japanese,
        english=english,
        pronunciation=pronunciation or None,
        user_id=current_user.id,
    )

    db.session.add(new_word)
    db.session.commit()
    flash("New word added from result!", "success")
    return redirect(url_for("translator.words"))
