from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin.route('/product_category')
@login_required
def product_category():
    # return render_template('admin/admin_base.html')
    return render_template('admin/product_category.html')