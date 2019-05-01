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
                #sub = random.randint(2,10) - crash
                t.pensize(pensize)
                t.color(red,150,0)
                t.forward(branchLen)
                t.right(20) #default 20
                print(branchLen)
                tree(branchLen-15,t, pensize-2, red-20) #default 15
                sub = random.randint(2,10)
                t.left(40) #default 40
                tree(branchLen-15,t, pensize-2, red-20) #default 15
                sub = random.randint(2,10)
                t.right(20) #default 20
                t.backward(branchLen)
                
                

def main():
        t = turtle.Turtle()
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        turtle.colormode(255)
    
    
        tree(100,t,10,150)
        myWin.exitonclick()

main()
