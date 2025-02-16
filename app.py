from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from config import Config
from extensions import db, login_manager, migrate  # Import db and other extensions
from flask_login import  login_user, logout_user, login_required
from models.user import User  # Import User model
from models.word import Word  # Import Word model

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
    return User.query.get(int(user_id))

@app.route("/")
def index():
    words = Word.query.all()
    return render_template("index.html", words=words)

@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == "POST":
        answers = {}
        for word in Word.query.all():
            answer_key = f"answer_{word.id}"
            user_answer = request.form.get(answer_key, "").strip()
            answers[word.id] = user_answer # Store the user's answer

        flash("Quiz submitted successfully!", "success")
        return redirect(url_for("index")) # Redirect after submitting
    words = Word.query.all()
    return render_template("quiz.html", words=words, csrf_token=generate_csrf())

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

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out!", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
