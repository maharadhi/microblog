from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Balaji'}
    posts = [
        {
            'author': {'username': 'Jadayu'},
            'body': "It's a cold day in Dallas!"
        },
        {
            'author': {'username': 'Sujata'},
            'body': "My name is Sujata"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)