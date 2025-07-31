from django.shortcuts import redirect
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required

bp = Blueprint('blog', __name__)

@bp.route('/blog')
def index():
    return render_template('blog/dashboard.html')

@bp.route('/blog/create_post', methods=['GET', 'POST'])
#@login_required
def create_post():
    if request.method == 'POST':
        # Handle post creation logic here
        pass
    
    return render_template('blog/create_post.html')

@bp.route('/blog/edit_post/<int:post_id>', methods=['GET', 'POST'])
#@login_required
def edit_post(post_id):
    if request.method == 'POST':
        # Handle post editing logic here
        pass
    
    return render_template('blog/edit_post.html', post_id=post_id)  

@bp.route('/blog/post_detail/<int:post_id>')
def post_detail(post_id):
    # Fetch post details from the database using post_id
    return render_template('blog/post_detail.html', post_id=post_id)

@bp.route('/blog/delete_post/<int:post_id>', methods=['POST'])
#@login_required    
def delete_post(post_id):
    # Handle post deletion logic here
    return redirect(url_for('blog.index'))

@bp.route('/blog/manage_posts')
#@login_required    
def manage_posts():
    # Fetch all posts from the database
    return render_template('blog/manage_posts.html')

@bp.route('/blog/comments/<int:post_id>', methods=['GET', 'POST'])
#@login_required    
def comments(post_id):
    if request.method == 'POST':
        # Handle comment submission logic here
        pass
    
    # Fetch comments for the post from the database
    return render_template('blog/comments.html', post_id=post_id)

@bp.route('/blog/author/<int:author_id>')
def author_posts(author_id):
    # Fetch posts by the author from the database using author_id
    return render_template('blog/author_posts.html', author_id=author_id)

@bp.route('/blog/categories')
def categories():
    # Fetch all categories from the database
    return render_template('blog/categories.html')

