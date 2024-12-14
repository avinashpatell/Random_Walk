from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
	rw=RandomWalk(50000)
	rw.fill_walk()
	plt.figure(dpi=128, figsize=(10, 6))
	point_numbers=list(range(rw.num_points))
	plt.axes().get_xaxis().set_visible(False)
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none', s=1)
	plt.axis('off')
	plt.show()
	
	keep_running=input("Keep running the walk? (y/n): ")

	if keep_running=='n':
		break

