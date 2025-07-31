from flask import Blueprint, render_template, request
from flask_login import login_required

bp = Blueprint('admin', __name__)

@bp.route('/admin')
def index():
    return render_template('admin/dashboard.html')

@bp.route('/admin/revenue')
#@login_required 
def revenue():
    # Placeholder for total revenue calculation logic
    total_revenue = 100000
    return render_template('admin/revenue.html', total_revenue=total_revenue)



















