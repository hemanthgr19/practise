x=float(input("area of 1 side of triangle: "))
y=float(input("area of 2 side of triangle: "))
z=float(input("area of 3 side of triangle: "))

s = float(x+y+z)/2
print(s)

area= (s * (s-x) * s * (s-y) * s * (s-z)) ** 0.5
print(area)