#lists
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = [] #Empty list used to save the values of zipped lists
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord): #point is an element inside the point list
    points.append("{}: {}, {}, {}".format(*point)) #Adding elements to the points empty list

    
for point in points: #Printing individual elements of the list points.
    print(point)