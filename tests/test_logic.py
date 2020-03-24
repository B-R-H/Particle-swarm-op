import pytest
from services.python.logic.application import logic

def test_new_high():
	a = logic.assess_on_function([0,-12,20],[15,0])
	assert a[0]>0
	assert a[1]==15
	assert a[2]==0

def test_old_high():
	assert logic.assess_on_function([100,200,-150.2314],[15,0])==[100,200,-150.2314]
