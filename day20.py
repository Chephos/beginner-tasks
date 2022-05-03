import time
import beepy


def get_time_value(value:str): 
    """
    Returns the time value and its unit
    """
    return int(value[:-1]), value[-1]

def get_time_in_seconds(value:str, unit:str):
    """
    Returns the time value in seconds
    """
    if unit == 's':
        return value
         
    elif unit == 'm':
        return value *60

    elif unit == 'h':
        return value * 3600

def countdown(time_in_seconds):

    for i in range(time_in_seconds, -1,-1):
        if i != 0:
            print(i,"seconds")
            time.sleep(1)
        else:
            while True:
                print("Time Up!")
                beepy.beep()

def main():
    time_value = (input('h, m & s represent the unit of hours, minutes & seconds respectively\nEnter time: '))
    value, unit = get_time_value(time_value)
    time_in_secs = get_time_in_seconds(value, unit)
    countdown(time_in_secs)

if __name__ == '__main__':
    main()


# def countdown(t):
#     while t>0:
#         mins,secs = divmod(t,60)
#         timer = '{:02d}:{:02d}'.format(mins,secs)
#         print(timer,end='\r')
#         time.sleep(1)
#         t -=1

#     print('Fire in the hole!!')

# countdown(int(cntdwn))