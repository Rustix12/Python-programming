print("If any of these value is unkwon just put 0 in it!")

r = float(input("Enter the radius of the circle: "))
d = float(input("Enter the diameter of the circle: "))
c = float(input("Enter the circumference of the circle: "))
if r > 0:
    print("Area of the circle is: ",3.1416*r*r)
elif d > 0:
    print("Area of the circle is:  ",d/2*d/2*3.1416)
elif c > 0:
    print("Area of the circle is: ",c/2/3.1416*c/2/3.1416*3.1416)
else:
    print("Sorry we could not find the area with the given infromation:( ")
