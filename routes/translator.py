from flask import Blueprint, request, jsonify, current_app, redirect, url_for, render_template
import requests
import pykakasi

translator_bp = Blueprint('translator', __name__, template_folder='templates')
kks = pykakasi.kakasi()

def get_translation(text_en):
    jp_text = ""
    try:
        resp = requests.post(
            "https://api.mymemory.translated.net/get",
            params={"q": text_en, "langpair": "en|ja"},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        jp_text = data.get("responseData", {}).get("translatedText", "")
    except Exception as e:
        jp_text = "ERROR: Translation failed"

    conv = kks.convert(jp_text or "")
    reading_kana = "".join([item.get('hira', '') for item in conv]).strip()
    reading_romaji = " ".join([item.get('hepburn', '') for item in conv]).strip()
    image_url = f"https://source.unsplash.com/400x300/?{text_en}"

    return {
        "english": text_en,
        "japanese": jp_text,
        "kana": reading_kana,
        "romaji": reading_romaji,
        "image": image_url
    }


@translator_bp.route('/word_lookup')
def word_lookup_page():
    word = request.args.get('q')
    result = get_translation(word) if word else None
    return render_template('word_lookup.html', result=result)

