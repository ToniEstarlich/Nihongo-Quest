import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from extensions import db
from models.task import TaskImagen
from forms import TaskImagenForm  # Import the form
from forms import DeleteImageForm 


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

# Dictionary route
@task_bp.route('/dictionary')
def dictionary():
    entries = TaskImagen.query.all()
    return render_template('task/dictionary.html', entries=entries)

# Delete image
@task_bp.route('/delete/<int:image_id>', methods=['GET', 'POST'])
def delete_image(image_id):
    image = TaskImagen.query.get_or_404(image_id)
    form = DeleteImageForm()

    if form.validate_on_submit():  # Ensure Flask-WTF CSRF validation
        image_path = os.path.join('static', image.image_path)
        if os.path.exists(image_path):
            os.remove(image_path)

        db.session.delete(image)
        db.session.commit()
        flash("Image deleted successfully!", "success")
        return redirect(url_for('task.dictionary'))

    return render_template('task/delete_image.html', image=image, form=form)  # Pass 'form' here


# Edit image
@task_bp.route('/edit/<int:image_id>', methods=['GET', 'POST'])
def edit_image(image_id):
    image = TaskImagen.query.get_or_404(image_id)
    form = TaskImagenForm(obj=image)

    if form.validate_on_submit():
        if form.image.data:  # If a new image is uploaded
            file = form.image.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                image.image_path = f'uploads/{filename}'  # Update the image path
        
        # Update other fields (even if no new image is uploaded)
        image.category = form.category.data
        image.japanese_word = form.japanese_word.data
        image.pronunciation = form.pronunciation.data

        db.session.commit()
        flash("Image updated successfully!", "success")
        return redirect(url_for('task.dictionary'))

    return render_template('task/edit_image.html', form=form, image=image)
