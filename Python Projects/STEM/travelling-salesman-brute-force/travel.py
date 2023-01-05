import random
import matplotlib.pyplot as plt
import tkinter as tk

class Point:
	def __init__(self, x, y):
		self.x=x
		self.y=y

def calculate_distance(points_list):
	total=0
	for n in range(len(points)-1):
		distance=(((points[n].x-points[n+1].x)**2 + (points[n].y-points[n+1].y)**2)**0.5)
		total+=distance;
	return total

def printer(x_values,y_values,point_path,min_dist):
	window=tk.Tk()
	window.title("Travelling Salesman Problem")
	path=tk.Label(window, text=f"The Smallest Path:{point_path}")
	dista=tk.Label(window, text=f"The Distance:{min_dist}")
	path.pack()
	dista.pack()
	plt.scatter(x_values,y_values)
	plt.show()
	window.mainloop()
		
points=[]
number_of_point=4
smallest_path=[]
record_distance=0
x_axis=[]
y_axis=[]

for n in range(number_of_point):
	x=random.choice(range(1,11))
	y=random.choice(range(1,11))
	point=Point(x,y)
	points.append(point)
	x_axis.append(x)
	y_axis.append(y)

dist=calculate_distance(points)
record_distance=dist

slice_object=slice(number_of_point)
smallest_path=points.copy()

a=[]
for n in range(len(smallest_path)):
	a.append((smallest_path[n].x,smallest_path[n].y))


printer(x_axis,y_axis,a,record_distance)

'''
plt.scatter(x_axis,y_axis)
plt.show()

print("The Smallest Path:", str(a))
print("The Distance:", str(record_distance))'''