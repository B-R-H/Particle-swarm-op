from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import *
from sqlalchemy.sql.expression import func
import requests
import time

@app.route('/start')
def start():
	run=Run_state.query.filter_by(flag="running particles").first()
	run.state = True
	db.session.commit()
	# try block needed to stop the intentional time out from causing trouble on the front end.
	try:
		requests.get("http://party:5003/move",timeout=1)
	except:
		pass
	return redirect(url_for('home'))

@app.route('/stop')
def stop():
	run=Run_state.query.filter_by(flag="running particles").first()
	run.state = False
	db.session.commit()
	return redirect(url_for('home'))

@app.route('/reset')
def reset():
	requests.get("http://frontend:5000/stop")
	time.sleep(.5)
	Iteration_couter.query.delete()
	db.session.commit()
	requests.get("http://party:5003/generate")
	return redirect(url_for('home'))

@app.route('/')
@app.route('/home')
def home():
	data = Iteration_couter.query.all()
	data_length = len(data)-1
	if str(data) != "[]":
		gmax = [data[data_length].max_value,data[data_length].x,data[data_length].y]
	else:
		gmax =[None,None,None]
	# button to start and stop process
	return render_template('home.html', title='Particle Swarm Optermisation', fx='z=5*sin(x/10)+5*cos(y/10)+5*sin(e^(y^2/10)+e^(x^2/10))*cos(x*y))-(0.001*(x^2+y^2)', gmax=gmax)