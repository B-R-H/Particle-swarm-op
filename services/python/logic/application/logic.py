import math

def assess_on_function(global_max,patricle_location):
	# Function exspecting 1 int and array. global_max and particle_location with 2 values for the particle location [x,y]
	# Returns None if new value not evaluated at a higer point if new max returns array [newmax,x,y]
	x=patricle_location[0]
	y=patricle_location[1]
	value = (5*math.sin(x/10)+5*math.cos(y/10)+5*math.sin(math.exp(y**2/10)+math.exp(x**2/10))*math.cos(x*y))-(0.001*(x**2+y**2))
	if value>global_max[0]:
		return [value,x,y]
	else:
		return global_max
