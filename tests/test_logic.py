import pytest
from services.python import logic

def test_new_high():
	a = logic.assess_on_function(0,[15,0])
	assert a[0]>0
	assert a[1]==15
	assert a[2]==0

def test_old_high():
	assert logic.assess_on_function(100,[15,0])==None