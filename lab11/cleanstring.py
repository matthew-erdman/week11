"""
    Description: This program removes instances of a charcter from a string. A user
    provides a string and a charcter, and the program recursively removes all occurrences
    of the character from the string.
    Author: Matthew Erdman
    Date: 9/20/21
"""

def getChar():
    """
    Purpose: Gets input from the user and validates that it is a single character.
    Parameters: None.
    Return Value: The user's chosen character.
    """
    userChar = input("Char: ")
    while True:
        if len(userChar) == 1:
            return userChar
        print("Please enter a single character.")
        userChar = input("Char: ")


def cleanString(rawStr, cleanChar):
    """
    Purpose: Recursively removes all instances of a character from a string.
    Parameters: The string which will have its characters searched/removed and
    the charcter which will be removed from the string.
    Return Value: The final string with selected characters removed.
    """
    # reached first (final) charcter, return back up
    if len(rawStr) == 1:
        return rawStr[-1] if rawStr[-1] != cleanChar else ""
    else:
        cleanedString = cleanString(rawStr[:-1], cleanChar)
        # build up string as each recursive call returns
        if rawStr[-1] != cleanChar: # remove instances of character
            cleanedString += rawStr[-1]
        return cleanedString


def main():
    rawStr = input("String: ")
    cleanChar = getChar()
    cleanedString = cleanString(rawStr, cleanChar)
    print(cleanedString)

main()
