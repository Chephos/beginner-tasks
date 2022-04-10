def no_of_days(height):
    "Returns the number of days it takes a man to climb out of a well."
    up = 8
    down = 3
    total = 0
    days = 0
    while True:
        days += 1
        total += up
        if total >= height:
            break
        else:
            total -= down
    return print(f"It takes {days} days to climb out of the well.")

no_of_days(17)