## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)

# | Routes/image_routes.py
- **/task/** add **(GET & POST)**

- **Purpose:** Add a new image via form manual.

**Blueprint:** ``image_bp``

**Upload folder:** ``static/uploads``

**Allowed file types:** ``png, jpg, jpeg, gif``

### **C**reate 🟢⇩

**Models** 🟦  
  ```python
  class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String, nullable=False)
    ...
  ```
**Forms** 🟦 
  ```python
  class TaskImagenForm(FlaskForm):
    image = FileField("Upload Image", validators=[FileAllowed(['jpg','png','jpeg','gif'], "Images only!")])
    japanese_word = StringField("Japanese Word")
    ...
  ```
**Routes** 🟩 
  ```python
  @image_bp.route('/task/add', methods=['GET', 'POST'])
  @login_required
  def add_image():
  ...
  ```
**HTML** 🟧 
  ```html
  <form method="POST" enctype="multipart/form-data" action="{{ url_for('image.add_image') }}">
  ``` 
**Jinja** ⬜
  ```html
    {{ form.hidden_tag() }}
    {{ form.image() }}
    {{ form.japanese_word() }}
    {{ form.pronunciation() }}
    {{ form.category() }}
    {{ form.submit() }}
  ```
  ### **R**ead 🟢⇩
  / (GET) → ``Image list``

**Purpose:** List all images uploaded by the current user.
**Routes** 🟩 
  ```python
 @image_bp.route('/')
@login_required
def image_list():
    entries = Image.query.filter_by(user_id=current_user.id).all()
    return render_template('add_images/image_list.html', entries=entries)

  ```
**HTML** 🟧 
**Jinja** ⬜
  ```html
  {% for entry in entries %}
  <img src="{{ url_for('static', filename=entry.image_path) }}" alt="{{ entry.japanese_word }}">
  <p>{{ entry.japanese_word }} ({{ entry.pronunciation }})</p>
  <a href="{{ url_for('image.edit_image', image_id=entry.id) }}">Edit</a>
  <a href="{{ url_for('image.delete_image', image_id=entry.id) }}">Delete</a>
  {% endfor %}
  ```

   ### **D**elete 🟢⇩
  **/delete/** int:image_id
 **(GET & POST)**

**Purpose:** Delete a user’s image.
**Forms** 🟦 
  ```python
  class DeleteImageForm(FlaskForm):
    submit = SubmitField("Delete")
  ```
**Routes** 🟩 
  ```python
  @image_bp.route('/delete/<int:image_id>', methods=['GET','POST'])
  @login_required
  def delete_image(image_id):
   ...
  ```
**HTML** 🟧  
**Jinja** ⬜
  ```html
<p>Are you sure you want to delete {{ image.japanese_word }}?</p>
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.submit() }}
</form>
  ```

 ### **U**pdate 🟢⇩
**/edit/** int:image_id
 **(GET & POST)**

**Purpose:** Edit image metadata (category, Japanese word, pronunciation).

**Routes** 🟩 
  ```python
  @image_bp.route('/edit/<int:image_id>', methods=['GET','POST'])
  @login_required
  def edit_image(image_id):
 ...
 
  ```
**HTML** 🟧  
**Jinja** ⬜
  ```html
  <form method="POST">
    {{ form.hidden_tag() }}
    {{ form.japanese_word() }}
    {{ form.pronunciation() }}
    {{ form.category() }}
    {{ form.submit() }}
</form>
  ```

  **Description:**

1- Loads existing image data into the form.

2- Validates on submission.

3- Updates the DB entry.

4- Redirects to the image list with a flash message.

## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)