import math

a = int(input("Please enter the co-efficient of x^2: "))
b = int(input("Please enter the co-efficient of x: "))
c = int(input("Please enter the constant: "))

D = math.sqrt((b**2)-(4*a*c))

z1 = ((-b)+(D))/(2*a)
z2 = ((-b)-(D))/(2*a)

if D == 0:
    print("It has two real identical roots: ",z1,"and",z2)
elif D > 0:
    print("It has two real distinct roots: ",z1,"and",z2)
else:
    print("It has no real roots: ",z1,"and",z2)


