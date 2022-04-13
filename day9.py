def isPrime(num):
    """
    Checks if a number is a prime number or not.
    """

    if num > 1:
        for i in range(2,num//2):
            if (num % i) == 0:
                return print(f"{num} is not a prime number.")
                
        else:
            return print(f"{num} is a prime number.")

    else:
        return print(f"{num} is not a prime number.")

num = int(input("Enter a number: "))
isPrime(num)