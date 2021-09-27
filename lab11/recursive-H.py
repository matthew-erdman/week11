from graphics import *
import sys


def drawH(pt, size, win):

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

def recurseH(pt, degree, win):
    size = 200
    newPt = Point(pt.getX() + size, pt.getY() + size)
    if degree > 0:
        drawH(pt, size, win)
        recurseH(newPt, degree-1, win)

def main():
    win = GraphWin("Letter H", 600, 600)
    width = win.getWidth()
    height = win.getHeight()
    pt = Point(width/2, height/2)
    degree = int(sys.argv[1])

    recurseH(pt, degree, win)
    win.getMouse()

main()
