import math


def cal_ellipse(x, y):
    return math.pi*x*y
   


print("A program to calculate area of ellipse in form of square meter")
x = float(input("Radius of center and vertex (m) : "))
y = float(input("Radius of center and co-vertex (m) : "))

area = cal_ellipse(x,y)
print(f"Area of ellipse is = {area : .2f} m^2")