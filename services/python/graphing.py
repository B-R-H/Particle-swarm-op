import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def figure_gen():
	delta = 0.5
	x = np.arange(-100,100,delta)
	y = np.arange(-100,100,delta)
	X,Y=np.meshgrid(x,y)
	Z =  (5*np.sin(X/10)+5*np.cos(Y/10)+5*np.sin(np.exp(Y**2/10)+np.exp(X**2/10))*np.cos(X*Y))-(0.001*(X**2+Y**2))

	fig, ax = plt.subplots()
	CS = ax.contour(X,Y,Z)
	ax.clabel(CS,inline=1,fontsize=10)
	ax.set_title('fig1')

	plt.show()

figure_gen()