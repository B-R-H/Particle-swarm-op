import random as r 

def bounded_value(value,lowerbound,upperbound):
	#function to bound a value within two limits 
	if value<min:
		return min
	elif value>max:
		return max
	else:
		return value

class Particle:
	def __init__(self,xuper = 10,xlower=-10,yuper =10,ylower=-10):
		self.x = (xuper - xlower)*r.random + xlower
		self.y = (yuper - ylower)*r.random + ylower
		self.xv = ((xuper -	xlower)*r.random + xlower)*0.05
		self.yv = ((yuper - ylower)*r.random + ylower)*0.05
		self.xuper = xuper
		self.xlower = xlower
		self.yuper = yuper
		self.ylower = ylower
		#velosity limits so that the particle can travel a maximum of 10% of the sample space in one move
		self.xvuper = xuper-xlower*0.1
		self.xvlower = xlower-xuper*0.1
		self.yvuper = yuper-ylower*0.1
		self.yvlower = ylower-yuper*0.1

	def get_postion_x():
		# returns the x postion of the particle
		return self.x

	def get_postion_y():
		# returns the y postion of the particle
		return self.y

	def get_velosity_x():
		# returns the x velosity of the particle
		return self.xv

	def get_velosity_y():
		# returns the y velosity of the particle
		return self.yv

	def update(gx,gy):
		# updates the postion and velosity of the particle based on target cordinates
		xdif = gx - self.x
		ydif = gy - self.y
		xvupdate = xdif*0.05
		yvupdate = ydif*0.05
		self.xv = bounded_value(self.xv+xvupdate,self.xvlower,self.xvuper)
		self.yv = bounded_value(self.yv+yvupdate,self.yvlower,self.yvuper)
		# update the postion of the particles
		self.x = bounded_value(self.x+self.xv,self.xlower,self.xuper)
		self.y = bounded_value(self.y+self.yv,self.ylower,self.yuper)
		# decay on the velosity to slow particles over time if they are close to the global maximum
		self.xv*=0.98
		self.yv*=0.98