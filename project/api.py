from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, make_response
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from . import db
from datetime import datetime
import json

api = Blueprint('api', __name__, url_prefix='/api')

# API Endpoint to get all product categories
@api.route('/product_categories', methods=['GET'])
@login_required
def get_product_categories():
    product_categories = ProductCategory.query.all()
    output = []
    for p in product_categories:
        productCategory = {}
        productCategory['id'] = p.id
        productCategory['name'] = p.name
        productCategory['description'] = p.description
        productCategory['created_at'] = p.created_at
        productCategory['modified_at'] = p.modified_at
        productCategory['deleted_at'] = p.deleted_at
        output.append(productCategory)
    return jsonify({'product_categories' : output})

# API Endpoint to get product category by id
@api.route('/product_category/<int:id>', methods=['GET'])
@login_required
def get_product_category_by_id(id: int):
    product_category = ProductCategory.query.filter_by(id = id).first()
    if product_category is None:
        return jsonify({ 'error': 'Product category does not exist'}), 404
    return jsonify(product_category)

# API Endpoint to update product category by id
@api.route('/product_category/<int:id>', methods=['PATCH'])
@login_required
def update_product_category_by_id(id: int):
    if request.method == 'PATCH':
        product_category = ProductCategory.query.filter_by(id = id).first()
        if product_category is None:
            return jsonify({ 'error': 'Product category does not exist'}), 404
        request_data = request.get_json()
        name = request_data['productCategoryName']
        description = request_data['productCategoryDescription']
        created_at = request_data['productCreatedAt']
        modified_at = datetime.now()
        product_category.modified_at = modified_at
        product_category.name = name
        product_category.description = description
        db.session.commit()
        return jsonify({"message": "Product Category updated successfully", "name": name, "description": description, "created_at":created_at, "id": product_category.id, "modified_at":modified_at})
    else:
        return jsonify({ 'error': 'Product category could not be updated'}), 404
    # json_data = request.get_json()
    # data = product_category.update(dict(json_data))
    # db.session.commit()
    # return jsonify({"message": "Product Category updated successfully"})

# API Endpoint to create product category 
@api.route('/create_product_category', methods=['POST'])
@login_required
def create_product_category():
    if request.method == 'POST':
        request_data = request.get_json()
        name = request_data['productCategoryName']
        description = request_data['productCategoryDescription']
        created_at = datetime.now()
        print(name)
        print(description)
        print(created_at)
        new_product_category = ProductCategory(name=name, description=description, created_at=created_at)
        db.session.add(new_product_category)
        db.session.commit()
        product_category = ProductCategory.query.filter_by(created_at = created_at).first()
        return jsonify({"message": "Product Category created successfully", "name": name, "description": description, "created_at":created_at, "id": product_category.id})
    else:
        return jsonify({ 'error': 'Product category could not be created'}), 404

# API Endpoint to delete product category 
@api.route('/delete_product_category/<int:id>', methods=['DELETE'])
def delete_product_category_by_id(id: int):
    if request.method == 'DELETE':
        product_category = ProductCategory.query.filter_by(id = id).first()
        if product_category is None:
            return jsonify({ 'error': 'Product category does not exist'}), 404
        if product_category:
            db.session.delete(product_category)
            db.session.commit() 
            return jsonify({"message": "Product Category Deleted successfully"})
