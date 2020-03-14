"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash
from app.forms import MyForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
import psycopg2    
import os    
from datetime import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/allprofiles/<userid>')
def fullprofile(userid):
    """Render the website's about page."""
    user=UserProfile.query.get(userid)
    return render_template('fullprofile.html', user=user, startdate=format_date_joined(12, 2, 2018))

@app.route('/allprofiles/')
def Users(): 
    users=db.session.query(UserProfile).all()
    return render_template('allprofiles.html', users=users)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profile/', methods=('GET', 'POST'))
def profile():
    form = MyForm()
    if request.method=='POST' and form.validate_on_submit():
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        gender=request.form['gender']
        email=request.form['email']
        location=request.form['location']
        biography=request.form['biography']
        profilepic = form.profilepic.data
        
        
        filename=secure_filename(profilepic.filename)
        profilepic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        userprofile = UserProfile(firstname,lastname,gender,email,location,biography, filename)
        db.session.add(userprofile)
        db.session.commit()
        
        flash('Yup. you been added')
        return redirect(url_for('Users'))
        
    return render_template('profile.html', form=form)
    
    
    
# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def format_date_joined(month,day, year):
    x = datetime(year,month,day) 
    return(x.strftime("%B" + " " +"%d"+ "  "+"%Y"))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
