from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from models.word import Word
from flask_login import current_user
from sqlalchemy import or_

flashcards_bp = Blueprint("flashcards", __name__, url_prefix="/flashcard")


@flashcards_bp.route("/flashcards.html")
@login_required
def flashcards():
    words = Word.query.filter(
        or_(Word.user_id == current_user.id, Word.user_id == None)  # global words
    ).all()
    return render_template("flashcards/flashcards.html", words=words)


@flashcards_bp.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    card_id = request.args.get("card_id", 1, type=int)
    words = Word.query.filter(
        or_(
            Word.user_id == current_user.id,
            Word.user_id == None,  # public words what don't need use user_id
        )
    ).all()

    start_index = (card_id - 1) * 5
    selected_words = words[start_index : start_index + 5]
    feedback = {}

    if request.method == "POST":
        correct_answers = sum(
            1
            for word in selected_words
            if request.form.get(f"answer_{word.id}", "").strip().lower()
            == word.english.strip().lower()
        )
        total_questions = len(selected_words)

        if correct_answers == total_questions:
            flash("Perfect score! All answers are correct. 🎉", "success")
        elif correct_answers > 0:
            flash(f"{correct_answers} correct answers. Keep practicing! 💪", "warning")
        else:
            flash("No correct answers. Keep practicing! 💪", "danger")

        return redirect(url_for("flashcards.flashcards"))

    return render_template(
        "flashcards/quiz.html",
        selected_words=selected_words,
        card_id=card_id,
        feedback=feedback,
    )
