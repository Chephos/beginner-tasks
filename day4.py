def decimal_to_Hexadecimal(decimal):
    """Returns the hexadecimal of a decimal number"""
    conversion_table = {
        0:'0',1:'1',2:'2',
        3:'3',4:'4',5:'5',
        6:'6',7:'7',8:'8',
        9:'9',10:'A',11:'B',
        12:'C',13:'D',14:'E',15:'F'
    }

    hexadecimal = ''
    while (decimal) >0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal //=  16

    return hexadecimal

print(decimal_to_Hexadecimal(13104038110))

#or

print(hex(13104038110))
