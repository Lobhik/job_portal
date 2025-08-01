from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import redirect, url_for

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_portal.db'


    db.init_app(app)
    login_manager.init_app(app)
  

    from .auth.routes import auth
    from .admin.routes import admin as admin_bp
    from .employer.routes import employer as employer_bp
    from .jobseeker.routes import jobseeker as jobseeker_bp

    app.register_blueprint(auth)
    app.register_blueprint(admin_bp)
    app.register_blueprint(employer_bp)
    app.register_blueprint(jobseeker_bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    

    return app
