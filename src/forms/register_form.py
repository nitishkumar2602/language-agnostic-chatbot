from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import Email


class RegisterForm(FlaskForm):
    full_name = StringField(id="register-name")
    email = EmailField(validators=[Email()], id="register-email")
    password = PasswordField(id="register-password")

    submit = SubmitField(id="register-submit")
