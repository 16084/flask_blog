# blog app that allows users to register and post blogs 

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a469bb9b2a9e4dabd2b03e1fa2c816e8'

#list of post dictionaries 

posts = [
    
    {
        'author': "Diane Dumbong",
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'February 22, 2022'       
    },
    
    {
        'author': 'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'February 24, 2022'
    },
    
    {
        'author': 'Bob Doe',
        'title':'Blog Post 3',
        'content':'Third post content',
        'date_posted':'February 26, 2022'
    }
        
]

#routes

#route for homepage 
@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html', posts=posts) #call to render the home page template 

# route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

# route for login page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)