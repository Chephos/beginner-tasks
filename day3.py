def palindromic_numbers(numbers):
    """Print out all palindromic numbers less than the given input.

        Return the sum of the palindromes
    """
    #Check if the input is a string
    if str(numbers).isalpha():
        return print("The function only accepts integers!")
    else:
        print(f"Palindromes from 0 to {numbers} are:")
        palindromes = []
        count = 0

        #Loop through the input after converting it to a string
        #Check if it is equal to its reversed self
        #Count it and store in palindromes list
        
        for num in range(numbers):
            if str(num) == str(num)[::-1]:
                palindromes.append(num)
                count += 1
                
        return print(palindromes),print(f"\nThe total number of Palindrome is: {count}")
        

palindromic_numbers(500)
