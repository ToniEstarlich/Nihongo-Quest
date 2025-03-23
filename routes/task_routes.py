import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from extensions import db
from models.task import TaskImagen
from forms import TaskImagenForm  # Import the form

task_bp = Blueprint('task', __name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@task_bp.route('/add', methods=['GET', 'POST'])
def add_image():
    form = TaskImagenForm()

    if form.validate_on_submit():
        file = form.image.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)  # Save to static/uploads
            file.save(filepath)

            new_entry = TaskImagen(
                image_path=f'uploads/{filename}',  # Save relative path
                category=form.category.data,
                japanese_word=form.japanese_word.data,
                pronunciation=form.pronunciation.data
            )

            db.session.add(new_entry)
            db.session.commit()
            flash("New entry added successfully!", "success")
            return redirect(url_for('task.add_image'))

    return render_template('task/add_image.html', form=form)  # Pass form to template

@task_bp.route('/dictionary')
def dictionary():
    entries = TaskImagen.query.all()
    return render_template('task/dictionary.html', entries=entries)



@task_bp.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    entry = TaskImagen.query.get(entry_id)

    if request.method == 'POST':
        entry.category = request.form['category']
        entry.japanese_word = request.form['japanese_word']
        entry.pronunciation = request.form['pronunciation']

        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join('static/uploads', filename)  # Save to static/uploads
                file.save(filepath)
                entry.image_path = f'uploads/{filename}'  # Relative path

        db.session.commit()
        flash('Entry updated successfully!')
        return redirect(url_for('task.get_all_images'))

    return render_template('task/edit.html', entry=entry)  # Updated path


@task_bp.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = TaskImagen.query.get(entry_id)
    if entry:
        if os.path.exists(entry.image_path):
            os.remove(entry.image_path)

        db.session.delete(entry)
        db.session.commit()
        flash('Entry deleted successfully!')

    return redirect(url_for('task.get_all_images'))                  