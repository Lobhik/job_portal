from . import jobseeker
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Job, Application
from datetime import datetime

@jobseeker.route('/jobseeker/dashboard')
@login_required
def dashboard():
    if current_user.role != "Jobseeker":
        return "Access Denied", 403

    jobs = Job.query.order_by(Job.posted_at.desc()).all()
    return render_template('jobseeker/dashboard.html', jobs=jobs)

@jobseeker.route('/jobseeker/apply/<int:job_id>')
@login_required
def apply(job_id):
    if current_user.role != "Jobseeker":
        return "Access Denied", 403

    # Check if already applied
    existing = Application.query.filter_by(job_id=job_id, jobseeker_id=current_user.id).first()
    if existing:
        flash("You’ve already applied to this job.", "warning")
        return redirect(url_for('jobseeker.dashboard'))

    application = Application(
        job_id=job_id,
        jobseeker_id=current_user.id,
        applied_at=datetime.utcnow()
    )
    db.session.add(application)
    db.session.commit()
    flash("Applied successfully!", "success")
    return redirect(url_for('jobseeker.dashboard'))

@jobseeker.route('/jobseeker/applications')
@login_required
def my_applications():
    if current_user.role != "Jobseeker":
        return "Access Denied", 403

    applications = Application.query.filter_by(jobseeker_id=current_user.id).all()
    return render_template('jobseeker/applications.html', applications=applications)
