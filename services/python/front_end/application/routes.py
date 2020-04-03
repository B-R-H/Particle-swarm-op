from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import *
from sqlalchemy.sql.expression import func


@app.route('/')
@app.route('/home')
def home():
	data = Iteration_couter.query.all()
	data_length = len(data)-1
	gmax = [data[data_length].max_value,data[data_length].x,data[data_length].y]
	# button to start and stop process
	return render_template('home.html', title='Particle Swarm Optermisation', fx='z=5*sin(x/10)+5*cos(y/10)+5*sin(e^(y^2/10)+e^(x^2/10))*cos(x*y))-(0.001*(x^2+y^2)', gmax=gmax)