from application import app, db
from flask import render_template, redirect, url_for, request, jsonify
import logic

# define routes for / & /home, this function will be called when these are accessed
@app.route('/logic',methods=['GET','POST'])
def logic():
	data = itteration.query(func.max(id))
	global_max = [data.max_value,data.x,data.y] 
	content = request.get_json()
	stack = []
	for i in content:
		stack.append([i['x'],i['y']]) 
	for i in stack:
		global_max=logic.assess_on_function(global_max,i)
	# update datbse
	return jsonify({'Value':global_max[0],'x':global_max[1],'y':global_max[2]})