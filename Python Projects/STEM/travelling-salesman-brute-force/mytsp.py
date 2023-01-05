import random
import itertools

def calculate_distance(x_list,y_list):
	matrix=[]
	for iteration in range(len(x_list)):
		total=[]
		for n in range(len(x_list)):
			distance=(((x_list[iteration]-x_list[n])**2 + (y_list[iteration]-y_list[n])**2)**0.5)
			distance_rounded=round(distance, 2)
			total.append(distance_rounded)
		matrix.append(total)
	return matrix

def elimination(perm_list_alpha,points):
	perm_list_gamma=list(itertools.chain.from_iterable(perm_list_alpha))
	perm_list_gamma.sort()
	frick=list(set(perm_list_gamma))
	frick.pop(0)
	frick_me=sum(frick[0:points-1])
	return frick_me

num_of_points=4
x_axis=[]
y_axis=[]
for n in range(num_of_points):
	x=random.choice(range(1,11))
	y=random.choice(range(1,11))
	x_axis.append(x)
	y_axis.append(y)


permutations=calculate_distance(x_axis,y_axis)

final=elimination(permutations,num_of_points)
print(final)
print(x_axis)
print(y_axis)