from flask import Flask, render_template, request, flash, url_for, redirect
from routes.alphabet_routes import alphabet_bp
from routes.manga_routes import manga_routes
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from config import Config
from extensions import db, login_manager, migrate
from flask_login import login_user, logout_user, login_required
from models.user import User
from models.word import Word
from models.task import db
from routes.task_routes import task_bp
from forms import LoginForm
import requests

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(alphabet_bp, url_prefix="/alphabet")
app.register_blueprint(task_bp, url_prefix='/task')
app.register_blueprint(manga_routes)

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

# Updated index route
@app.route("/")
def index():
    return render_template("index.html")

# New flashcards route
@app.route("/flashcards")
@login_required
def flashcards():
    words = Word.query.all()
    return render_template("flashcards.html", words=words)

# Quiz flashcards
@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    card_id = request.args.get('card_id', 1, type=int)
    words = Word.query.all()
    start_index = (card_id - 1) * 5
    selected_words = words[start_index:start_index + 5]
    feedback = {}

    if request.method == "POST":
        correct_answers = sum(
            1 for word in selected_words if request.form.get(f"answer_{word.id}", "").strip().lower() == word.english.strip().lower()
        )
        total_questions = len(selected_words)

        if correct_answers == total_questions:
            flash("Perfect score! All answers are correct. 🎉", "success")
        elif correct_answers > 0:
            flash(f"{correct_answers} correct answers. Keep practicing! 💪", "warning")
        else:
            flash("No correct answers. Keep practicing! 💪", "danger")

        return redirect(url_for("flashcards"))

    return render_template("quiz.html", selected_words=selected_words, card_id=card_id, feedback=feedback)

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(request.args.get('next') or url_for("index"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out!", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)