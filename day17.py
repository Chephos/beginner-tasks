#pascals triangle
from math import factorial
def pascals_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print('s', end=' ')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')
        print()


num = int(input("Enter the number of rows: "))
pascals_triangle(num)
