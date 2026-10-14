from datetime import datetime


def main():
    # datetime.now()            --> get current date, when running the code.
    # datetime.now().strftime() --> string formatted time (shortcut name)
    
    # YYYY = 2023
    year = datetime.now().strftime("%Y")
    print(f"Year (%Y):\t{year}")
    
    # YY = 23
    year = datetime.now().strftime("%y")
    print(f"Year (%y):\t{year}")
    
    numeric_month = datetime.now().strftime("%m")
    print(f"Month (%m):\t{numeric_month}")
    
    short_month = datetime.now().strftime("%b")
    print(f"Month (%b):\t{short_month}")
    
    full_month = datetime.now().strftime("%B")
    print(f"Month (%B):\t{full_month}")
    
    day = datetime.now().strftime("%d")
    print(f"Day (%d):\t{day}")
    
    numeric_week = datetime.now().strftime("%w")
    print(f"Week (%w):\t{numeric_week}")
    
    day_of_the_week1 = datetime.now().strftime("%a")
    print(f"Week (%a):\t{day_of_the_week1}")
    
    day_of_the_week2 = datetime.now().strftime("%A")
    print(f"Week (%A):\t{day_of_the_week2}")
    
    hours_24 = datetime.now().strftime("%H")
    print(f"Hour (%H):\t{hours_24}")
    
    hours_12 = datetime.now().strftime("%I")
    print(f"Hour (%I):\t{hours_12}")
    
    minutes = datetime.now().strftime("%M")
    print(f"Minutes (%M):\t{minutes}")
    
    seconds = datetime.now().strftime("%S")
    print(f"Seconds (%S):\t{seconds}")
    
    ampm = datetime.now().strftime("%p")
    print(f"AP/PM (%p):\t{ampm}")


if __name__ == "__main__":
    main()