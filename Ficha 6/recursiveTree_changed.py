import turtle
import random
#Modify the thickness of the branches so that as 
# the branchLen gets smaller, the line gets thinner.        --DONE

#Modify the color of the branches so that as the branchLen  --DONE
# gets very short it is colored like a leaf.

#Modify the angle used in turning the turtle so that at each 
# branch point the angle is selected at random in some range.  --DONE
# For example choose the angle between 15 and 45 degrees. 
# Play around to see what looks good.

#Modify the branchLen recursively so that instead of always    --DONE - for some reason crashes
# subtracting the same amount you subtract a random amount in some range.

def tree(branchLen,t,pensize, red):
        if branchLen > 11:
                x = random.randint(15,45)
                sub = random.randint(5,20) 
                t.pensize(pensize)
                t.color(red,150,0)
                t.forward(branchLen)
                t.right(x) #default 20
                tree(branchLen-sub,t, pensize-1, red-10) #default 15
                t.left(2*x) #default 40
                tree(branchLen-(0.5*sub),t, pensize-1, red-10) #default 15
                t.right(x) #default 20
                t.backward(branchLen)
                
                

def main():
        t = turtle.Turtle()
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        turtle.colormode(255)
    
    
        tree(75,t,10,150)
        myWin.exitonclick()

main()
