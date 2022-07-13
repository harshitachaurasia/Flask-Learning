from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User ,Post


posts = [
    {
        'author':'Dan',
        'title':'Blog Post 1',
        'content':'First blog content',
        'date_posted': 'April 20 2019'
    },
    {
        'author':'John Doe',
        'title':'Blog Post2',
        'content':'second blog content',
        'date_posted':'Dec 7 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in successfully",'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check again Email and Password','danger')
    return render_template('login.html',title='login',form=form)

