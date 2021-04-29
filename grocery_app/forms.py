from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, GroceryItem, ItemCategory, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Grocery Title', validators=[DataRequired(), Length(min=3, max=100)])
    address = StringField('Grocery Address', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name      = StringField('Item name',  validators=[DataRequired(), Length(min=3, max=100)])
    price     = FloatField('Price',       validators=[DataRequired()])
    category  = SelectField('Catagory',   choices=ItemCategory.choices())
    photo_url = StringField('Photo_url',  validators=[URL()])
    store     = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit    = SubmitField('Submit')

class SignUpForm(FlaskForm):
    """Form for signing up"""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Form for logging in"""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
