from flask import Blueprint, render_template, request
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/home')
def home():
    return render_template('main/home.html')


@bp.route('/contact')
def contact():
    return render_template('main/contact.html')


@bp.route('/services')
def services():
    return render_template('main/services.html')

@bp.route('/about')
def about():
    return render_template('main/about.html')

@bp.route('/faqs')
def faqs():
    return render_template('main/faqs.html')

