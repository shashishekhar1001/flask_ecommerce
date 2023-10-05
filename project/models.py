from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

class ProductInventory(db.Model):
    __tablename__ = 'product_inventory'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    qty = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    # One-to-one relationship with Product
    product = db.relationship('Product', back_populates='product_inventory', uselist=False)

class Discount(db.Model):
    __tablename__ = 'discount'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    discount_percent = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    # Establish a one-to-many relationship with the Product model
    products = db.relationship('Product', backref='discount', lazy=True)

class Product(db.Model):
    __tablename__ = 'product'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    SKU = db.Column(db.String(100))
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'), nullable=False)
    product_category = db.relationship('ProductCategory', backref=db.backref('products', lazy=True))
    # One-to-one relationship with ProductInventory
    product_inventory_id = db.Column(db.Integer, db.ForeignKey('product_inventory.id'), unique=True, nullable=False)
    product_inventory = db.relationship('ProductInventory', back_populates='product')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    # One Product can have one discount
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
    # Establish a one-to-many relationship with ProductImage model
    images = db.relationship('ProductImage', backref='product', lazy=True)

class ProductImage(db.Model):
    __tablename__ = 'product_image'
    # __table_args__ = {'extend_existing': True} #Add this if the table already exists in db
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

