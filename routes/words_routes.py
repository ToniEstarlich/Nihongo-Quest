
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.word import Word
from forms import WordForm, DeleteWordForm
from extensions import db

words_bp = Blueprint("words", __name__, template_folder="../../templates/add_words")

@words_bp.route("/words")
@login_required
def words():
    words = Word.query.filter_by(user_id=current_user.id).all()
    print(
         f"User {current_user.id} words: {[w.japanese for w in words]}"
    ) # for debugs
    return render_template("add_words/words.html", words=words)


@words_bp.route("/add_word", methods=["GET", "POST"])
@login_required
def add_word():
    form = WordForm()
    if request.method == "POST" and form.validate_on_submit():
        new_word = Word(
            japanese=form.japanese.data,
            english=form.english.data,
            pronunciation=form.pronunciation.data,
            user_id=current_user.id,
        )
        db.session.add(new_word)
        db.session.commit()
        flash("New word added successfully!", "success")
        return redirect(url_for("words.words"))
    return render_template("add_words/add_words.html", form=form)

@words_bp.route("/edit_word/<int:word_id>", methods=["GET", "POST"])
@login_required
def edit_word(word_id):
    word = Word.query.get_or_404(word_id)
    if word.user_id != current_user.id:
        flash("You are not authorized to edit this word.", "danger")
        return redirect(url_for("words.add_word"))

    form = WordForm(obj=word)
    if request.method == "POST" and form.validate_on_submit():
        word.japanese = form.japanese.data
        word.english = form.english.data
        word.pronunciation = form.pronunciation.data
        db.session.commit()
        flash("Word updated successfully!", "success")
        return redirect(url_for("words.add_word"))
    return render_template("add_words/edit_word.html", form=form, word=word)

@words_bp.route("/delete_word/<int:word_id>", methods=["GET", "POST"])
@login_required
def delete_word(word_id):
    word = Word.query.get_or_404(word_id)
    if word.user_id != current_user.id:
        flash("You are not authorized to delete this word.", "danger")
        return redirect(url_for("add_words/words.add_word"))

    form = DeleteWordForm()
    if request.method == "POST":
        db.session.delete(word)
        db.session.commit()
        flash("Word deleted successfully!", "success")
        return redirect(url_for("words.add_word"))
    return render_template("add_words/delete_word.html", word=word, form=form)