from application import app, db, Particle
from flask import url_for, request, jsonify
from application.models import *
import requests

partilces = []

#trigger for reset of partilces on request 
@app.route("/generate")
def generate():
	global partilces
	partilces = []
	for i in range(100):
		partilces.append(Particle.Particle(xuper=75,xlower=-75,yuper=75,ylower=-75))
	return "partilces generated"

@app.route("/move", methods = ["GET","POST"])
def move():

	global partilces
	if len(partilces)!=100:
		return "partilces not generated correctly"

	flag = Run_state.query.filter_by(flag="running particles").first()
	run_state = flag.state
	global_max = None

	while run_state:
		# pulls from the databse to see if it should be running.
		flag = Run_state.query.filter_by(flag="running particles").first()
		run_state = flag.state
		partile_location={}
		particle_data={}
		for i in range(len(partilces)):
			if global_max!=None:
				partilces[i].update(global_max[0],global_max[1])
			partile_location[i]={
				"x":partilces[i].get_postion_x(),
				"y":partilces[i].get_postion_y()
			}
			particle_data[i]={
				"x":partilces[i].get_postion_x(),
				"y":partilces[i].get_postion_y(),
				"xv":partilces[i].get_velosity_x(),
				"yv":partilces[i].get_velosity_y()
			}
		gmax_responce = requests.post("http://logic:5002/logic",json=partile_location)
		requests.post("http://graphing:5001/plot",json=particle_data)
		gmax_responce = gmax_responce.json()
		global_max=[gmax_responce["x"],gmax_responce["y"]]
	return "run state not true"

        