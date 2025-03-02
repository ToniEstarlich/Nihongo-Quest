# Nihongo Quest  

Nihongo Quest is a Flask-based web application designed to help users learn Japanese vocabulary through interactive quizzes. Users can log in, take quizzes, and test their knowledge by answering questions about Japanese words.

## Objective and Next Steps  

### Objective  
The goal of Nihongo Quest is to provide an engaging platform for learning Japanese vocabulary. The app allows users to take quizzes, track their progress, and improve their understanding of the language through repetition and interaction.

### Next Steps  
- Implement user-specific progress tracking and scores.  
- Improve the UI/UX for a better learning experience.  
- Add more quiz categories and difficulty levels.  
- Deploy the application online for wider accessibility.  



## Technologies Used  

- **Flask** – Backend framework  
- **SQLAlchemy** – Database ORM  
- **Flask-Login** – User authentication  
- **Flask-WTF** – Forms and CSRF protection  
- **Jinja2** – Template rendering 

---
# 📚 Nihongo Quest - Flask & PostgreSQL Setup Guide example

## 🔹 1. Database (PostgreSQL + pgAdmin 4)  

### 📌 Step 1: Create a Database and Table  
1. Open **pgAdmin 4** and connect to your PostgreSQL server.  
2. Create a new database:  
   - **Right-click** on "Databases" → Click **"Create"** → Select **"Database"**  
   - Enter a **name** (e.g., `nihongo_db`) → Click **Save**  
3. Open the **Query Tool** and create a table:  
   ```sql
   CREATE TABLE hiragana (
       id SERIAL PRIMARY KEY,
       character VARCHAR(10) NOT NULL,
       pronunciation VARCHAR(20) NOT NULL
   );
   ```  
4. Insert sample data:  
   ```sql
   INSERT INTO hiragana (character, pronunciation) VALUES
   ('あ', 'a'), ('い', 'i'), ('う', 'u'), ('え', 'e'), ('お', 'o');
   ```

### 🌍 API Endpoints

| Endpoint      | Method | Description          |
|--------------|--------|----------------------|
| /            | GET    | Home Page            |
| /quiz        | GET    | Quiz Section         |
| /flashcards  | GET    | Flashcards Page      |
| /alphabet    | GET    | Alphabet Learning    |
| /manga       | GET    | Manga Section        |
| /register    | POST   | User Registration    |
| /login       | POST   | User Login           |


### 🗄️ Database Structure

- **Users Table**: Stores user details  
- **Flashcards Table**: Stores flashcards content  
- **Manga Table**: Stores manga references  
- **Quiz Table**: Stores quiz questions & answers  


---

## 🔹 2. Backend (Flask + SQLAlchemy)  

### 📌 Step 2: Install Dependencies  
Run the following command inside your virtual environment:  
```bash
pip install flask flask-sqlalchemy psycopg2
```

### 📌 Step 3: Database Configuration  
#### 📂 `db.py` (Database Connection)  
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

#### 📂 `config.py` (Database Settings)  
```python
import os

DB_NAME = "nihongo_db"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
```

---

### 📌 Step 4: Define Models  
#### 📂 `models/alphabet.py` (Hiragana Model)  
```python
from db import db

class Hiragana(db.Model):
    __tablename__ = "hiragana"
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(10), nullable=False)
    pronunciation = db.Column(db.String(20), nullable=False)
```

---

### 📌 Step 5: Create Flask Routes  
#### 📂 `routes/alphabet_routes.py` (Blueprint & API Routes)  
```python
from flask import Blueprint, render_template
from db import db
from models.alphabet import Hiragana

alphabet_bp = Blueprint("alphabet", __name__, url_prefix="/alphabet")

@alphabet_bp.route('/hiragana')
def get_hiragana():
    characters = Hiragana.query.all()
    return render_template('alphabet/hiragana.html', characters=characters)
```

---

### 📌 Step 6: Initialize Flask App & Register Blueprints  
#### 📂 `app.py` (Main Application File)  
```python
from flask import Flask
from config import DATABASE_URI
from db import db
from routes.alphabet_routes import alphabet_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(alphabet_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```

---

## 🔹 3. Frontend (HTML + Jinja2 Templates)  

### 📌 Step 7: Create the Template  
#### 📂 `templates/alphabet/hiragana.html` (Frontend Display)  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hiragana Characters</title>
</head>
<body>
    <h1>Hiragana Alphabet</h1>
    <table border="1">
        <tr>
            <th>Character</th>
            <th>Pronunciation</th>
        </tr>
        {% for char in characters %}
        <tr>
            <td>{{ char.character }}</td>
            <td>{{ char.pronunciation }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
##  Next Steps
# 🚀

- Design & implement the frontend

- Testing & bug fixing

- Deploy to Heroku

---

## 🔹 4. Run the Flask App  
1. Open the terminal and activate your virtual environment.  
2. Start the Flask app:  
   ```bash
   flask run
   ```
3. Open your browser and visit:  
   **`http://127.0.0.1:5000/alphabet/hiragana`**  


---
# THE ALGORITHM & CODE:

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

---
## Problems and Solutions  

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
   git clone https://github.com/your-username/nihongo-quest.git
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


