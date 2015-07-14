from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}
	posts = [
		{
			'author': {'nickname': 'Pete'},
			'body': 'It is a bit rainy today. Do you not enjoy the rain?'
		},
		{
			'author': {'nickname': 'Flag'},
			'body': 'I am a flag.'
		}
	]
	return render_template('index.html',
							title='Home',
							user = user,
							posts = posts)