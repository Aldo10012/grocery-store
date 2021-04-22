from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Grocery Title', validators=[DataRequired(), Length(min=3, max=100)])
    address = StringField('Grocery Address', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name      = StringField('Item name',  validators=[DataRequired(), Length(min=3, max=100)])
    price     = FloatField('Price',       validators=[DataRequired()])
    category  = SelectField('Catagory',   choices=ItemCategory.choices())
    photo_url = StringField('Photo_url',  validators=[URL])
    store     = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank-False)
    submit    = SubmitField('Submit')
    
