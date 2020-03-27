import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def base_figure_gen():
	delta = 0.5
	x = np.arange(-100,100,delta)
	y = np.arange(-100,100,delta)
	X,Y=np.meshgrid(x,y)
	Y2=(Y**2)/10
	eY2=np.exp(Y2)
	X2=(X**2)/10
	eX2=np.exp(X2)
	Z =  (5*np.sin(X/10)+5*np.cos(Y/10)+5*np.sin(eY2+eX2)*np.cos(X*Y))-(0.001*(X**2+Y**2))
	fig, ax = plt.subplots()
	CS = ax.contour(X,Y,Z,linewidths=.5)
	plt.axis('off')
	plt.savefig("contour_plot.png",dpi = 600,bbox_inches='tight',pad_inches = 0)
	plt.clf()

def overlay_particles(particles):
	x=[]
	y=[]
	xv=[]
	yv=[] 
	for i in particles:
		x.append(i[0])
		y.append(i[1])
		xv.append(i[2])
		yv.append(i[3])
	im = plt.imread('contour_plot.png')
	implot = plt.imshow(im,extent=[-100, 100, -100, 100])
	plt.scatter(x,y,c='r',s=1)
	plt.quiver(x,y,xv,yv,color='r',width=0.005)
	plt.savefig("static.Particle_plot.png",dpi = 600,bbox_inches='tight',pad_inches = 0)
	plt.clf()