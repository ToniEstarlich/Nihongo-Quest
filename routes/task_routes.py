import os 
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, TaskImagen

task_bp = Blueprint('task', __name__)

UPLOAD_FOLDER = 'satatic/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@task_bp.route('/add', methods=['GET', 'POST'])
def add_image():
    if request.method == 'POST':
        category = request.form['category']
        japanese_word = request.form['japanese_word']
        pronunciation = request.form['pronunciation']
        file = request.files['image']

        if file and allowed_file(file.filename): # the helper function
           filename = secure_filename(file.filename)
           filepath = os.path.join(UPLOAD_FOLDER, filename)
           file.save(filepath)

           new_entry = TaskImagen(
            image_path=filepath,
            category=category,
            japanese_word=japanese_word,
            pronunciation=pronunciation
           )
           db.session.add(new_entry)
           db.session.commit()
           flash('New entry added!')
           return redirect(url_for('task.get_all_images'))
    
    return render_template('add_image.html')

@task_bp.route('/list')
def get_all_images():
    entries = TaskImagen.query.all()
    return render_template('dictionary.html', entries=entries)

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
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                entry.image_path = filepath

        db.session.commit()
        flash('Entry updated successfully!')
        return redirect(url_for('task.get_all_images'))
    return render_template('edit.html', entry=entry)

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