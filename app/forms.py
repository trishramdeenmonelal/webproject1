from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email 
from flask import render_template, request, redirect, url_for, flash
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname  = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender', choices=[('', 'Select your CORRECT gender'),('M','Male'),('F','Female')])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    profilepic = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png'])])