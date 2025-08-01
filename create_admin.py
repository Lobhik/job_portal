

from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash


app = create_app()

with app.app_context():
    admin_email = "admin@example.com"
    existing_admin = User.query.filter_by(email=admin_email).first()
    
    if not existing_admin:
        admin_user = User(
            email=admin_email,
            password=generate_password_hash("admin123", method='pbkdf2:sha256'),
            role="Admin"
        )
        db.session.add(admin_user)
        db.session.commit()
        print(" Admin user created successfully.")
    else:
        print("Admin already exists.")
