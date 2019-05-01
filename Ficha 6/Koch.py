from turtle import *

pen = Turtle()
pen.speed(0)

def drawSide(i, size):
    if i == 0:
        pen.forward(size)
        return 
    size /= 3 
    drawSide(i-1, size)
    pen.left(60)
    drawSide(i-1, size)
    pen.right(120)
    drawSide(i-1, size)
    pen.left(60)
    drawSide(i-1, size)

def drawKoch(i, side_size):
    for _ in range(3):
        drawSide(i, side_size)
        pen.right(120)

drawKoch(4, 400)

wait = input('type: ')