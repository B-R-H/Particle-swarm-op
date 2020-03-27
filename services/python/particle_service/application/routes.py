from application import app, db
from flask import url_for, request, jsonify
import Particle

partilces = []

#trigger for reset of partilces on request 
@app.route('/generate')
def generate():
	global partilces
	partilces = []
	for i in range(100):
		partilces.append(Particle.Particle(xuper=100,xlower=-100,yuper=100,ylower=-100))
	return "partilces generated"

@app.route('/move', methods = ['GET','POST'])
def move():

	flag = Run_state.query.filter_by(flag='running particles').first()
	run_state = flag.state
	global_max =None

	while run_state:
		# pulls from the databse to see if it should be running.
		flag = Run_state.query.filter_by(flag='running particles').first()
		run_state = flag.state
		global partilces
	    partile_location={}
	    particle_data={}
	    for i in range(len(partilces)):
	    	if global_max!=None:
	       		particles[i].update(global_max[0],global_max[1])
	       	partile_location[i]={
	       		'x':particles[i].get_postion_x(),
	       		'y':particles[i].get_postion_y()
	       	}
	       	particle_data[i]={
	       		'x':particles[i].get_postion_x(),
	       		'y':particles[i].get_postion_y(),
	       		'xv':particles[i].get_velosity_x(),
	        	'yv':particles[i].get_velosity_y()
	      	}
	    ljson = jsonify(partile_location)
	    djson = jsonify(particle_data)
	    # post request to logic function that will return global max
	    # post request to graphing function to update postions
	    content = request.get_json()
	   	global_max=[content['x'],content['y']]
	    
	    
    return "run state not true"

        