## Comeback [README](../README.md)
# routes/users_routes.py
**Purpose** Handle user registration, login, and logout using ``Flask-Login`` + hashed passwords.

### /register (GET, POST)
Registers a new user and stores a hashed password.

**Models** 🟦  
  ```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    ...
    def set_password(self, password):
```

**Routes** 🟩 
  ```python
  @users_bp.route("/register", methods=["GET", "POST"])
  def register():
    if request.method == "POST":
        username = request.form["username"]
    ...
    return render_template("users/register.html")
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  <form class="register" method="POST">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">

    <label for="username">Username</label>
    <input type="text" name="username" id="username" required>
    ...
  ``` 
**Summary:**

1- Validates username uniqueness.

2- Hashes password (bcrypt).

3- Saves new user → redirects to login.
### /login (GET, POST)
**Forms** 🟦 
  ```python
  class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
  ```
**Routes** 🟩 
  ```python
  @users_bp.route("/login", methods=["GET","POST"])
  def login():
    form = LoginForm()
    ...
    return render_template("users/login.html", form=form)
  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
      <form method="POST">
        <!-- CSRF token --> 
         {{ form.hidden_tag() }}
        <label for="username">Username</label>
        <input type="text" name="username" 
        ...
    <p class="reg-here-text text-white" >Don't have an account?<a class="reg-here" href="{{url_for('users.register') }}">Register here</a></p>
  ``` 
  **Summary:**

1- Reads username/password from form.

2- Verifies password with check_password.

3- Logs the user in and redirects.

4- Flashes errors if invalid.
### /logout (GET)
**Routes** 🟩 
  ```python
  @users_bp.route("/logout")
  @login_required
  def logout():
    logout_user()
    return redirect(url_for("index"))

  ```
**HTML** 🟧 **Jinja** ⬜
  ```html
  <a href="{{ url_for('users.logout') }}">Logout</a>
  ``` 
  **Summary:**

1- Ends the session using logout_user().

2- Redirects to homepage.

3- Shows a flash message.
## Comeback [README](../README.md)