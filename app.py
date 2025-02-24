from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from config import Config
from extensions import db, login_manager, migrate  # Import db and other extensions
from flask_login import  login_user, logout_user, login_required
from models.user import User  # Import User model
from models.word import Word  # Import Word model
from forms import LoginForm # Assuming the loginForm is in forms.py file
import requests

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

# Set a secret key
app.secret_key = "0000"

# Initialize the extensions with the app
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route("/")
def index():
    words = Word.query.all()
    return render_template("index.html", words=words)

# Quiz
@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    words = Word.query.all() #Assuming have a World model in the database
    feedback = {}

    if request.method == "POST":
        answers ={}
        correct_answers = 0
        total_questions = 0

        for word in Word.query.all():
            answer_key = f"answer_{word.id}"
            user_answer = request.form.get(answer_key, "").strip()
            correct_answer =word.english.strip() # Assuming the correct is stored in 'english' column

            if user_answer.lower() == correct_answer.lower():
                correct_answers +=1 # Count correct answers

            total_questions +=1 #Count total questions
            answers[word.id] = user_answer #Store the user's answer
        
        # Provide feedback based on the number of correct answers
        if correct_answers == total_questions:
            flash("Perfect score! All answers are correct. 🎉","success")
        elif correct_answers > 0:
            flash(f"{correct_answers} correct answers. keep practicing!💪" "warning")
        else:
            flash("No correct answers. keep practicing! 💪", "danger")

        return redirect(url_for("index"))  # Redirect to home page after processing answers
    
    elif request.method == "GET":
        # Display fro GET request
        words = Word.query.all() # Fetch all words from the database
    return render_template("quiz.html", words=words)

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"] # get the email from the form

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))
        
        new_user = User(username=username, email=email) # Store Email
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! You can now log in.", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # Initialize  the form

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            next_page = request.args.get('next') # Redirect after login, if provided
            return redirect(next_page or url_for("index"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out!", "info")
    return redirect(url_for("index"))



# Manga search section

@app.route('/manga')
def manga():
    # Fetch manga data from Jikan API
    response = requests.get('https://api.jikan.moe/v4/manga')
    manga_data = response.json()['data']  # Get the 'data' key which contains the manga list

    # Pass manga data to the template
    return render_template('manga.html', manga_data=manga_data)

# Route for searching manga
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')  # Get the search query from URL parameters
    if query:
        # Fetch search results from Jikan API based on the query
        response = requests.get(f'https://api.jikan.moe/v4/manga?q={query}')
        manga_data = response.json()['data']  # Get search results
    else:
        manga_data = []

    # Pass search results to the template
    return render_template('manga.html', manga_data=manga_data)

if __name__ == "__main__":
    app.run(debug=True)
