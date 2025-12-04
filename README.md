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
- translate and add words to design my own flashcards, and add words with images in the “Add Image” section to enhance my learning.

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
7. [Routes, functions & tests](#nihongo-quest--routes-functions--tests-overview)
8. [CRUDs](#cruds)
9. [Testing](#test-results)
10. [Problems & Solutions](#problems-and-solutions)
11. [Deployment](#deployment)

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
-  Finally, translator functionality was added to “Add Words” and “Add Images”, enabling users to translate, add, and design their own words for flashcards while managing images in their personal Image List. 

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

##  Home  

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

## Flashcards  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/flashcards-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/flashcards-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/flashcards-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

The **Flashcards** section helps sharpen memory and improve retention through regular exercise.  
> _"Your brain is like a muscle — it needs exercise!"_  
Challenge yourself daily with flashcards to reinforce your learning and track your progress.  

---  

##  Manga Section  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/manga-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/manga-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/manga-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

The **Manga** section is a manga search tool where you can explore your favorite titles and suggest new ones.  
Curiosity is key to language learning — discovering new manga can expand your vocabulary and strengthen your reading skills.  
> _"Progress comes from curiosity."_

---

##  Translate + Add Word  

| Desktop View | Tablet View | Mobile View |  
|--------------|-------------|-------------|  
| <img src="./static/screenshots/translate-pc.jpeg" alt="Desktop Screenshot" width="330"> | <img src="./static/screenshots/translate-tablet.jpeg" alt="Tablet Screenshot" width="150"> | <img src="./static/screenshots/translate-phone.jpeg" alt="Mobile Screenshot" width="50"> |  

At the end of the project, a **word translator** was added to improve the user experience. Users can first translate the word they search for and then choose to add it to their vocabulary. There is also an option to add words manually.

# [Comeback to Readme](#nihongo-quest)

---  

#  Project Architecture


<img src="./static/screenshots/Diagram-NQ.PNG" alt="Mobile Screenshot" width="450">

This project follows an **MVC-like structure** inspired by Django MTV and .NET MVC.  
Each layer has a clear responsibility and works together to build a scalable web application.  

---
### 🔵 PostgreSQL – Database
- **PostgreSQL** stores application data (users, words, flashcards, etc.).  
- **SQLAlchemy** maps Python classes to database tables.  
- **Flask-WTF + CSRF** handles secure web forms.  
 
---

### 🟢 Python – Blueprint
- **Blueprints** allow splitting the app into modules (users, words, flashcards, etc.).  
- Keeps the code organized and reusable in large projects.  

---

### 🟠 HTML – Jinja
- **Jinja** is Flask’s templating engine, inserting dynamic data into HTML.  
- Enables the use of variables, loops, and conditions directly in web pages.  

---

### 🟣 Pytest – Testing
- **Pytest** is used for automated testing.  
- Ensures that routes, models, and forms work correctly after changes.  

---

### 📂 Example Project Structure
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
- The latest commits added the translator functionality to “Add Words” and “Add Image”, allowing users to translate, add, and design their own words for flashcards, while also managing images in their personal Image List. These changes involved updates to `routes/translator.py` and `routes/image_translator.py`.

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
 # NIHONGO QUEST — Routes, Functions & Tests Overview 
 # 📘

**Legend:**  
🟢 Implemented / Documented · 🔴 Tests incomplete or failing

This document provides a complete overview of all route modules in the **Nihongo Quest** Flask application, including their functionality and current test coverage. Below you will also find a clear explanation of the **user experience flow** inside the app.

---

# 🚏 Routes & Tests

## 👤 Users — Authentication  
### Route Documentation: [users](/docs/routes_README/users_README.md) 🟢  
Handles user registration, login, and logout with hashed passwords, form validation, and session management using Flask-Login.

### Tests: [users tests](/docs/tests_README/users_README.md) 🔴  
Validates authentication workflows: registration, login, logout, session handling, and flash messages across success and failure scenarios.

---

## 🔤 Translator — English → Japanese  
### Route Documentation: [translator](/docs/routes_README/translator_README.md) 🟢  
Translates English words into Japanese (Kanji, Kana, Romaji) using external APIs and `pykakasi`. Also fetches a related image from Pexels and integrates the results into Flask forms for saving.

### Tests: [translator tests](/docs/tests_README/translator_README.md) 🔴  
Ensures the translation module returns complete, valid dictionaries; handles empty inputs gracefully; validates all fields; and provides reliable image fallback behavior.

---

## 📝 Words — Vocabulary CRUD  
### Route Documentation: [words](/docs/routes_README/words_README.md) 🟢  
Provides full CRUD functionality for user-saved vocabulary (English ⇄ Japanese) using authenticated Flask routes and WTForms.

### Tests: [words tests](/docs/tests_README/words_README.md) 🔴  
Verifies correct behavior in listing, adding, editing, and deleting words, ensuring access control, database integrity, and proper flash messaging.

---

## 🃏 Flashcards & Quiz  
### Route Documentation: [flashcard](/docs/routes_README/flashcards_README.md) 🟢  
Generates 5-word flashcards from user vocabulary and provides an interactive quiz system with answer checking, visual feedback, and score-based flash messages.

### Tests: [flashcard tests](/docs/tests_README/flashcard_README.md) 🔴  
Validates flashcard loading, correct rendering, quiz evaluation accuracy, and proper feedback messaging.

---

## 🈁 Alphabet — Hiragana, Katakana, Kanji  
### Route Documentation: [alphabet](/docs/routes_README/alphabet_README.md) 🟢  
Serves Japanese alphabets and Kanji, querying the database and rendering characters with readings and meanings.

### Tests: [alphabet tests](/docs/tests_README/alphabet_README.md) 🔴  
Ensures that alphabet overview and individual pages load successfully with the expected content.

---

## 🖼️ Image Manager  
### Route Documentation: [image](/docs/routes_README/image_README.md) 🟢  
Allows authenticated users to upload, view, edit, and delete images, each linked to Japanese word metadata. Includes file validation and DB integration.

### Tests: [image tests](/docs/tests_README/image_README.md) 🔴  
Ensures the image list loads correctly and displays user-specific images with their Japanese metadata.

---

## 🌉 Image Translator — English → Japanese + Image Fetch  
### Route Documentation: [image translator](/docs/routes_README/image_translator_README.md) 🟢  
Translates English queries into Japanese, converts them to Kana/Romaji, fetches a related Pexels image, and allows saving metadata and images to the database.

### Tests: [image translator tests](/docs/tests_README/image_translator_README.md) 🔴  
Validates complete dictionary responses, safe empty-query handling, preservation of original English words, and the presence of a valid image URL.

---

## 📚 Manga Explorer  
### Route Documentation: [manga](/docs/routes_README/manga_README.md) 🟢  
Displays manga lists and search results using the Jikan API, showing titles, images, and synopses.

### Tests: [manga tests](/docs/tests_README/manga_README.md) 🔴  
Ensures list and search pages load correctly, handle mocked API responses, display content properly, and respond correctly to empty or provided search queries.

---

# 🎮 User Experience (UX) — Nihongo Quest



---

## 1. 👤 Authenticate  
- Register  
- Log in / log out  
- Persistent user sessions  

---

## 2. 🈶 Learn & Save Vocabulary  
- Translate English → Japanese  
- Manually add words  
- Every saved word is automatically linked to the flashcard system  

---

## 3. 🖼️ Memorize with Images  
- Upload images  
- Link images to their Japanese words  
- View and manage a personal image library  

---

## 4. 🔍 Explore Japanese Content  
- Study Hiragana, Katakana, and Kanji  
- Search manga (via Jikan API)  
- View readings, meanings, and illustrations  

---

## 5. 🃏 Practice With Flashcards  
- Automatically generated flashcard sets  
- Quiz with scoring and correctness feedback  
- Flash messages for progress tracking  

---

### ✔ All user data, vocabulary, images, and progress are saved per account.
# [Comeback to Readme](#nihongo-quest)
After creating an account, the user can:
# CRUDs
### Words
- Translate a word

<img src="./static/guide_screenshots/search-word.jpeg" alt="Website Preview" width="300">

- Add the word from the translate or manually

<img src="./static/guide_screenshots/add_word.jpeg" alt="Website Preview" width="300">

- The word is automatically added in `words` and `flashcards`

<img src="./static/guide_screenshots/add_flashcard.jpeg" alt="Website Preview" width="300">

- Edit the word

<img src="./static/guide_screenshots/edit_word.jpeg" alt="Website Preview" width="300">

- Or delete the word

<img src="./static/guide_screenshots/delete_word.jpeg" alt="Website Preview" width="300">

### Images
- Translate and search an image

<img src="./static/guide_screenshots/search_img.jpeg" alt="Website Preview" width="300">

- Add the image to your `image list`

<img src="./static/guide_screenshots/add_img.jpeg" alt="Website Preview" width="300">

- Edit or delete the image

<img src="./static/guide_screenshots/edit_img.jpeg" alt="Website Preview" width="300">

<img src="./static/guide_screenshots/delete_img.jpeg" alt="Website Preview" width="300">

### Flashcard Game
- Enter flashcards and start the quiz (5 words per card)

<img src="./static/guide_screenshots/flashCards_game.jpeg" alt="Website Preview" width="300">

- Answer the Japanese words

<img src="./static/guide_screenshots/question-flascard.jpeg" alt="Website Preview" width="300">

- After submitting, you can see the results:
  - Correct answer: "Perfect score! All answers are correct. 🎉", "success"
  - Some correct: "Correct answers. Keep practicing! 💪", "warning"
  - All incorrect: "No correct answers. Keep practicing! 💪", "danger"

<img src="./static/guide_screenshots/results-cards.jpeg" alt="Website Preview" width="300">

# [Comeback to Readme](#nihongo-quest)

## Test Results
# 🧪 

All automated tests for Nihongo Quest passed successfully:

<img src="./static/guide_screenshots/pytest.png" alt="Website Preview" width="500">

This demonstrates that:
- User authentication works correctly
- Word CRUD functions properly
- Image upload, edit, and deletion works
- Flashcard quiz system functions as expected
- Translation and image fetching modules operate reliably
### How to Run Tests

To run all automated tests for Nihongo Quest, follow these steps:

```bash
# Activate your virtual environment
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Run all tests
pytest

# Run tests in a specific directory
pytest tests/
```
# [Comeback to Readme](#nihongo-quest)
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

### Deployment
The project was deployed to **Heroku** using a PostgreSQL database. The steps to deploy are as follows:

1. Login to Heroku CLI and create a new app.
2. Add the Heroku PostgreSQL add-on for the database.
3. Push the project to Heroku using Git.
4. Initialize the database tables in production.
5. Open the app using the live link below.

The live link can be found here: [Nihongo Quest](https://nihongo-quest-app-54ed3ed7b8f5.herokuapp.com/)

# [Comeback to Readme](#nihongo-quest)
## Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/ToniEstarlich/nihongo-quest.git
   cd nihongo-quest
   ```

2. Create and activate a virtual envionment:
   ```sh
   python -m venv venv
     
     venv\Scripts\activate  # On IOs: source venv/bin/activate

   ```

3. Install independecies:
   ```sh
   pip install -r requirements.txt

   ```
4. Run the application
   ```sh
   python app.py

   ```
## Contributing  

Feel free to open issues or submit pull requests to improve Nihongo Quest! 

# [Comeback to Readme](#nihongo-quest)

