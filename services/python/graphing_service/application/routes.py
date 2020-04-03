from application import app
from flask import render_template, redirect, url_for, request, jsonify
from application import graphing as gr
import matplotlib
matplotlib.use('Agg')


@app.route('/generate')
def generate():
	gr.base_figure_gen()
	return 'figure generated\n'

@app.route('/plot')
def plot():
	content = request.get_json()
	particles = []
	for i in content:
		particles.append([i['x'],i['y'],i['xv'],i['yv']])
	gr.overlay_particles(particles)
	return 'overlay generated\n'

@app.route('/figure')
def figure():
	return render_template('image.html')