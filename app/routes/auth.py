from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from app.models.user import User
from app import db


bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.home'))
            
        flash('Invalid Email or password', 'danger')
    
    return render_template('auth/login.html')   



@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate input data
        if not username or not username.strip():
            flash('Username is required', 'danger')
            return render_template('auth/register.html')
            
        if not email or not email.strip():
            flash('Email is required', 'danger')
            return render_template('auth/register.html')
            
        if not password or not password.strip():
            flash('Password is required', 'danger')
            return render_template('auth/register.html')
        
        # Clean the input
        username = username.strip()
        email = email.strip()
        
        # Check for existing users
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'warning')
            return render_template('auth/register.html')
            
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'warning')
            return render_template('auth/register.html')
        
        # Create and save user
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
            
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'danger')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base.html'))