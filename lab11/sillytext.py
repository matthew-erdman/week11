"""
    Description: This program creates a silly text effect. A user provides a string
    and an integer, and each letter of the original text is printed repeated n times.
    Author: Matthew Erdman
    Date: 9/20/21
"""

def getInteger():
    """
    Purpose: Gets input from the user and validates that it is a non-negative integer.
    Parameters: None.
    Return Value: The user's chosen integer.
    """
    userInt = input("Num: ")
    while True:
        try:
            userInt = int(userInt)
            if userInt >= 0:
                return userInt
        except ValueError:
            pass
        print("Please enter a non-negative integer.")
        userInt = input("Num: ")


def sillyText(repeatStr, repeatNum):
    """
    Purpose: Recursively repeats each character in a string a certain number of times.
    Parameters: The string which will have its characters repeated and the
    non-negative integer which will determine how many times the characters are repeated.
    Return Value: The final string with repeated characters.
    """
    # reached first (final) character of string, return back up
    if len(repeatStr) == 1:
        return repeatStr[0] * repeatNum
    else:
        sillyString = sillyText(repeatStr[:-1], repeatNum)
        # build up string as each recursive call returns
        sillyString += repeatStr[-1] * repeatNum
        return sillyString


def main():
    repeatStr = input("String: ")
    repeatNum = getInteger()
    sillyString = sillyText(repeatStr, repeatNum)
    print(sillyString)

main()
