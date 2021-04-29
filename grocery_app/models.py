from sqlalchemy_utils import URLType
from flask_login import UserMixin
from grocery_app import db
from grocery_app.utils import FormEnum

class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    
    # add relationship to user
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

class GroceryItem(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(
        db.Integer, db.ForeignKey('grocery_store.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    
    # add relationship to user
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User', secondary='shopping_list', back_populates='shopping_list_items')

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) # cannot be null, MUST be entered
    password = db.Column(db.String(100), nullable=False) # cannot be null, MUST be entered

    shopping_list_items = db.relationship("GroceryItem", secondary='shopping_list', back_populates='created_by')

# shopping_list_table
shopping_list_table = db.Table('shopping_list',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('grocery_item_id', db.Integer, db.ForeignKey('grocery_item.id'))
)
