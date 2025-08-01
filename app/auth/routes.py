from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .. import db, login_manager
from ..models import User
from .forms import RegisterForm, LoginForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully!", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash("Invalid credentials", "danger")
    return render_template('login.html', form=form)





@auth.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == "Admin":
        return redirect(url_for('admin.dashboard'))
    elif current_user.role == "Employer":
        return redirect(url_for('employer.dashboard'))
    elif current_user.role == "Jobseeker":
        return redirect(url_for('jobseeker.dashboard'))
    else:
        return "Unauthorized Role", 403





@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
