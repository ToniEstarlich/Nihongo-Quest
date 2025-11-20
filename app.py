from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf.csrf import CSRFProtect, CSRFError, generate_csrf
from config import Config
from extensions import bcrypt, db, login_manager, migrate
from flask_login import login_user, logout_user, login_required, current_user
import os
from models.user import User
from models.word import Word

print("DATABASE_URL =", os.environ.get("DATABASE_URL"))

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)
csrf.init_app(app)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = "users.login"  #  blueprint is users.login
bcrypt.init_app(app)

# Import blueprints
from routes.users_routes import users_bp
from routes.alphabet_routes import alphabet_bp
from routes.image_routes import image_bp
from routes.manga_routes import manga_routes
from routes.flashcards_routes import flashcards_bp
from routes.translator import translator_bp
from routes.errors import errors
from routes.image_translator import visual_bp

app.register_blueprint(users_bp,)  
 
app.register_blueprint(alphabet_bp, url_prefix="/alphabet")
app.register_blueprint(image_bp, url_prefix="/images")
app.register_blueprint(visual_bp, url_prefix="/visual")
app.register_blueprint(manga_routes)
app.register_blueprint(flashcards_bp,)
app.register_blueprint(translator_bp, url_prefix='/translator')
app.register_blueprint(errors)

from routes.words_routes import words_bp
app.register_blueprint(words_bp) 

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.before_request
def log_csrf_token():
    if request.method == "POST":
        csrf_token = request.form.get('_csrf_token')
        print(f"CSRF Token: {csrf_token}")

@app.errorhandler(CSRFError)
def handle_csrf_error(error):
    print(f"CSRF Error: {error.description}")
    flash("CSRF token missing or incorrect", "danger")
    return redirect(request.referrer or url_for("index"))

@app.route("/")
def index():
    return render_template("index.html")


@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
