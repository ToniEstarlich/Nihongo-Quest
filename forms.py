#form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, FileField 
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class WordForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation")
    submit = SubmitField("Add Word")

class TaskImagenForm(FlaskForm):
    image = FileField("Upload Image", validators=[DataRequired()])
    category = SelectField("Category", choices=[
        ("Object", "Object"), ("Verb", "Verb"), ("Fruit", "Fruit"),
        ("Street", "Street"), ("Shop", "Shop"), ("Animals", "Animals"),
        ("Plants", "Plants"), ("People", "People")
    ], validators=[DataRequired()])
    japanese_word = StringField("Japanese Word", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation", validators=[DataRequired()])
    submit = SubmitField("Add Entry")

class DeleteImageForm(FlaskForm):
    submit = SubmitField("Delete")