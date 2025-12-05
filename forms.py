# form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, Optional
from wtforms import SubmitField

# Login form


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


# Register form


class WordForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation")
    submit = SubmitField("Add Word")


class DeleteWordForm(FlaskForm):
    submit = SubmitField("Delete")  # Class for delete words


# Imagen form


class TaskImagenForm(FlaskForm):
    image_url = StringField(
        "Image URL", validators=[Optional()]
    )  # add url imagen from Pexel
    image = FileField("Upload Image", validators=[Optional()])  # add imagen from pc
    category = SelectField(
        "Category",
        choices=[
            ("Object", "Object"),
            ("Verb", "Verb"),
            ("Fruit", "Fruit"),
            ("Street", "Street"),
            ("Shop", "Shop"),
            ("Animals", "Animals"),
            ("Plants", "Plants"),
            ("People", "People"),
        ],
        validators=[DataRequired()],
    )
    japanese_word = StringField("Japanese Word", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation", validators=[Optional()])
    submit = SubmitField("Add Entry")


class DeleteImageForm(FlaskForm):
    submit = SubmitField("Delete")  # Class for delete imagens


# translator form


class AddWordFromResultForm(FlaskForm):
    japanese = StringField("Japanese", validators=[DataRequired()])
    english = StringField("English", validators=[DataRequired()])
    pronunciation = StringField("Pronunciation")
    submit = SubmitField("Add Word")
