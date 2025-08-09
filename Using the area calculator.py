#Using the area calculator
import math
print("===================")
print('Area Calculator 📐')
print('===================')
print()
print('1. Triangle')
print('2. Rectangle')
print('3. Square')
print('4. Circle')
print('5. Quit')
print()
a=int(input("Which Shape: "))
if a==1:
    b=float(input('Base= '))
    h=float(input('Height= '))
    Area1=(h*b)/2
    print('Area of the triangle is ',Area1)
elif a==2:
    l=float(input('Length= '))
    w=float(input('Width= '))
    Area2=l*w
    print('Area of the rectangle is',Area2)
elif a==3:
    s=float(input('Sides= '))
    Area3=s**2
    print('Area of the square is',Area3)
elif a==4:
    r=float(input('Radius= '))
    Area4=round(math.pi*r**2,3)
    print('Area of the circle is',Area4)
else:
    print('Quit')
