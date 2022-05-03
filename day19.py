import datetime 
def day(date_string:str) -> str:
    """Returns the day of the week of the input date."""    
    dt_object = datetime.datetime.strptime(date_string, '%d-%m-%Y')
    return dt_object.strftime('%A')

try:
        date_string = input("Enter a date (dd-mm-yyyy) to check for the day: ")
        print(day(date_string))
except ValueError:
        print("Use dd-mm-yyyy format")

