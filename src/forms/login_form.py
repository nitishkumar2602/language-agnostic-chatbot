from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField
from wtforms.validators import Email


class LoginForm(FlaskForm):
    email = EmailField(validators=[Email()], id="login-email")
    password = PasswordField(id="login-password")

    submit = SubmitField(id="login-submit")
