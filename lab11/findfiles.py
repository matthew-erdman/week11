"""
    Description: This program allows the user to search for filenames containing a
    given pattern in a given directory. A user provides a directory and a pattern, and
    the program recursively finds all occurrences of the pattern in filenames from the directory.
    Author: Matthew Erdman
    Date: 9/20/21
"""
from os import listdir
from os.path import isdir, expanduser

def getDir():
    """
    Purpose: Gets a path from the user and validates that it is a real directory.
    Parameters: None.
    Return Value: The user's chosen path.
    """
    userDir = input("Path: ")
    while True:
        # add forward slash to end of path if not already present
        if userDir[-1] != "/":
            userDir += "/"
        # check that the path supplied is a valid directory
        if isdir(userDir):
            return userDir
        print("Please enter a valid path.")
        userDir = input("Path: ")


def searchFile(text, pattern):
    """
    Purpose: Recursively search a text string for an instance of a pattern.
    Parameters: text, the string which will be searched and pattern, the pattern
    which will be searched for in the string.
    Return Value: Boolean value indicating if the pattern was found.
    """
    # reached end of string, pattern not present
    if len(text) < len(pattern):
        return False
    # check first chunk of text for pattern
    elif text[:len(pattern)] == pattern:
        return True
    # recursive call to check next chunk of text
    else:
        return searchFile(text[1:], pattern)


def searchDir(userDir, pattern):
    """
    Purpose: Recursively search directories for instances of a pattern in filenames.
    Parameters: userDir, the path to the directory where the search will begin and
    patter, the pattern which will be searched for in the directory.
    Return Value: None.
    """
    contents = listdir(userDir)
    # loop through each item in user's directory
    for item in contents:
        # prepend path to active item
        current = userDir + item
        # recursive call to search nested directories
        if isdir(current):
            searchDir(current + "/", pattern)
        # found file, check filename for pattern
        else:
            if searchFile(item, pattern):
                print(current)


def main():
    userDir = getDir()
    pattern = input("Pattern: ")
    searchDir(userDir, pattern)


main()
