from Classes.MyCircle import MyCircle

if __name__ == '__main__':
    c1 = MyCircle(radius=10)
    c2 = MyCircle(diameter=50)
    c3 = MyCircle(circle_area=223)

sum_of_circles = c1.__add__(c2)

print(c1.__str__())

print(c1.__lt__(c3))

list_of_circles=[c1, c2, c3]
for i,circle in enumerate(list_of_circles):
    print(f"{i}. {circle.__str__()}")
list_of_circles.sort()
for i,circle in enumerate(list_of_circles):
    print(f"{i}. {circle.__str__()}")