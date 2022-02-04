# Three sides of the triangle is a, b and c
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# the semi perimeter  
s = (a + b + c) / 2  
  
# area of the triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is ',area)