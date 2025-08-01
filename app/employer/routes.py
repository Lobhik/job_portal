from . import employer
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Job
from .forms import JobPostForm
from ..models import Application, User



@employer.route('/employer/dashboard')
@login_required
def dashboard():
    if current_user.role != "Employer":
        return "Access Denied", 403

    jobs = Job.query.filter_by(employer_id=current_user.id).all()
    return render_template('employer/dashboard.html', jobs=jobs)

@employer.route('/employer/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != "Employer":
        return "Access Denied", 403

    form = JobPostForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            employer_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('employer.dashboard'))
    
    return render_template('employer/post_job.html', form=form)





@employer.route('/employer/job/<int:job_id>/applications')
@login_required
def job_applications(job_id):
    if current_user.role != "Employer":
        return "Access Denied", 403

    job = Job.query.filter_by(id=job_id, employer_id=current_user.id).first()
    if not job:
        return "Job not found or unauthorized.", 404

    applications = Application.query.filter_by(job_id=job.id).all()
    return render_template('employer/job_applications.html', job=job, applications=applications)
