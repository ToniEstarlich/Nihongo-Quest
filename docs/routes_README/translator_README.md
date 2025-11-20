## Comeback [README](../README.md)
# Routes/translator.py

### get_translation(text_en)
APIs
  - https://api.mymemory.translated.net/get
  - https://api.pexels.com/v1/search

**Purpose:** Translate English → Japanese, generate Kana/Romaji, and fetch a related image.

**Routes** 🟩
Used by:

/add_words → show translation form + result

/add_word_from_result → populate hidden fields for saving

Output Example 🟦
```python
{
  "english": "cat",
  "japanese": "猫",
  "kana": "ねこ",
  "romaji": "neko",
  "image": "https://images.pexels.com/..."
}
```


Summary:

1- Calls MyMemory API for translation.

2- Converts Japanese text to Kana & Romaji using pykakasi.

3- Fetches one image from Pexels API (fallback to placeholder).

### /search_translate_image :

**Models** 🟦  
  ```python
  class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String, nullable=False)
  ```
**Forms** 🟦 
  ```python
  class WordForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    ...
    submit = SubmitField("Add Word")

  class AddWordFromResultForm(FlaskForm):
    japanese = HiddenField()
    english = HiddenField()
    ...
    submit = SubmitField("Add Word")
  ```
**Routes** 🟩 
  ```python
  @translator_bp.route('/add_words')
  def word_lookup_page():
    ...
    return render_template('add_words/add_words.html', result=result, form=form, add_result_form=add_result_form)
  ```
**HTML** 🟧 
  ```html
    <form method="get" action="{{ url_for('translator.word_lookup_page') }}">
    <button type="submit">Translate</button>
  ``` 
**Jinja** ⬜
  ```html
     <img src="{{ result.image }}" class="img-fluid rounded-start" alt="{{ result.english }}">
     {{ result.japanese }}
     {{ result.kana }}
     {{ result.romaji }}
  ```

### /add_word_from_result ``(POST)``

**Models** 🟦  
  ```python
  class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String, nullable=False)
  ```
**Forms** 🟦 
  ```python
  class WordForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    ...
    submit = SubmitField("Add Word")

  class AddWordFromResultForm(FlaskForm):
    japanese = HiddenField()
    english = HiddenField()
    ...
    submit = SubmitField("Add Word")
  ```
**Routes** 🟩 
  ```python
  @translator_bp.route("/add_word_from_result", methods=["POST"])
  @login_required
  def add_word_from_result():
  ```
**HTML** 🟧 
  ```html
  <form method="post" action="{{ url_for('translator.add_word_from_result') }}">
  ``` 
**Jinja** ⬜
  ```html
  {{ add_result_form.hidden_tag() }}
  {{ add_result_form.japanese(value=result.japanese) }}
  {{ add_result_form.english(value=result.english) }}
  {{ add_result_form.pronunciation(value=result.romaji) }}
  ```
  ## Comeback [README](../README.md)