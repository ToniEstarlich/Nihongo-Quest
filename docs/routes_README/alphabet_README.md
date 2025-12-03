## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# routes/alphabet_routes.py
**Blueprint:** ``alphabet_bp`` ``(url_prefix="/alphabet")``
**Purpose:** Serve pages with the Japanese alphabets (Hiragana, Katakana) and a Kanji overview, reading data from the DB.

```render_template``` injects the Hiragana, Katakana, or Kanji data into their respective HTML templates.

### / (GET)- Alphabet overview 
**Routes** 🟩 
  ```python
  @alphabet_bp.route('/')
  def alphabet():
    return render_template('alphabet/alphabet.html')
  ```
  **Description**: Simple index/landing page that links to the three alphabet sections.
  ### /hiragana (GET)
  
**Models** 🟦  
  ```python
  class Hiragana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(5), nullable=False)
    ...
    def __repr__(self):
        return f'<Hiragana {self.character}>'
  ```
**Routes** 🟩 
  ```python
  @alphabet_bp.route('/hiragana')
  def hiragana():
    hiragana_characters = Hiragana.query.all()
    return render_template('alphabet/hiragana.html', characters=hiragana_characters)
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  {% for character in characters %}
            <div class="alphabet-card">
                <div class="character">{{ character.character }}</div>
                <div class="meaning">{{ character.meaning }}</div>
                <div class="romaji">{{ character.romaji }}</div>
            </div>
  {% endfor %}
  ``` 
  ### /katakana (GET)
    
**Models** 🟦  
  ```python
  class Katakana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(5), nullable=False)
    ...
    def __repr__(self):
        return f'<Katakana {self.character}>'
  ```
**Routes** 🟩 
  ```python
  @alphabet_bp.route('/katakana')
  def katakana():
    katakana_characters = Katakana.query.all()
    return render_template('alphabet/katakana.html', characters=katakana_characters)
  ```
**HTML** 🟧**Jinja** ⬜ 
  ```html
  {% for character in characters %}
            <div class="alphabet-card">
                <div class="character">{{ character.character }}</div>
                <div class="meaning">{{ character.meaning }}</div>
                <div class="romaji">{{ character.romaji }}</div>
            </div>
  {% endfor %}
  ``` 
  ### /kanji (GET)
    
**Models** 🟦  
  ```python
  class Kanji(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(10), nullable=False)
    ...
    def __repr__(self):
        return f'<Kanji {self.character}>'
  ```
**Routes** 🟩 
  ```python
  @alphabet_bp.route('/kanji')
  def kanji():
    kanji_characters = Kanji.query.all()
    return render_template('alphabet/kanji.html', characters=kanji_characters)
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  {% for character in characters %}
            <div class="alphabet-card">
                <div class="character">{{ character.character }}</div>
                <div class="meaning">{{ character.meaning }}</div>
                <div class="romaji">{{ character.romaji }}</div>
            </div>
  {% endfor %}
  ``` 
  **Summary**

1- Each route queries its model (Hiragana, Katakana, Kanji) and renders a template.

2- Templates receive characters and loop to display symbol + readings + optional meaning.

3- Routes are public (no login_required) — ensure DB is seeded with kana/kanji data.

4- Consider DB pagination or caching if lists become large.
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)