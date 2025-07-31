from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

bp = Blueprint('producer', __name__)



@bp.route('/producer')
def index():
    return render_template('producer/dashboard.html')


@bp.route('/producer/upload_beat', methods=['GET', 'POST'])
#@login_required
def upload_beat():
    if request.method == 'POST':
        # Handle the file upload logic here
        # For example, save the file to a specific directory
        # and store the metadata in the database.
        pass
    
    return render_template('producer/upload_beat.html')

@bp.route('/producer/beat_list')
#@login_required
def beat_list():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('producer/beat_list.html')


@bp.route('/producer/collaboration')
#@login_required
def collaboration():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('producer/collaboration.html')


@bp.route('/producer/purchase')
#@login_required
def purchase():
    beat= {
        'title': 'Sample Beat',
        'price': 1000.00
    }
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('producer/purchase.html', beat=beat, buyer_name="John Doe")