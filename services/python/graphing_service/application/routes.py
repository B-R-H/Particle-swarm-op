from application import app
from flask import render_template, redirect, url_for, request, jsonify, send_file
from application import graphing as gr
import matplotlib
from PIL import Image
matplotlib.use('Agg')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/generate')
def generate():
	gr.base_figure_gen()
	return 'figure generated\n'

@app.route('/plot',methods=['POST'])
def plot():
	content = request.get_json()
	particles = []

	for i in range(len(content)):
		particles.append([content[str(i)]["x"],content[str(i)]["y"],content[str(i)]["xv"],content[str(i)]["yv"]])
	gr.overlay_particles(particles)
	return 'overlay generated\n'

@app.route('/figure')
def figure():
	return send_file("static/particle_plot.png", mimetype='image/png')