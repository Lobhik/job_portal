from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256))
    role = db.Column(db.String(50))  # Admin, Employer, Jobseeker
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    applications = db.relationship('Application', backref='job', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    jobseeker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)