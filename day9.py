def isPrime(num):
    """
    Checks if a number is a prime number or not.
    """
    # prime numbers are greater than 1 hence the check
    if num > 1:
        #check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return print(f"{num} is not a prime number.")
                
        else:
            return print(f"{num} is a prime number.")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return print(f"{num} is not a prime number.")

# try:
#     num.isalpha()
# except ValueError:
#     print("Enter an integer")
num = int(input("Enter a number: "))
isPrime(num)