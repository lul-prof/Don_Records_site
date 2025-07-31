from django.shortcuts import redirect
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required

bp = Blueprint('payment', __name__)

@bp.route('/payment')
def index():
    return render_template('payment/checkout.html')
