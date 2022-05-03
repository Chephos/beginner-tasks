
def to_roman_numeral(arab_num):
    """Returns the roman numeral of a given integer"""
    roman_numerals = {1_000_000:'M\u0304',500_000:'D\u0304',100_000:'C\u0304',50_000:'L\u0304',10_000:'X\u0304',5000:'V\u0304',1000:'M',900:'CM' ,500:'D',400:'CD' , 100:'C', 90:'XC' , 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I', }

    roman = ''
    
    for arab,rome in roman_numerals.items():
        x,y=divmod(arab_num,arab)
        roman += rome*x
        arab_num = y
    return roman

print(to_roman_numeral(156))