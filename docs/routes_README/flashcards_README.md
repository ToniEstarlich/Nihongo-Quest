## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)
# routes/flashcards_routes.py

**Purpose:** Display flashcards and run quizzes with score feedback.
### /flashcards.html
**Models** 🟦  
  ```python
  class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String, nullable=False)
    english = db.Column(db.String, nullable=False)
    ...
  ```
**Routes** 🟩 
  ```python
  @flashcards_bp.route("/flashcards.html")
  @login_required
  def flashcards():
    words = Word.query.filter()...
    return render_template("flashcards/flashcards.html", words=words)
  ```
**HTML** 🟧 **Jinja** ⬜

jinja create a loop card and separate in 5 words for card
  ```html
  {% for i in range(0, words|length, 5) %}
            <div class="flashcard">
                <h3>Card {{ loop.index }}</h3>
                <ul>
                    {% for word in words[i:i+5] %}
                        <li>
                            <h6><strong>{{ word.japanese }}</strong> - <b class="word-english">{{ word.english }}</b>
                            {% if word.pronunciation %}
                                <br> {{ word.pronunciation }}</h6>
                            {% endif %}
                        </li>
                    {% endfor %}
                </ul>
                <a href="{{ url_for('flashcards.quiz', card_id=loop.index) }}" class="quiz-btn">Start Quiz</a>
            </div>
{% endfor %}
  ``` 

### /quiz

**Routes** 🟩 
  ```python
  @flashcards_bp.route("/quiz", methods=["GET","POST"])
  @login_required
  def quiz():
    card_id = request.args.get('card_id', 1, type=int)
    ...
    return render_template("flashcards/quiz.html", selected_words=selected_words, card_id=card_id)
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  <form action="{{ url_for('flashcards.quiz', card_id=card_id) }}" method="POST">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    
    {% for word in selected_words %}
        <div class="flashcard">
            <h3><strong>"{{ word.japanese }}"</strong></h3>
            <input type="text" name="answer_{{ word.id }}"
            class="flashcard-input {% if feedback and feedback[word.id] == 'correct' %}correct{% elif feedback and feedback[word.id] == 'incorrect' %}incorrect{% endif %}">
        </div>
    {% endfor %}
    
    <button type="submit" class="quiz-btn">Submit</button>
</form>
  ``` 

**summary:**

1- Quiz shows 5 words per page (controlled by card_id query param).

2- On POST, compares submitted answers to word.english (case-insensitive).

3- Flashes feedback:

- all correct → success,

- some correct → warning,

- none correct → danger.

4- Redirects back to the flashcards list after submission.
## Comeback [README](../../README.md#nihongo-quest--routes-functions--tests-overview)