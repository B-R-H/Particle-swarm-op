from aplication import app
from flask import render_template, redirect, url_for, request, jsonify
import graphing as gr


@app.route('/generate')
def generate():
	gr.base_figure_gen()
	return 'figure generated'

@app.route('/plot')
def plot():
	content = request.get_json()
	particles = []
	for i in content:
		particles.append([i['x'],i['y'],i['xv'],i['yv']])
	gr.overlay_particles(particles)
	return 'overlay generated'

@app.route('/figure')
def figure():
	return render_template('image.html')