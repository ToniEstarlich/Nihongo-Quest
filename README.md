# Nihongo Quest   
<img src="./static/screenshots/nihongo_logo.png" alt="Mobile Screenshot" width="100">

Nihongo Quest is a Flask-based web application designed to help users learn Japanese vocabulary through interactive quizzes. Users can log in, take quizzes, and test their knowledge by answering questions about Japanese words.
![Website Preview](./static/screenshots/responsive.jpg)

##  - User Stories  

As a user:  

- create an account and log in so that I can track my progress and save my quiz results.  
- practice with flashcards so that I can memorize Japanese vocabulary more effectively.  
- take quizzes so that I can test my knowledge and receive feedback instantly.  
- explore manga and cultural sections so that learning Japanese feels fun and immersive.  
- the website to be responsive so that I can use it easily on desktop, tablet, and mobile devices.  

---

You can find the source code for **Nihongo Quest** in the GitHub repository below:  
- **Repository**: [Nihongo Quest GitHub Repository](https://github.com/ToniEstarlich/Nihongo-Quest)  

The live version of the project is accessible here:  
- **Live Project**: [Nihongo Quest](https://nihongo-quest-app-54ed3ed7b8f5.herokuapp.com/)  


## Table of Contents
1. [Tech Stack](#tech-stack)
2. [Wireframes](#wireframes)
3. [The Loggo](#the-logo)
4. [Colors](#colors)
5. [Screenshots](#uiux-screenshots)
6. [Nihongo Quest The process](#nihongo-quest---flask--postgresql-setup-guide-example)
7. [Problems & Solutions](#problems-and-solutions)
8. [Algorithm](#example-of-algorithm--code)

### Objective  
The goal of Nihongo Quest is to provide an engaging platform for learning Japanese vocabulary. The app allows users to take quizzes, track their progress, and improve their understanding of the language through repetition and interaction.


# Tech Stack  
# 🛠️

Nihongo Quest is built using a modern and reliable tech stack to ensure a smooth user experience and scalable performance.  

## 🎨 Style  
- **CSS** – Handles the layout and styling, ensuring a visually appealing and responsive design.  
- **Flexbox** & **Grid** – structuring content and creating a consistent layout across different screen sizes.  

## 🌐 Frontend  
- **HTML** – Provides the foundation for the content and structure of the web app.  
- **JavaScript** – Enables interactivity and dynamic content updates.  
- **Event Listeners** – handling user interactions like clicks and keyboard inputs.  

## 🚀 Backend
  - **Python** – The programming language used to build the backend logic.
- **[Flask](https://flask.palletsprojects.com/)** – A lightweight Python framework used for handling requests and serving data to the frontend.  
- **REST API** – Used for fetching and managing data between the frontend and backend.  

## 🗄️ Database  
- **[PostgreSQL](https://www.postgresql.org/)** – A powerful and reliable relational database used for storing user data, flashcards, and quiz results.  
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – An ORM (Object-Relational Mapping) tool used to simplify database interactions.  

## Illustration & Design 
#   🎨 
- **[Procreate](https://procreate.com/)** –  Sketch the minimalist cat logo,defining the color palette and refining the design elements and other illustrations.    
- **[Adobe Illustrator](https://www.adobe.com/products/illustrator.html)** –  designing and creating the logo. 
- **[Clipchamp](https://www.clipchamp.com/)** – editing promotional video About.  

## 🔄 Version Control  
- **[Git](https://git-scm.com/)** – tracking code changes and maintaining version control.  
- **[GitHub](https://github.com/)** – hosting and managing the project repository. 

## 🧪 Testing

This project uses `pytest` for testing the Flask application. Fixtures are defined in `conftest.py` and test cases are organized per blueprint (e.g. `test_users.py`, `test_words.py`, etc.).

### References

- Flask Official Documentation - Testing: https://flask.palletsprojects.com/en/2.3.x/testing/
- TestDriven.io - Testing Flask Applications with Pytest: https://testdriven.io/blog/flask-pytest/
- Miguel Grinberg Blog - Unit Testing Your Flask Application: https://blog.miguelgrinberg.com/post/unit-testing-your-flask-application



# [Comeback to Readme](#nihongo-quest)
---

# WIREFRAMES  
# 📐 

Nihongo Quest features several interactive sections, each designed to enhance the learning experience: **Home**, **Alphabet**, **Flashcards**, **Manga**, and **Quiz**. Below are the wireframes for the four main sections: 

## - Design Iteration  

The project started with wireframes to outline the main sections: Home, Flashcards, Alphabet, Manga, and Quiz.  

- Early versions were simple and focused mainly on functionality.  
- Based on feedback, the design was refined to improve navigation, responsiveness, and visual consistency.  
- A color palette inspired by Japanese culture and a custom logo were introduced to give the app a stronger identity.  
- Iterations also focused on UI/UX improvements, such as adjusting button placement, form validation, and adding motivational feedback during quizzes.  
- later expanded the app in add imagens.  

---

## 🏠 Home  

The **Home** section introduces the web app, explaining its purpose and long-term vision. It includes helpful **tips** and insights into Japanese culture and travel, aiming to create an engaging and immersive experience.  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/wireframes/home_pc.jpg" alt="Desktop Screenshot" width="330"> | <img src="./static/wireframes/home_tablet.jpg" alt="Tablet Screenshot" width="150"> | <img src="./static/wireframes/home_phone.jpg" alt="Mobile Screenshot" width="50"> |  

---  

## 🃏 Flashcards  

The **Flashcards** section is designed to improve memory retention through strategic exercises. As mentioned in the **Tips** section, mastering Japanese requires practicing writing, listening, and speaking — future updates will focus on incorporating these objectives.  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/wireframes/flashcard_pc.jpg" alt="Desktop Screenshot" width="330"> | <img src="./static/wireframes/flashCard_tablet.jpg" alt="Tablet Screenshot" width="150"> | <img src="./static/wireframes/flashCard_phone.jpg" alt="Mobile Screenshot" width="50"> |  

---  

## 🔠 Alphabet  

The **Alphabet** section explains the structure and differences between **Hiragana**, **Katakana**, and **Kanji**, providing a clear understanding of how the Japanese writing system works.  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/wireframes/alphabet_pc.jpg" alt="Desktop Screenshot" width="330"> | <img src="./static/wireframes/alphabet_tablet.jpg" alt="Tablet Screenshot" width="150"> | <img src="./static/wireframes/alphabet_phone.jpg" alt="Mobile Screenshot" width="50"> |  

---  

## 📖 Manga Section  

Anime and manga are major gateways to Japanese culture for many learners. The **Manga** section highlights the influence of manga in Western culture and encourages learning Japanese through reading. Users can discover new manga, helping to expand their vocabulary and reading skills in an enjoyable way.  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/wireframes/manga_pc.jpg" alt="Desktop Screenshot" width="330"> | <img src="./static/wireframes/manga_tablet.jpg" alt="Tablet Screenshot" width="150"> | <img src="./static/wireframes/manga_phone.jpg" alt="Mobile Screenshot" width="50"> |  

# [Comeback to Readme](#nihongo-quest)
---
# THE LOGO 
<img src="./static/screenshots/nihongo_logo.png" alt="Mobile Screenshot" width="350">

The logo for Nihongo Quest features a **minimalist cartoon-style cat head**, symbolizing curiosity and exploration — traits that reflect the learning journey in Nihongo Quest. The cat's simple and clean design represents the Japanese aesthetic of minimalism and balance.  

To the right of the cat's head, the logo includes the Japanese word **"日本語"** (*Nihongo*), which means **"Japanese language."** This reinforces the focus of the app on helping users navigate and learning Japanese through an engaging and intuitive experience.  

The combination of the cat and the Japanese text creates a visually balanced and culturally meaningful symbol that reflects the app’s purpose — learning Japanese through exploration and curiosity.
# [Comeback to Readme](#nihongo-quest)
---

# Colors:
## Color Palette Explanation  

The color palette for Nihongo Quest was carefully selected to reflect Japanese culture and history, particularly inspired by **Hiroshima** and the symbolism associated with **Japanese Culture**. Each color has a specific meaning and purpose in the design:  
<img src="./static/screenshots/background&colors.png" alt="Mobile Screenshot" width="350">
### **Body Colors**  
| Color | Code | Meaning |  
|-------|------|---------|  
| `#ff4646` | #ff4646 | Represents the red of the Japanese flag, symbolizing the sun and strength. |  
| `#ffffff` | #ffffff | Represents purity and simplicity, inspired by traditional Japanese minimalism. |  
| `#FFBEBE` | #FFBEBE | A light salmon pink, representing warmth and the softness of Japanese cherry blossoms. |  
| `rgb(255, 142, 142)` |rgb(255, 142, 142)| A softer red tone, providing a balanced contrast and warmth. |  
| `linear-gradient(108deg, #ff3314 0%, #86070b 29%, #43031a 75%)` | Gradient | A dynamic red gradient reflecting the intensity and historical depth of Hiroshima. |  

### **Footer and Navbar Colors** 
 <img src="./static/screenshots/footer_colors.png" alt="Mobile Screenshot" width="350">

| Color | Code | Meaning |  
|-------|------|---------|  
| `#606060` | #606060 | Neutral gray, symbolizing stability and balance. |  
| `#929292` | #929292 | A lighter gray, providing subtle contrast while maintaining harmony. |  
| `#ffffff` | #ffffff | Ensures readability and clarity. |  
| `#231E1E` | #231E1E | Dark tone for a clean, modern look inspired by traditional Japanese aesthetics. |  

# [Comeback to Readme](#nihongo-quest)
---
#  UI/UX Screenshots 
#  🎨

## 🏠 Home  

The **Home** section introduces the Nihongo Quest web app and sets the tone for the learning experience.  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/home-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/home-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/home-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

### 🌟 About  
The cover of **Nihongo Quest** introduces the app’s core purpose: to help learners immerse themselves in the Japanese language while experiencing the depth and beauty of Japanese culture.  

### 💡 Tips  
This section explains the key to mastering a new language: **consistent practice**. Listening, speaking, and writing daily is essential — but Nihongo Quest aims to make learning fun and engaging through interactive challenges.  

### 🌍 Travel  
Explore four of the most important cities in Japan — but Nihongo Quest doesn't stop there. The app aims to uncover the hidden secrets and rich history behind Japanese culture.  
**"Learning is more than just knowledge; it’s an adventure."**  

---  

## 🃏 Flashcards  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/flashcards-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/flashcards-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/flashcards-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

The **Flashcards** section helps sharpen memory and improve retention through regular exercise.  
> _"Your brain is like a muscle — it needs exercise!"_  
Challenge yourself daily with flashcards to reinforce your learning and track your progress.  

---  

## 📖 Manga Section  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/manga-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/manga-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/manga-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

The **Manga** section is a manga search tool where you can explore your favorite titles and suggest new ones.  
Curiosity is key to language learning — discovering new manga can expand your vocabulary and strengthen your reading skills.  
> _"Progress comes from curiosity."_

# [Comeback to Readme](#nihongo-quest)

---

#  Project Architecture


<img src="./static/screenshots/Diagram-NQ.PNG" alt="Mobile Screenshot" width="450">

This project follows an **MVC-like structure** inspired by Django MTV and .NET MVC.  
Each layer has a clear responsibility and works together to build a scalable web application.  

---

### 🟢 Python – Blueprint
- **Blueprints** allow splitting the app into modules (users, words, flashcards, etc.).  
- Keeps the code organized and reusable in large projects.  

---

### 🟠 HTML – Jinja
- **Jinja** is Flask’s templating engine, inserting dynamic data into HTML.  
- Enables the use of variables, loops, and conditions directly in web pages.  

---

### 🔵 PostgreSQL – Database
- **PostgreSQL** stores application data (users, words, flashcards, etc.).  
- **SQLAlchemy** maps Python classes to database tables.  
- **Flask-WTF + CSRF** handles secure web forms.  
 
---

### 🟣 Pytest – Testing
- **Pytest** is used for automated testing.  
- Ensures that routes, models, and forms work correctly after changes.  

---

### 📂 Project Structure
- **templates/** → HTML templates with Jinja.  
- **routes/** → Flask routes (URL handling).  
- **models/** → Database models (SQLAlchemy).  
- **tests/** → Automated tests with Pytest.  
- **forms.py** → Web forms defined with Flask-WTF.  

<img src="./static/screenshots/diagram-code.JPEG" alt="Mobile Screenshot" width="450">

##  - Git & Version Control  

- Version control was managed using Git and hosted on GitHub.  
- Each new feature (e.g., login system, flashcards, quiz logic) was developed in a separate branch before merging into the main branch.  
- Regular commits documented the progress and made it easier to track changes.  
- Pull requests were used to review changes before merging.  
- GitHub also served as a central hub for deployment to Heroku and collaboration. 
- Additionally, package.json and package-lock.json were included in version control to document the Node.js dependencies (used for JavaScript testing with Jest). These files ensure consistency if the environment needs to be reinstalled or tested by others.

---

# [Comeback to Readme](#nihongo-quest)

#  Nihongo Quest - Flask & PostgreSQL Setup Guide example
# 📚

<img src="./static/screenshots/fullStack.png" alt="Mobile Screenshot" width="450">

# Nihongo Quest

A Flask-based web application for learning Japanese vocabulary by adding, managing, and practicing words with their pronunciation and meanings.

## Table of Contents
1. [Database](#1-database)
2. [Back-end](#2-back-end-flask--sqlalchemy)
3. [Front-end](#3-front-end-html--jinja2-templates)

---

## 1. Database
The project uses **PostgreSQL** as its database, managed via **pgAdmin4**.

### Pages to references: 
 - **[NEON](https://neon.tech/postgresql/tutorial)** 
 - **[W3School (PostgreSQL)](https://www.w3schools.com/postgresql/postgresql_pgadmin4.php?utm_source=chatgpt.com)**
 - **[W3School (SQL)]()** 

### Creating the Database in pgAdmin4
1. Open **pgAdmin4**.
2. Create a new database:
   - Name: `nihongo_db`
   - Owner: `postgres`
3. Execute the following SQL command to create the **Word** table:
   ```sql
   CREATE TABLE word (
       id SERIAL PRIMARY KEY,
       japanese VARCHAR(100) NOT NULL,
       english VARCHAR(100) NOT NULL,
       pronunciation VARCHAR(100)
   );
   ```
4. Insert sample words:
   ```sql
   INSERT INTO word (japanese, english, pronunciation) VALUES
   ('ねこ', 'cat', 'ne-ko'),
   ('いぬ', 'dog', 'i-nu'),
   ('さくら', 'cherry blossom', 'sa-ku-ra');
   ```

---

## 2. Back-end (Flask + SQLAlchemy)
The back-end is built using Flask and SQLAlchemy.

### Pages to references: 
- **[REAL PYTHON](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#update-configuration)** 
 

### **Database Configuration (`config.py`)**
```python
import os

DATABASE_URI = "postgresql://postgres:Example@localhost/nihongo_db"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "0000"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### **Database Setup (`db.py`)**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### **Word Model (`models/word.py`)**

```python
from flask import current_app
from extensions import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    pronunciation = db.Column(db.String(100))

    def __repr__(self):
        return f"<Word {self.japanese} - {self.english} - Pronunciation: {self.pronunciation}>"
```

### **Form for Adding Words (`forms.py`)**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation")
    submit = SubmitField("Add Word")
```

### **Adding Words (`app.py`)**
### Pages to references: 
- **[Flask Pallets (Minimal app)](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods)** 
- **[Flask Pallets (Methods)](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods)**
- **[Flask Pallets (Rendering Templates)](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates)**
- **[Flask Pallets (SQLAlquemy)](https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/)**

```python
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required
from extensions import db
from models.word import Word
from forms import WordForm

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)

@app.route("/add_word", methods=["GET", "POST"])
@login_required
def add_word():
    form = WordForm()

    if request.method == "POST" and form.validate_on_submit():
        new_word = Word(
            japanese=form.japanese.data,
            english=form.english.data,
            pronunciation=form.pronunciation.data
        )
        db.session.add(new_word)
        db.session.commit()

        flash("New word added successfully!", "success")
        return redirect(url_for("add_word"))

    return render_template("add_words.html", form=form)
```

---

## 3. Front-end (HTML + Jinja2 Templates)
The application uses **Jinja2** for rendering dynamic HTML pages.
### Pages to references: 
 **[JINJA](https://jinja.palletsprojects.com/en/stable/)** 
 

### **Adding Words (`templates/add_words.html`)**
```html
{% extends "base.html" %}
{% block title %}Add Word - Nihongo Quest{% endblock %}
{% block content %}
<div class="container">
    <h2 class="title_add">Add a New Japanese Word</h2>
    <p class="text-how">Add words and create your own personalized learning experience!</p>

    <!-- Flash Messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
    {% endwith %}

    <!-- Form to add words -->
    <form method="POST" action="/add_word">
        {{ form.hidden_tag() }}
        <label for="japanese">Japanese:</label>
        <input type="text" id="japanese" name="japanese" required>
    
        <label for="english">English:</label>
        <input type="text" id="english" name="english" required>
    
        <label for="pronunciation">Pronunciation:</label>
        <input type="text" id="pronunciation" name="pronunciation">
    
        <button type="submit" class="button">Add Word</button>
    </form>
</div>
{% endblock %}
```

---

# [Comeback to Readme](#nihongo-quest)

---
# EXAMPLE OF ALGORITHM & CODE:

## 📌 Quiz Function Explanation
The `quiz()` function handles the quiz logic in a Flask web application. It:

- Displays a form with words from the database.
- Processes user answers and checks correctness.
- Uses Flask routes, loops, if-else conditions, dictionaries, and flash messages.
- Requires user authentication `(@login_required)`.
- Redirects users after submission.

## 📌 Code analysis of word.py:

Flask and PostgreSQL.
```python
# 1. Importing Dependencies: "word.py"  
from flask import current_app
from extensions import db

class Word(db.Model):  #  2. Defining the `Word` Model: "Defines a SQLAlchemy model for a database table"
   
    #  3. Defining Database Columns:
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each word (Primary Key)
    japanese = db.Column(db.String(100), nullable=False)  # Japanese word (max 100 chars)
    english = db.Column(db.String(100), nullable=False)  # English translation (max 100 chars)

    def __repr__(self):
        return f"<Word {self.japanese} - {self.english}>"  # String representation for debugging

```

## 🔍 Code with Detailed Comments

```python
# Function: Defines a route for the quiz page
@app.route("/quiz", methods=["GET", "POST"])  # Flask route decorator
@login_required  # Restricts access to logged-in users
def quiz():  # Function definition
    words = Word.query.all()  # Query database (Array/List of objects)
    feedback = {}  # Dictionary to store feedback

    # If-Else Condition: Checks if the request method is POST (Form submitted)
    if request.method == "POST":
        answers = {}  # Dictionary to store user's answers
        correct_answers = 0  # Counter for correct answers
        total_questions = 0  # Counter for total questions

        # For Loop: Iterates over each word in the database
        for word in Word.query.all():
            answer_key = f"answer_{word.id}"  # Generates form key dynamically
            user_answer = request.form.get(answer_key, "").strip()  # Gets user input
            correct_answer = word.english.strip()  # Fetches correct answer

            # If Condition: Compares user input with the correct answer (Case insensitive)
            if user_answer.lower() == correct_answer.lower():
                correct_answers += 1  # Increments correct answer count

            total_questions += 1  # Increments total question count
            answers[word.id] = user_answer  # Stores user's answer in dictionary

        # If-Else Condition: Provides feedback based on quiz performance
        if correct_answers == total_questions:
            flash("Perfect score! All answers are correct. 🎉", "success")  # Success message
        elif correct_answers > 0:
            flash(f"{correct_answers} correct answers. Keep practicing!💪", "warning")  # Encouragement
        else:
            flash("No correct answers. Keep practicing! 💪", "danger")  # Motivational message

        return redirect(url_for("index"))  # Redirects to homepage after submission

    # Else If Condition: Handles GET request (Displays quiz form)
    elif request.method == "GET":
        words = Word.query.all()  # Fetches all words from database

    return render_template("quiz.html", words=words)  # Renders quiz page
```
## 📌 Explanation with W3Schools References

| Concept                              | Explanation                                                                | W3Schools, flask, and SQLAlquemy Links       |
|--------------------------------------|----------------------------------------------------------------------------|----------------------|
| **Function (`def`)**                 | Defines a function (`quiz()`) to handle requests.                          | [Python Functions](https://www.w3schools.com/python/python_functions.asp) |
| **Flask Route (`@app.route`)**       | Defines a route (`/quiz`) that handles GET and POST requests.              | [Flask Routes](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing) |
| **If-Else (`if request.method == "POST"`)** | Checks whether the request is a form submission (POST) or just loading the page (GET). | [Python If-Else](https://www.w3schools.com/python/python_conditions.asp) |
| **Loop (`for word in Word.query.all()`)** | Iterates over each word stored in the database.                            | [Python Loops](https://www.w3schools.com/python/python_for_loops.asp) |
| **Dictionary (`answers = {}`)**      | Stores user answers using key-value pairs.                                 | [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) |
| **Flask Flash Messages (`flash()`)** | Displays messages to users based on their score.                           | [Flask Flash Messages](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/) |
| **Flask Redirect (`redirect(url_for("index"))`)** | Redirects users to another route.                                    | [Flask Redirect](https://flask.palletsprojects.com/en/2.3.x/api/#flask.redirect) |
| **Class (`class Word`)**             | Defines a database model (`Word`) with attributes `id`, `japanese`, and `english`. | [Python Classes](https://www.w3schools.com/python/python_classes.asp) |
| **SQLAlchemy Model (`db.Model`)**    | Connects the `Word` class to the PostgreSQL database using SQLAlchemy.     | [SQLAlchemy Models](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/) |
| **Database Column (`db.Column`)**    | Defines table columns (`id`, `japanese`, `english`) in the database.       | [SQLAlchemy Column](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/#column) |
| **String Data Type (`db.String`)**   | Stores text data with a max length (e.g., `100` characters).               | [SQLAlchemy String](https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.String) |
| **Primary Key (`primary_key=True`)** | Uniquely identifies each word entry in the database.                       | [Primary Key](https://www.w3schools.com/sql/sql_primarykey.asp) |
| **Special Method (`__repr__`)**      | Returns a string representation of the object (`"<Word Japanese - English>"`). | [Python __repr__](https://www.w3schools.com/python/ref_func_repr.asp) |



## ✅ Summary algorithm
- This function is responsible for handling quiz logic in the Flask app.
- Uses database queries to fetch words from the database.
- Uses a for loop to iterate through words and compare answers.
- Implements flash messages to give users feedback.
- Uses redirect() to send users back to the homepage after submission.
📌 For more information, check the W3Schools and Flask links above! 🚀

quiz.html end explanation:
```html
<!-- 1. Page Header: "Displays the title of the quiz page" -->
<h1>Japanese Quiz</h1>

<!-- 2. Form Setup: "Defines a form that submits data to the '/quiz' route via POST" -->
<form action="{{ url_for('quiz')}}" method="POST">

    <!-- 3. CSRF Token: "Prevents CSRF attacks for security" -->
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">

    <!-- 4. Looping Through Words: "Displays each Japanese word and an input box for the answer" -->
    {% for word in words %}
       <p>What is the meaning of "{{ word.japanese }}"?</p>
       <input type="text" name="answer_{{ word.id }}" 
       class="{% if feedback and feedback[word.id] == 'correct' %}correct{% elif feedback and feedback[word.id] == 'incorrect' %}incorrect{% endif %}">
    {% endfor %}

    <!-- 5. Submit Button: "Sends the user's answers for evaluation" -->
    <button type="submit">Submit</button>
</form>

<!-- 6. Return Link: "Navigates back to the homepage" -->
<a href="/">Return to Home</a>

```
# [Comeback to Readme](#nihongo-quest)
---

## Problems and Solutions  

### Pages to references: 
 - **[Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/)** 

### ❌ **Problem: CSRF Token Errors in Quiz Form**  
- **Issue:** The CSRF token was missing or not being validated correctly in the form submission.  
- **Solution:**  
  - Ensured that `CSRFProtect(app)` was correctly initialized in `app.py`.  
  - Passed the CSRF token explicitly in `render_template()`.  
  - Added a hidden input field in `quiz.html` to include the CSRF token in the form.  

### ❌ **Problem: Understanding Mako Templates**  
- **What is Mako?**  
  Mako is a templating engine for Python, similar to Jinja2 but with a syntax closer to standard Python expressions.  
  - **Why is it relevant?** Mako is sometimes used in Flask applications when working with certain frameworks or plugins that require an alternative template engine.  
  - **In Nihongo Quest:** We are using Jinja2 (Flask's default template engine), so Mako is not needed for now. However, understanding Mako can be useful for other Python projects.  

## Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/ToniEstarlich/nihongo-quest.git
   cd nihongo-quest
   ```

2. Create and activate a virtual envionment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```

3. Install independecies:
   ```sh
   pip install -r requirements.txt

   ```
4. Run the application
   ```sh
   flask run

   ```
## Contributing  

Feel free to open issues or submit pull requests to improve Nihongo Quest! 



