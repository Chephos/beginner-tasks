def greatest_common_divisor(num1,num2):
    """Returns the greatest common factor of inputs"""
    if num2 != 0:
        remainder = num1 % num2
        greatest_common_divisor(num2,remainder)
    else:
        return print(f"The greatest common factor is {num1}")

greatest_common_divisor(816,226)