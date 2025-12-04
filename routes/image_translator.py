import os
import uuid
import requests
import pykakasi

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, Response, abort
from flask_login import current_user, login_required
from extensions import db
from models.image import Image
from forms import TaskImagenForm, DeleteImageForm

visual_bp = Blueprint('visual', __name__)

kks = pykakasi.kakasi()

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Pixels API Key from environment variable
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
PEXELS_KEY = os.environ.get("PEXELS_KEY")

# Search for an image related to an English word using Pexels API ---------------------------------

def get_image_for_word(text_en):
    headers = {"Authorization": PEXELS_KEY}
    image_url = f"https://via.placeholder.com/400x300?text={text_en}"

    try:
        pexels_resp = requests.get(
            "https://api.pexels.com/v1/search",
            params={"query": text_en, "per_page": 1},
            headers=headers,
            timeout=10
        )
        pexels_resp.raise_for_status()
        data = pexels_resp.json()
        if data.get("photos"):
            image_url = data["photos"][0]["src"]["medium"]
    except Exception as e:
        current_app.logger.warning(f"Pexels fetch failed for {text_en}: {e}")

    return {
        "english": text_en,
        "japanese": "",
        "kana": "",
        "romaji": "",
        "image": image_url
    }


@visual_bp.route('/search_translate_image', methods=['GET'])
@login_required
def search_translate_image():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', 'Object').strip() or 'Object'
    result = None

    if query:
        # 1) MyMemory translation (English -> Japanese)
        jp_text = ""
        try:
            resp = requests.post(
                "https://api.mymemory.translated.net/get",
                params={"q": query, "langpair": "en|ja"},
                timeout=10
            )
            resp.raise_for_status()
            data = resp.json()
            jp_text = data.get("responseData", {}).get("translatedText", "") or ""
        except Exception as e:
            current_app.logger.warning(f"MyMemory translation failed for {query}: {e}")
            jp_text = ""

        # convert to kana/romaji with pykakasi if available (kks defined elsewhere)
        kana = ""
        romaji = ""
        try:
            conv = kks.convert(jp_text or "")
            kana = "".join([item.get('hira', '') for item in conv]).strip()
            romaji = " ".join([item.get('hepburn', '') for item in conv]).strip()
        except Exception as e:
            current_app.logger.exception(f"pykakasi conversion failed for '{jp_text}': {e}")
            kana = ""
            romaji = ""

        # 2) Pexels image (single)
        headers = {"Authorization": PEXELS_KEY}
        image_url = f"https://via.placeholder.com/400x300?text={query}"
        try:
            resp = requests.get(
                "https://api.pexels.com/v1/search",
                params={"query": f"{query} {category}", "per_page": 1},
                headers=headers,
                timeout=10
            )
            resp.raise_for_status()
            data = resp.json()
            photo = (data.get("photos") or [None])[0]
            if photo:
                # use original for download/save, medium for display if you prefer
                image_url = photo.get("src", {}).get("original") or photo.get("src", {}).get("medium")
        except Exception as e:
            current_app.logger.warning(f"Pexels fetch failed for {query}: {e}")
            image_url = f"https://via.placeholder.com/400x300?text={query}"

        result = {
            "english": query,
            "japanese": jp_text,
            "kana": kana,
            "romaji": romaji,
            "image": image_url,
            "category": category
        }

    form = TaskImagenForm()
    return render_template('add_images/add_image.html', form=form, result=result, query=query, category=category)


# add and download image from results -----------------------------------
def download_image_to_uploads(url, suggested_ext=None, timeout=10):

    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
    except Exception as e:
        current_app.logger.error(f"Failed to download image from {url}: {e}")
        return None, None, None

    # Determine extension 
    content_type = resp.headers.get('Content-Type', '').lower()
    ext = 'jpg'
    if 'png' in content_type:
        ext = 'png'
    elif 'gif' in content_type:
        ext = 'gif'
    elif 'jpeg' in content_type or 'jpg' in content_type:
        ext = 'jpg'
    elif suggested_ext:
        ext = suggested_ext.strip('.')

    # Ensure upload folder exists (absolute path)
    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.{ext}"
    filepath = os.path.join(upload_folder, filename)
    try:
        with open(filepath, "wb") as f:
            f.write(resp.content)
    except Exception as e:
        current_app.logger.error(f"Failed to write image to disk: {e}")
        return None, None, None
    
    return f"uploads/{filename}", resp.content, resp.headers.get('Content-type')


@visual_bp.route('/add_image_from_result', methods=['POST'])
@login_required
def add_image_from_result():
    image_url = request.form.get("image_url", "").strip()
    japanese_word = request.form.get("japanese", "").strip() or request.form.get("japanese_word", "").strip()
    english_word = request.form.get("english", "").strip()
    pronunciation = request.form.get("pronunciation", "").strip()
    category = request.form.get("category", "Object").strip() or "Object"

    if not image_url:
        flash("Missing image URL.")
        return redirect(url_for('translator.word_lookup_page', q=english_word or japanese_word))

    if not japanese_word:
        # fallback: if translation didn't provide japanese, store english as japanese_word
        japanese_word = english_word or ""

    saved_rel_path, img_data, content_type = download_image_to_uploads(image_url)
    if not saved_rel_path:
        flash("Failed to download/save the image.")
        return redirect(url_for('translator.word_lookup_page', q=english_word or japanese_word))

    try:
        new_entry = Image(
            image_path=saved_rel_path,
            category=category,
            japanese_word=japanese_word,
            pronunciation=pronunciation or "",
            user_id=current_user.id,
            data=img_data,
            content_type=content_type
        )
        db.session.add(new_entry)
        current_app.logger.debug(f"About to commit Image entry: {new_entry}")
        db.session.commit()
        current_app.logger.debug(f"Save image entry id={new_entry.id} path={new_entry.image_path}")
    except Exception as e:
        current_app.logger.exception(f"Failed to save image entry to DB: {e}")
        try:
            full_path = os.path.join(current_app.root_path, 'static', saved_rel_path)
            if os.path.exists(full_path):
                os.remove(full_path)
        except Exception:
            current_app.logger.exception("Failed to remove downloaded file after database error")
        flash("Failed to save image entry to database.")
        return redirect(url_for('visual.search_translate_image', q=english_word or japanese_word))

    flash("Image added from result successfully!", "success")
    return redirect(url_for('image.image_list'))

@visual_bp.route("/image/<int:image_id>")
def serve_image(image_id):
    img = Image.query.get(image_id)
    if not img:
        abort(404)
    if img.data:
        return Response(img.data, mimetype=img.content_type or "image/jpeg")
    return redirect(url_for('static', filename=img.image_path))