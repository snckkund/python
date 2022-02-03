import math
number = int(input("enter a value please? "))
sqrt = math.sqrt(number)
print(sqrt)


def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a,end=' ')
    else:
        print(a,end=' ')
        print(b,end=' ')
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c,end=' ')
fib(int(sqrt))