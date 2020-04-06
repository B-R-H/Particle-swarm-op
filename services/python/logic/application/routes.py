from application import app, db
from flask import render_template, redirect, url_for, request, jsonify
from application.models import *
from sqlalchemy.sql.expression import func
from application import logic as L

# define routes for / & /home, this function will be called when these are accessed
@app.route('/logic',methods=['POST'])
def logic():
	previous_itteration = Iteration_couter.query.filter_by(id=db.session.query(func.max(Iteration_couter.id))).first()
	if previous_itteration == None:
		global_max = [-100000000,0,0]
		function_id = 1
		p_it=0
	else:
		global_max = [previous_itteration.max_value,previous_itteration.x,previous_itteration.y] 
		function_id = previous_itteration.function_id
		p_it=previous_itteration.itteration
	content = request.get_json()
	stack = []
	for i in range(len(content)):
		stack.append([content[str(i)]['x'],content[str(i)]['y']]) 
	for i in stack:
		global_max=L.assess_on_function(global_max,i)
	itteration = Iteration_couter(
		function_id = function_id,
		max_value = global_max[0],
		x = global_max[1],
		y = global_max[2],
		itteration = p_it + 1
	)
	db.session.add(itteration)
	db.session.commit()
	return jsonify({'Value':global_max[0],'x':global_max[1],'y':global_max[2]})