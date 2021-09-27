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
    """
    Purpose: Draws an image based on a given size and starting point.
    Parameters: The starting point (center) of the drawing, the integer size of
    the drawing and the graphics window object.
    Return Value: None.
    """
    # square
    p1 = pt.clone()
    p1.move(-size, size)
    p2 = pt.clone()
    p2.move(size, -size)

    square = Rectangle(p1,p2)
    square.setOutline("dark red")
    square.setFill("blue")
    square.setWidth(5)
    square.draw(win)

    # triangle left
    p3 = pt.clone()
    p3.move(-size, size)
    p4 = pt.clone()
    p4.move(-size/2, -size/2)
    p5 = pt.clone()
    p5.move(size/2, size/2)

    triL = Polygon([p3, p4, p5])
    triL.setWidth(0)
    triL.setFill("dark red")
    triL.draw(win)

    # triangle right
    p6 = pt.clone()
    p6.move(size, -size)

    triR = Polygon([p6, p4, p5])
    triR.setWidth(0)
    triR.setFill("dark red")
    triR.draw(win)

    # circle outer
    circleO = Circle(pt, size/2)
    circleO.setOutline("magenta")
    circleO.draw(win)

    # circle inner
    circleI = Circle(pt, size/4)
    circleI.setOutline("magenta")
    circleI.draw(win)


def recursiveDraw(pt, size, degree, win):
    """
    Purpose: Recursively calls an image drawing function a given number of times.
    Parameters: The starting point (center) of the drawing, the integer size of
    the drawing, an integer degree (level of recursion), and the graphics window object.
    Return Value: None.
    """
    if degree > 0:

        offset = size * 1.5 # squares touch corner to corner

        # alternate sides to prevent layering/clipping and increase coolness
        if degree % 2 == 0:
            newPt = Point(pt.getX() + offset, pt.getY() + offset)
            drawShape(pt, size, win)
            recursiveDraw(newPt, size/2, degree-1, win)

            newPt = Point(pt.getX() - offset, pt.getY() - offset)
            drawShape(pt, size, win)
            recursiveDraw(newPt, size/2, degree-1, win)

        else:
            newPt = Point(pt.getX() + offset, pt.getY() - offset)
            drawShape(pt, size, win)
            recursiveDraw(newPt, size/2, degree-1, win)

            newPt = Point(pt.getX() - offset, pt.getY() + offset)
            drawShape(pt, size, win)
            recursiveDraw(newPt, size/2, degree-1, win)


def main():
    win = GraphWin("Recursive Draw", 600, 600)

    width = win.getWidth()
    height = win.getHeight()
    size = 100
    mid = Point(width/2, height/2)

    degree = getInteger() # int(sys.argv[1])

    recursiveDraw(mid, size, degree, win)

    win.getMouse() # prevent win closing after drawing



main()
