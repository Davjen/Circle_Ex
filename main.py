from Classes.MyCircle import Circle
from Classes.SparseArray import SparseArray

if __name__ == '__main__':
    c1 = Circle(10)
    c2 = Circle.from_diameter(25)
    c3 = Circle.from_area(223)

    sum_of_circles = c1+c2

    print(c1)

    print(c1<c2)

    list_of_circles=[c1, c2, c3]
    for i,circle in enumerate(list_of_circles):
        print(f"{i}. {circle}")
    list_of_circles.sort()
    for i,circle in enumerate(list_of_circles):
        print(f"{i}. {circle}")
