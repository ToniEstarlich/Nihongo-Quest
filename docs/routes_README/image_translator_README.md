## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# Routes/image_translator.py

### /search_translate_image :
APIs
  - https://api.mymemory.translated.net/get
  - https://api.pexels.com/v1/search

**Models** 🟦  
  ```python
  class Image(db.Model):
    __tablename__ = 'task_imagen'
  ```
**Forms** 🟦  
  ```python
  class TaskImagenForm(FlaskForm):
    image_url = StringField("Image URL", validators=[Optional()])
     # add url imagen from Pexel
  ```  
**Routes** 🟩 

Displays the search form and result images.
 ```python
    @visual_bp.route('/search_translate_image', methods=['GET'])
    @login_required
    def search_translate_image():
 ```

```python
form = TaskImagenForm()
    return render_template('add_images/add_image.html', form=form, result=result, query=query, category=category)
```
**HTML** 🟧 

```html
<form method="get" action="{{ url_for('visual.search_translate_image') }}">...
```

**Jinja** ⬜
```html
{{ form.japanese_word() }}
{{ form.category() }}
{{ result.english }}
{{ result.japanese }}
{{ result.kana }}
{{ result.romaji }}
```

**Description:**

1- Receives a query string (q) and optional category.

2- Translates the English word to Japanese via MyMemory API.

3- Converts Japanese text to Kana/Romaji using pykakasi.

4- Retrieves an image using the Pexels API.

5- Renders the template with the form and search results.

### /add_image_from_result (POST) :

- **Purpose:** Add a new image from results.

**Models** 🟦  
  ```python
  class Image(db.Model):
    __tablename__ = 'task_imagen'
  ```
  - Stores images with Japanese/English words, category, pronunciation, user ID, raw data, and content type.

**Forms** 🟦  
  ```python
  class TaskImagenForm(FlaskForm):
    image_url = StringField("Image URL", validators=[Optional()])
     # add url imagen from Pexel
  ```
  -  TaskImagenForm (indirectly, receives POST data)

**Routes** 🟩 
  ```python
  @visual_bp.route('/add_image_from_result', methods=['POST'])
  @login_required
  def add_image_from_result():
  ...
  ```
**HTML** 🟧 
  ```html
  <form method="post" action="{{ url_for('visual.add_image_from_result') }}">
  ``` 
**Jinja** ⬜

 Receives request.form data:
  ```html
            {{ form.hidden_tag() }}
            {{ form.image_url(value=result.image, type="hidden") }}
            {{ form.japanese_word(value=result.japanese or result.english, type="hidden") }}
            {{ form.pronunciation(value=result.romaji, type="hidden") }}
            {{ form.category(value=result.category, type="hidden") }}
            {{ form.submit(class="btn btn-success mt-2") }}
  ```

**Description:**

1- Downloads the image from the result URL.

2- Saves the image file in static/uploads.

3- Creates a new Image record in the database.

4- Redirects with flash messages depending on success/failure.
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)