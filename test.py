"""This Module contains basic functions that I use in various programs"""

# Variable Definitions

__version__ = "Beta"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "17/09/2018"

# functions


def cls():
    """This function clears the shell screen"""
    print("\n" * 50)


def pause():
    """This function pauses the program until the user presses enter key"""
    x = input("PRESS ENTER TO CONTINUE...")


def confirm():
    """This Function asks user for confirmation"""
    confirmation = input("Do you wish to confirm? Y-N")
    confirmation = confirmation.lower()
    if confirmation == "y":
        return True
    else:
        print("Confirmation Failed!")
        return False


def UEIP(x, y):
    """This Function Confirms whether input type is correct"""
    if y == 0:
        while y is not 2:
            try:
                UserInput = int(input(x))
                y = 2
            except:
                print('Not a Valid Entry.')
    elif y == 1:
        while y is not 2:
            try:
                UserInput = str(input(x))
                y = 2
            except:
                print('Not a Valid Entry.')
    return UserInput


def DP():
    day = UEIP("What day number is it today? ", 0)
    month = UEIP("What month number is it today? ", 0)
    year = UEIP("What year is it today? ", 0)
    date = [day, month, year]
    return date


def PD(date):
    """Converts list date format into a string representation"""
    datestr = "{}/{}/{}".format(date[0], date[1], date[2])
    return datestr


def DC(date, date2):
    day = date[0]
    day2 = date2[0]
    month = date[1]
    month2 = date2[1]
    year = date[2]
    year2 = date2[2]
    if year == year2:
        pass
    elif year > year2:
        i = 1
        return i
    else:
        i = 0
        return i
    if month == month2:
        pass
    elif month > month2:
        i = 1
        return i
    else:
        i = 0
        return i
    if day == day2:
        i = 2
        return i
    elif day > day2:
        i = 1
        return i
    else:
        i = 0
        return i


def DC2(dates):
    dates2 = []
    for date in dates:
        if len(dates2) == 0:
            dates2.append(date)
        else:
            x = 0
            for date2 in dates2:
                i = DC(date, date2)
                if i == 1:
                    dates2.insert(x,date)
                    break
                else:
                    x += 1
    return dates2

# Main Code


i = 0
xdates = []
while i is not 5:
    x = DP()
    xdates.append(x)
    i += 1

ydates = DC2(xdates)

print(ydates)

