import os
from app import create_app, db
from werkzeug.security import generate_password_hash
from app.models.user import User

app = create_app()

def create_default_users():
    # Create admin user if it doesn't exist (check both email AND username)
    existing_user = User.query.filter(
        (User.email == 'admin1@gmail.com') | (User.username == 'admin')
    ).first()
    
    if existing_user is None:
        admin = User(
            username='admin', 
            email='admin@gmail.com', 
            is_admin=True
        )
        admin.set_password('admin123')
        
        db.session.add(admin)
        db.session.commit()
        print('Admin user created!')
    else:
        print(f'Admin user already exists: {existing_user.username} ({existing_user.email})')


if __name__ == '__main__':
    # Clear console for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')
    
    with app.app_context():
        db.create_all()  # Create tables first
        create_default_users()  # Then create admin user
    
    print('Admin setup complete')
    print("🚀 Starting BFL Apparel application...")

    app.run(debug=True)
    