from application import app
from flask import render_template, redirect, url_for, request

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
	gmax=[10,13.67,25.43]
	return render_template('home.html', title='Particle Swarm Optermisation', fx='z=5*sin(x/10)+5*cos(y/10)+5*sin(e^(y^2/10)+e^(x^2/10))*cos(x*y))-(0.001*(x^2+y^2)', gmax=gmax)