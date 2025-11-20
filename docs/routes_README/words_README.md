## Comeback [README](../README.md)
---
# Routes/words_routes.py

Description (CRUD manual words):

1-  Lists all words saved by the current user.

2-  Validates and saves a new word from the manual form.

3-  Loads an existing word, updates fields, and commits changes.

4-  Confirms delete action and removes the entry from the database.

---
### **R**ead 🟢⇩
### /words:
**Purpose:** List all words added manually by the current user.

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
  ```
**Routes** 🟩 
  ```python
  @words_bp.route("/words")
  @login_required
  def words():
    ...
    return render_template("add_words/words.html", words=words)
  ```
**HTML** 🟧  **Jinja** ⬜
```html
<ul>
 {% for word in words %}
  <li>{{ word.japanese }} ({{ word.english }}) - {{ word.pronunciation }}</li>
  <button class="btn btn-delete"
         onclick="window.location.href='{{ url_for('words.delete_word', word_id=word.id) }}'">
         <i class="fas fa-trash"></i> Delete 
 </button> 
 {% endfor %}
</ul>
 ```
 ---
### **C**reate 🟢⇩
### /add_word
**Routes** 🟩 
  ```python
    @words_bp.route("/add_word", methods=["GET","POST"])
    @login_required
    def add_word():
    ...
  ```
**HTML** 🟧 
  ```html
  <form method="post" action="{{ url_for('translator.add_word') }}">
  ``` 
**Jinja** ⬜
  ```html
       {{ form.hidden_tag() }}

       {{ form.english(class="form-control") }}

       {{ form.japanese(class="form-control") }}

       {{ form.pronunciation(class="form-control") }}

       {{ form.submit(class="btn btn-primary mt-3") }}
  ```
---
### **U**pdate 🟢⇩
### /edit_word
**Routes** 🟩 
  ```python
  @words_bp.route("/edit_word/<int:word_id>", methods=["GET","POST"])
  @login_required
  def edit_word(word_id):
    ...
    return render_template("add_words/edit_word.html", form=form, word=word)
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  <form method="POST">
        {{ form.hidden_tag() }}
        <label for="japanese">Japanese:</label>
        {{ form.japanese(class="form-control") }}
    
        <label for="english">English:</label>
        {{ form.english(class="form-control") }}
    
        <label for="pronunciation">Pronunciation:</label>
        {{ form.pronunciation(class="form-control") }}
    
        <button type="submit" class="button">Update Word</button>
   </form>
  ``` 
---
### **D**elete 🟢⇩
### /delete_word
**Forms** 🟦 
  ```python
  class DeleteWordForm(FlaskForm):
    submit = SubmitField("Delete")
  ```
**Routes** 🟩 
  ```python
   @words_bp.route("/delete_word/<int:word_id>", methods=["GET","POST"])
   @login_required
   def delete_word(word_id):
  ...
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  <form method="POST" action="{{ url_for('words.delete_word', word_id=word.id) }}">
        {{ form.hidden_tag() }}
  <button type="submit" class="btn btn-danger">Delete</button>
  ``` 



## Comeback [README](../README.md)