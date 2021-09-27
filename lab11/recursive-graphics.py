"""
    Description:
    Author: Matthew Erdman
    Date: 9/23/21
"""
from graphics import *
import sys

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


def drawShape(pt, size, win):

    p1 = pt.clone()
    p1.move(-size, -size)
    p2 = pt.clone()
    p2.move(-size, size)

    left = Line(p1,p2)
    left.draw(win)

    p3 = pt.clone()
    p3.move(size, size)
    p4 = pt.clone()
    p4.move(size, -size)

    right = Line(p3,p4)
    right.draw(win)

    p5 = pt.clone()
    p5.move(size, 0)
    p6 = pt.clone()
    p6.move(-size, 0)

    mid = Line(p5,p6)
    mid.draw(win)


def recurseH(pt, size, degree, win):
    if degree > 0:
        newPt = Point(pt.getX() + size, pt.getY() + size)
        drawShape(pt, size, win)
        recurseH(newPt, size/2, degree-1, win)

        newPt = Point(pt.getX() + size, pt.getY() - size)
        drawShape(pt, size, win)
        recurseH(newPt, size/2, degree-1, win)

        newPt = Point(pt.getX() - size, pt.getY() + size)
        drawShape(pt, size, win)
        recurseH(newPt, size/2, degree-1, win)

        newPt = Point(pt.getX() - size, pt.getY() - size)
        drawShape(pt, size, win)
        recurseH(newPt, size/2, degree-1, win)


def main():
    win = GraphWin("Letter H", 600, 600)

    width = win.getWidth()
    height = win.getHeight()
    size = 100

    pt = Point(width/2, height/2)
    degree = int(sys.argv[1]) # getInteger()

    recurseH(pt, size, degree, win)

    win.getMouse()



main()
