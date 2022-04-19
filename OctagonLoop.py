import turtle

p = turtle.Pen()

def RecLeft(i):
    for i in range(8):
        p.forward(100)
        p.left(45)

def RecRight(i):
    for i in range(8):
        p.forward(100)
        p.right(45)
    
def Go(x,y):
    p.penup()
    p.goto(x,y)
    p.pendown()

p.clear()

for i in range(4):
        Go(10*i,10*i)
        RecLeft(i)
        Go (-10*i,-10*i)
        RecRight(i)

        
