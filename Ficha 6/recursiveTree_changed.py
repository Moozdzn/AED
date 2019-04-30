import turtle

#Modify the thickness of the branches so that as 
# the branchLen gets smaller, the line gets thinner.

#Modify the color of the branches so that as the branchLen 
# gets very short it is colored like a leaf.

#Modify the angle used in turning the turtle so that at each 
# branch point the angle is selected at random in some range. 
# For example choose the angle between 15 and 45 degrees. 
# Play around to see what looks good.

#Modify the branchLen recursively so that instead of always 
# subtracting the same amount you subtract a random amount in some range.

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()