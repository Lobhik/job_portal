from . import admin
from flask import render_template, request
from flask_login import login_required, current_user
from ..models import Job, User
from datetime import datetime, timedelta
from sqlalchemy import func



@admin.route('/admin/dashboard')
@login_required
def dashboard():
    if current_user.role != "Admin":
        return "Access Denied", 403

    now = datetime.utcnow()
    start_of_day = datetime(now.year, now.month, now.day)
    start_of_week = start_of_day - timedelta(days=start_of_day.weekday())
    start_of_month = datetime(now.year, now.month, 1)
    start_of_year = datetime(now.year, 1, 1)

    # def count_since(model, date):
    #     return model.query.filter(model.created_at >= date).count()

    def count_since(model_or_query, date):
        if hasattr(model_or_query, 'query'):
            # It's a model class
            return model_or_query.query.filter(model_or_query.created_at >= date).count()
        else:
            # It's already a query object
            return model_or_query.filter(model_or_query.column_descriptions[0]['type'].created_at >= date).count()

    stats = {
        'jobs': {
            'day': count_since(Job, start_of_day),
            'week': count_since(Job, start_of_week),
            'month': count_since(Job, start_of_month),
            'year': count_since(Job, start_of_year),
        },
        'employers': {
            'day': count_since(User.query.filter_by(role='Employer'), start_of_day),
            'week': count_since(User.query.filter_by(role='Employer'), start_of_week),
            'month': count_since(User.query.filter_by(role='Employer'), start_of_month),
            'year': count_since(User.query.filter_by(role='Employer'), start_of_year),
        },
        'jobseekers': {
            'day': count_since(User.query.filter_by(role='Jobseeker'), start_of_day),
            'week': count_since(User.query.filter_by(role='Jobseeker'), start_of_week),
            'month': count_since(User.query.filter_by(role='Jobseeker'), start_of_month),
            'year': count_since(User.query.filter_by(role='Jobseeker'), start_of_year),
        },
    }

    return render_template('admin/dashboard.html', stats=stats)




@admin.route('/admin/manage/jobs')
@login_required
def manage_jobs():
    if current_user.role != "Admin":
        return "Access Denied", 403

    jobs = Job.query.order_by(Job.created_at.desc()).all()
    return render_template('admin/manage_jobs.html', jobs=jobs)



@admin.route('/admin/job/delete/<int:job_id>')
@login_required
def delete_job(job_id):
    if current_user.role != "Admin":
        return "Access Denied", 403

    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted successfully", "success")
    return redirect(url_for('admin.manage_jobs'))




@admin.route('/admin/manage/employers')
@login_required
def manage_employers():
    if current_user.role != "Admin":
        return "Access Denied", 403

    employers = User.query.filter_by(role="Employer").order_by(User.created_at.desc()).all()
    print("test",employers )
    return render_template('admin/manage_employers.html', employers=employers)




@admin.route('/admin/employer/delete/<int:user_id>')
@login_required
def delete_employer(user_id):
    if current_user.role != "Admin":
        return "Access Denied", 403

    employer = User.query.get_or_404(user_id)
    db.session.delete(employer)
    db.session.commit()
    flash("Employer deleted successfully", "success")
    return redirect(url_for('admin.manage_employers'))
