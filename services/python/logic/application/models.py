from application import db

class Functions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	function = db.Column(db.String(1000), nullable = False)

class Iteration_couter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	function_id = db.Column(db.Integer, db.ForeignKey('functions.id'))
	itteration = db.Column(db.Integer, nullable = False)
	max_value = db.Column(db.Float, nullable = False)
	x = db.Column(db.Float, nullable = False)
	y = db.Column(db.Float, nullable = False)

class Run_state(db.Model):
	flag = db.Column(db.String(100),primary_key=True)
	state = db.Column(db.Boolean, nullable = False)