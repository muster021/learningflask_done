from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired("Please enter your first name")])
    last_name = StringField("Last Name", validators=[DataRequired("Please enter your last name")])
    email = StringField("Email", validators=[DataRequired("Please enter your email adress"), Email("Please enter a valid email adress")])
    password = PasswordField("Password", validators=[DataRequired("Please a password"), Length(min=6, message="Password must be 6 characters or more")])
    submit = SubmitField("Sign Up", validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email adress"), Email("Please enter a valid email adress")])
    password = PasswordField("Password", validators=[DataRequired("Please enter your password")])
    submit = SubmitField("Sign in")

class AddressForm(FlaskForm):
    address = StringField("Address", validators=[DataRequired("Please enter an adress")])
    submit = SubmitField("Search")
