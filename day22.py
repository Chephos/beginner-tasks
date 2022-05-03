import datetime 
def day(date_string:str) -> str:

    """Returns the day of the week of the input date."""    
    dt_object = datetime.datetime.strptime(date_string, '%d-%m-%Y')
    print(dt_object.strftime('%d %b'))
    {'aries': ['mar  03-21 - april 04-19' ],
        'taurus':'apr 04-20-may 05-20',
        'gemini':'may 05-21-jun 06-20',
        'cancer':'jun 06-21-july 07-22',
        'leo':'jul 07-23-aug 08-22',
        'virgo':'aug 08-23-sep 09-22',
        'libra':'sep 09-23-oct 10-22',
        'scorpio':'oct 10-23-nov 11-21',
        'sagittarius':'nov 11-22-dec 12-21',
        'capricon':'dec 12-22-jan 01-19',
        'aquarius':'jan 01-20-feb 02-18',
        'pisces':'feb 02-19-mar 03-20'
        }
    return dt_object.strftime('%A')

try:
        date_string = input("Enter a date (dd-mm-yyyy) to check for the day: ")
        print(day(date_string))
except ValueError:
        print("Use dd-mm-yyyy format")