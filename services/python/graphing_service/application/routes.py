from application import app
from flask import render_template, redirect, url_for, request, jsonify
from application import graphing as gr
import matplotlib
matplotlib.use('Agg')


@app.route('/generate')
def generate():
	gr.base_figure_gen()
	return 'figure generated\n'

@app.route('/plot',methods=['POST'])
def plot():
	content = request.get_json()
	particles = []
	# particles = [[content["1"]["x"],content["1"]["y"],content["1"]["xv"],content["1"]["yv"]],[content["0"]["x"],content["0"]["y"],content["0"]["xv"],content["0"]["yv"]]]

	for i in range(len(content)):
		particles.append([content[str(i)]["x"],content[str(i)]["y"],content[str(i)]["xv"],content[str(i)]["yv"]])
	gr.overlay_particles(particles)
	return 'overlay generated\n'

@app.route('/figure')
def figure():
	return render_template('image.html')