# Shape-Color-Position-Recognition
Python program to Find shape,colour and position of objects in an image and match them with same objects in different image

# Given:
* A board - having 9 Objects in 9 Positions.Figure 1 shows a sample board. Positions on “board” are numbered as shown in Figure.
* 5 images of containers - each having 16 Objects in 16 Positions. Figure 2 shows a sample “container”. Positions on container are numbered as shown in Figure.

Each Object is defined by three features, viz. Shape,Sizeand Color

![capture1](https://cloud.githubusercontent.com/assets/14962324/21743583/fdd7fa10-d52a-11e6-855e-4a8436da6156.PNG)

# Output
* Code returns a python list having 9 python tuples. Each tuple has three elements, first element is the position number on the “board”, second element is color of object viz, “red”, “blue”, “green” and “yellow”, third element is shape of object viz, “Triangle”,“4-sided” and “Circle”.

* For each object in the “board”, find the matching object in the “container”. Objects are considered a match only if all the three features of an object viz, Shape, Size and Color in the “board”matches exactly with an object inthe “container”.

# Example:

* Considering Figure 1, the output should be: [(1, “red”, “4-sided”), (2, “red”, “Triangle”), (3, “yellow”, “Triangle”), (4, “green”, “Circle”), (5, “red”, “4-sided”), (6, “blue”, “4-sided”), (7, “red”, “Circle”), (8, “yellow”, “4-sided”), (9, “yellow”, “4-sided”)]

* Expected output for sample “board” and “container” shown in Figure 1and Figure 2 : [(1, 16), (2, 5), (3, 9), (4, 4), (5, 11), (6, 3), (7, 7), (8, 1), (9, 8)]

