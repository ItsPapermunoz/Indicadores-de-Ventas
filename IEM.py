"""This Module contains basic functions that I use in various programs"""

# Variable Definitions

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "9th of August 2017"

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


# Main Code

print("Succesfully loaded Itspaper's essentials Module!")
print("Thank you for Using!")
pause()