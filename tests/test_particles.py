import pytest

from services/python import Particle

p1 = Particle.Particle()
p2 = Particle.Particle()
p3 = Particle.Particle(xuper=1,xlower=0,yuper=1,ylower=0)
p1x=p1.get_postion_x()
p1y=p1.get_postion_y()
p2x=p2.get_postion_x()
p2y=p2.get_postion_y()
p3x=p3.get_postion_x()
p3y=p3.get_postion_y()
p1xv=p1.get_velosity_x()
p1yv=p1.get_velosity_y()
p2xv=p2.get_velosity_x()
p2yv=p2.get_velosity_y()
p3xv=p3.get_velosity_x()
p3yv=p3.get_velosity_y()

def test_x_location():
	assert p1x<=10 and p1x>=-10
	assert p2x<=10 and p2x>=-10
	assert p3x<=1 and p3x>=0
	assert p1x!=p2x or p1x!=p3x

def test_y_location():
	assert p1y<=10 and p1y>=-10
	assert p2y<=10 and p2y>=-10
	assert p3y<=1 and p3y>=0
	assert p1y!=p2y or p1y!=p3y

def test_x_velosity():
	assert p1xv<=20*0.1 and p1xv>=-20*0.1
	assert p2xv<=20*0.1 and p2xv>=-20*0.1
	assert p3xv<=1*0.1 and p3xv>=-1*0.1
	assert p1xv!=p2xv or p1xv!=p3xv

def test_y_velosity():
	assert p1yv<=20*0.1 and p1yv>=-20*0.1
	assert p2yv<=20*0.1 and p2yv>=-20*0.1
	assert p3yv<=1*0.1 and p3yv>=-1*0.1
	assert p1yv!=p2yv or p1yv!=p3yv