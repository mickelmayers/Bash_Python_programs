import math

print ("root's counter")
input("Enter a, b, c from Your equation y = ax2 + bx + c:")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

delta = b**2-4*a*c

if delta<0:
    print ("No roots :(  delta is <0 ")
elif delta == 0:
    x = (-b + math.sqrt(b**2-4*a*c))/2*a
    print ("Delta is 0. You have one root:%s" %x)
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print ("You have two root's. Delta is >0 x1= %s and x2= %s" %(x1,x2))
