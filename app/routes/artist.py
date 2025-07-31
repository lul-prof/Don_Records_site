from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

bp = Blueprint('artist', __name__)



@bp.route('/artist')
def index():
    artist_name = "Artist Name"  # Replace with actual artist name logic
    return render_template('artist/dashboard.html', artist=artist_name)




@bp.route('/artist/upload_music', methods=['GET', 'POST'])
#@login_required
def upload_music():
    if request.method == 'POST':
        # Handle the file upload logic here
        # For example, save the file to a specific directory
        # and store the metadata in the database.
        pass
    
    return render_template('artist/upload_music.html')

@bp.route('/artist/beat_store')
#@login_required
def beat_store():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('artist/beat_store.html')


@bp.route('/artist/music_list')
#@login_required
def music_list():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('artist/music_list.html')


@bp.route('/artist/purchase')
#@login_required
def purchase():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('artist/purchase.html')


@bp.route('/artist/profile')
@login_required
def profile():
    # Fetch the artist's profile information from the database
    # and pass it to the template.
    return render_template('artist/profile.html')

@bp.route('/artist/music')
@login_required
def music():
    # Fetch the artist's music from the database
    # and pass it to the template.
    return render_template('artist/music.html')

@bp.route('/artist/analytics')
@login_required 
def analytics():
    # Fetch the artist's analytics data from the database
    # and pass it to the template.
    return render_template('artist/analytics.html')

@bp.route('/artist/settings')
@login_required     
def settings():
    # Fetch the artist's settings from the database
    # and pass it to the template.
    return render_template('artist/settings.html')

@bp.route('/artist/notifications')
@login_required
def notifications():
    # Fetch the artist's notifications from the database
    # and pass it to the template.
    return render_template('artist/notifications.html')

@bp.route('/artist/help')
@login_required
def help():
    # Fetch the help resources or FAQs for the artist
    # and pass it to the template.
    return render_template('artist/help.html')

@bp.route('/artist/logout')
@login_required
def logout():
    # Handle the logout logic here
    # For example, call logout_user() from flask_login
    return redirect(url_for('main.index'))


