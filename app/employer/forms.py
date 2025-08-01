from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class JobPostForm(FlaskForm):
    title = StringField('Job Title', validators=[InputRequired()])
    description = TextAreaField('Job Description', validators=[InputRequired()])
    submit = SubmitField('Post Job')
