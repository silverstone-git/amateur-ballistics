"""_________________________________________________________ Amateur Ballistics _________________________________________________
_______________________________________________________Game Developer - Aryan Sidhwani____________________________________________
last updated >>>---17/02/2020---<<"""
import random
from math import sin,cos,radians,degrees,sqrt,atan,pi
import turtle
initpos1,initpos2,a,b,turns = 0,0,0,0,0
wavevals = [360,720,1080,2880]
speedvals = [2,5,8]
startornot = "Yes"
space = turtle.Screen()
gbox = None
print("*"*150)
print("Relax and read the instructions while the game loads")
print()
print("%*"*75)
print("This game is a multiplayer game in which 2 players can take on")
print("2 tanks and enter the distance to move the tank ahead, launch ")
print("angle of the missile in degrees and power of the missile from ")
print("0 to 3; 0 power gives definite speed and giving power increases")
print("the uncertainties in speed. Damage points are most if missile hits")
print("near the target and none if explodes outside a certain radius.")
print("Once the first damage is done, the player who inflicts more ")
print("damage points wins. The game damage points can be saved.")
print("%*"*75)
print()
print("Quit the game any time by pressing ctrl + c in this window")
print()
print()
while gbox != "1" and gbox !="earth" and gbox != "Earth" and gbox != "2" and gbox!= "moon" and gbox != "Moon" and gbox != "3" and gbox != "Jupiter" and gbox != "jupiter" and gbox != "4" and gbox != "Shinigami Realm" and gbox != "shinigami" and gbox != "shinigami realm":
        gbox = space.textinput("Where do you want to play?: ","1:Earth\n2.Moon\n3.Jupiter\n4.Shinigami realm")
        if gbox == "1" or gbox == "earth" or gbox == "Earth":
            g = 9.8
            lcol = "brown"
        elif gbox == "2" or gbox == "moon" or gbox == "Moon":
            g = 1.6
            lcol = "gray"
        elif gbox == "3" or gbox == "Jupiter" or gbox == "jupiter":
            g = 30
            lcol = "yellow"
        elif gbox == "4" or gbox == "Shinigami Realm" or gbox == "shinigami" or gbox == "shinigami realm":
            g = 12
            lcol = "white"
infobox = None
while infobox != "1" and infobox != "2" and infobox != "3":
    infobox = space.textinput("Welcome to the game","Enter level 1,2, or 3 and press enter to start")
    if infobox == "1":
        waveval = wavevals[2]
        speedval = speedvals[1]
        maxmov = 25
    elif infobox == "2":
        waveval = wavevals[3]
        speedval = speedvals[2]
        maxmov = 100
    elif infobox == "3":
        waveval = wavevals[3]
        speedval = speedvals[1]
        maxmov = 125
try:
        import savefile
        repornot = space.textinput("Continue with last game?","1. Yes or \n2. No")
        if repornot == "Yes" or repornot == "1" or repornot == "yes" or repornot == "y":
                dmg1 = savefile.dmg1
                dmg2 = savefile.dmg2
        else:
                dmg1 = 0
                dmg2 = 0
except:
        print("Error: savefile.py not found")
        dmg1 = 0
        dmg2 = 0
hl = turtle.Turtle()#the hill maker turt
p1 = turtle.Turtle()#Player 1 turt
p2 = turtle.Turtle()#Player 2 turt
m1 = turtle.Turtle()#Player 1 Missile
m2 = turtle.Turtle()#Player 2 Missile
bd = turtle.Turtle()#Border maker turt
wt = turtle.Turtle()#writer turt
space.title("Amateur Ballistics")
bd.pu()
bd.speed(600)
bd.pen(pencolor = "white", pensize = 10)
m1.shape("arrow")
m1.pen(pencolor = "white")
m2.shape("arrow")
m2.pen(pencolor = "white")
p1.shape("square")
p2.shape("square")
space.bgcolor("black")
wt.pen(pencolor = "white")
hl.ht()
p1.ht()
p2.ht()
m1.ht()
m2.ht()
bd.ht()
wt.ht()
p1.resizemode("auto")
p2.resizemode("auto")
p1.pu()
p2.pu()
p1.pen(pensize = 5,pencolor = "red")
p2.pen(pensize = 5,pencolor = "blue")
hl.pen(pencolor = lcol, pensize = 5)
hl.pu()
hl.setpos(-750,-250) #the start point of hill
hl.pd()
gnd = []
for x in range(0,waveval):                                 
	x = radians(x)
	hl.setpos((degrees(x)/2)-750,30*sin(x)-250)         
	gnd.append(hl.position())
"""
the hill points are plot one by one and are appended one by one to an empty list gnd
"""
bd.setpos(gnd[-1][0],-350)
#The border is made by enclosing hill in 4 sides by bd turt
bd.pd()
bd.lt(90)
bd.fd(720)
bd.lt(90)
bd.fd(gnd[-1][0]-gnd[0][0])
bd.lt(90)
bd.fd(720)
bd.lt(90)
bd.fd(gnd[-1][0]-gnd[0][0])
"""
Tank 1 and the missile position is set
"""
m1.pu()
p1.setpos(gnd[a])
m1.setpos(gnd[a])
p1.st()
m1.st()
m1.pd()
m2.pu()
"""
Tank 2 and the missile position is set
"""
p2.setpos(gnd[-1])
m2.setpos(gnd[-1])
p2.st()
m2.st()
m2.pd()
m2.setheading(pi)
while startornot == "Yes" or startornot == "yes" or  startornot == "1":
    initpos1,initpos2,a,b,turns = 0,0,0,0,0
    while turns < 5:
        #print("Player 1's Turn")
        x = None
        while x == None:
        	x = space.numinput("Player 1","Enter the distance which you want your tank to tread ahead, max = {0}".format(maxmov),0,minval = -maxmov,maxval = maxmov)
        #------------------------------------------------------Fd1--------------------------------------------------------------
        x = 10*x #assumptions used
        targ1 = int(x)
        a = 0
        m1.pen(pencolor = "black")
        """while a < targ1:
                p1xinit = p1.pos()[0]
                p1yinit = p1.pos()[1]
                p1.setpos(gnd[initpos1 + a])
                m1.setpos(gnd[initpos1 + a])
                p1xfinal = p1.pos()[0]
                p1yfinal = p1.pos()[1]
                p1tan = atan((p1yfinal-p1yinit)/(0.2 + p1xfinal-p1xinit))
                p1.setheading(p1tan)
                a += 1"""
        m1.setpos(gnd[initpos1 + targ1])
        p1.setpos(gnd[initpos1 + targ1])
        m1.pen(pencolor = "red")
        initpos1 = gnd.index(p1.pos())
        #------------------------------------------------------Mov1------------------------------------------------------------
        p = None
        while p == None:
        	p = space.numinput("Player 1","Enter the launch angle in degrees",45,minval = -100,maxval = 100)
        p = radians(p)
        u1a = None
        while u1a == None:
        	u1a = space.numinput("Player 1","Enter the booster power of missile within range 0 to 3",0,minval = 0,maxval = 3)
        if u1a == 0:
                u1 = speedval
        elif random.random() > 0.5:
            u1 = speedval + (u1a*4) #The power of missile increases the uncertainty in speed
        else:
            u1 = speedval - (u1a*4)
        #print("speed of m1 = ",10*u1)
        m1init = m1.pos()
        t1 = (2*u1*sin(p))/g
        t1 = 10*t1
        t1 = int(t1) 
        u1 = 10*u1
        u1x = u1 * cos(p)
        u1y = u1 * sin(p)
        t1a = 1
        while t1a < t1:
                m1x = m1init[0] + u1x*t1a
                m1y = m1init[1] + (u1y*t1a-((g*t1a*t1a)/2))
                m1tangent = atan((u1y*t1a-((g*t1a*t1a)/2))/(u1x*t1a))
                m1.setheading(m1tangent)
                d21a = sqrt(((m1.pos()[0]-p2.pos()[0])**2)+(((m1.pos()[1]-p2.pos()[1])**2)))
                m1.goto(m1x,m1y)
                """
                m1 goes in a parabola point by point
                """
                d21b = sqrt(((m1.pos()[0]-p2.pos()[0])**2)+(((m1.pos()[1]-p2.pos()[1])**2)))
                """
                If missile is coming towards target, it continues
                """
                if d21a > d21b:
                        t1 += 1
                else:
                        break
                for gdp1 in gnd:
                        if int(gdp1[0]) == int(m1x):
                                if gdp1[1] - m1y > 0:
                                        t1a += 1000
                t1a += 1
        m1.pd()
        m1.pen(pencolor = "red")
        m1.dot(40)
        m1.pu()
        """
        the if - elif ladder checks the distance from target when missile explodes
        Near Explosion results in more damage
        """
        if sqrt((p2.pos()[0]-m1.pos()[0])**2 + (p2.pos()[1]-m1.pos()[1])**2) < 20: 
                dmg2 += 15
        elif sqrt((p2.pos()[0]-m1.pos()[0])**2 + (p2.pos()[1]-m1.pos()[1])**2) < 40:
                dmg2 += 7
        elif sqrt((p2.pos()[0]-m1.pos()[0])**2 + (p2.pos()[1]-m1.pos()[1])**2) < 60:
                dmg2 += 4
        elif sqrt((p2.pos()[0]-m1.pos()[0])**2 + (p2.pos()[1]-m1.pos()[1])**2) <= 120:
                dmg2 += 2
        else:
        	pass
        m1.clear()
        #print("damage on p2 is: ",dmg2)
        wt.ht()
        wt.pu()
        wt.goto(p2.pos()[0] - 50,p2.pos()[1]+50)
        wt.pd()
        wt.fillcolor("red")
        wt.color("red")
        wt.write(dmg2,align="left",font=("Arial",16,"bold"))
        wt.pu()
        m1.ht()
        m1.pu()
        m1.setpos(p1.pos())
        m1.st()
        m1.pd()
        space.ontimer(wt.clear(),2500)
        #print("Player 2's Turn")
        #---------------------------------------------------------------Fd2-------------------------------------------------------
        y = None
        while y == None:
        	y = space.numinput("Player 2","Enter the distance which you want your tank to tread ahead max = {0}".format(maxmov),0,minval = -maxmov,maxval = maxmov)
        y = -10*y
        targ2 = int(y)
        b = -1
        m2.pen(pencolor = "black")
        """while b > targ2:
                p2xinit = p2.pos()[0]
                p2yinit = p2.pos()[1]
                p2.setpos(gnd[initpos2 + b])
                m2.setpos(gnd[initpos2 + b])
                p2xfinal = p2.pos()[0]
                p2yfinal = p2.pos()[1]
                #p2tan = atan((p2yfinal-p2yinit)/(0.2 + p2xfinal-p2xinit))
                #p2.setheading(p2tan)
                b -= 1"""
        m2.setpos(gnd[initpos2 + targ2])
        p2.setpos(gnd[initpos2 + targ2])
        m2.pen(pencolor = "yellow")
        initpos2 = gnd.index(p2.pos())
        #---------------------------------------------------------------Mov2-------------------------------------------------------
        q = None
        while q == None:
        	q = space.numinput("Player 2","Enter the launch angle in degrees",45,minval = -100,maxval = 100)
        q = radians(q)
        u2a = None
        while u2a == None:
        	u2a = space.numinput("Player 2","Enter the booster power of missile within range 0 to 3",0,minval = 0,maxval = 3)
        if u2a == 0 :
                u2 = speedval
        elif random.random() > 0.5:
            u2 = speedval + (u2a*4)
        else:
            u2 = speedval - (u2a*4)
        #print("speed of m2 is =",10*u2)
        m2init = m2.pos()
        m2.setheading(180)
        t2 = (2*u2*sin(q))/g
        t2 = 10*t2
        t2 = int(t2)
        u2 = 10*u2
        u2x = u2 * cos(q)
        u2y = u2 * sin(q)
        t2a = 1
        while t2a < t2:
                m2x = m2init[0] - u2x*t2a
                m2y = m2init[1] + (u2y*t2a-((g*t2a*t2a)/2))
                m2tangent = atan((u2y*t2a-((g*t2a*t2a)/2))/(u2x*t2a))
                m2.setheading(m2tangent)
                d12a = sqrt(((m2.pos()[0]-p1.pos()[0])**2)+(((m2.pos()[1]-p1.pos()[1])**2)))
                m2.goto(m2x,m2y)
                d12b = sqrt(((m2.pos()[0]-p1.pos()[0])**2)+(((m2.pos()[1]-p1.pos()[1])**2)))
                if d12a > d12b:
                        t2 += 1
                else:
                        break
                for gdp2 in gnd:
                        if int(gdp2[0]) == int(m2x):
                                if gdp2[1] - m2y > 0:
                                        t2a += 1000               
                t2a += 1
        m2.pd()
        m2.pen(pencolor = "yellow")
        m2.dot(40)
        m2.pu()
        if sqrt((p1.pos()[0]-m2.pos()[0])**2 + (p1.pos()[1]-m2.pos()[1])**2) < 20:
                dmg1 += 15
        elif sqrt((p1.pos()[0]-m2.pos()[0])**2 + (p1.pos()[1]-m2.pos()[1])**2) < 40:
                dmg1 += 7
        elif sqrt((p1.pos()[0]-m2.pos()[0])**2 + (p1.pos()[1]-m2.pos()[1])**2) < 60:
                dmg1 += 4
        elif sqrt((p1.pos()[0]-m2.pos()[0])**2 + (p1.pos()[1]-m2.pos()[1])**2) <= 120:
                dmg1 += 2
        else:
        	pass
        m2.clear()
        #print("damage on p1 is : ",dmg1)
        wt.ht()
        wt.pu()
        wt.goto(p1.pos()[0] + 50 , p1.pos()[1] + 50)
        wt.pd()
        wt.fillcolor("red")
        wt.color("red")
        wt.write(dmg1,align="left",font=("Arial",16,"bold"))
        wt.pu()
        m1.ht()
        m2.ht()
        m2.pu()
        m2.setpos(p2.pos())
        m2.pd()
        space.ontimer(wt.clear(),2500)
        turns += 1
        if dmg1 == 0 and dmg2 == 0:
                turns -= 1
    try:
            with open("savefile.py","a") as pdt:
                pdt.write("\ndmg1 = {0}".format(dmg1))
            with open("savefile.py","a") as pdt:
                pdt.write("\ndmg2 = {0}".format(dmg2))
    except:
            print(">>--savefile.py file does not exist in the folder")
            print("Progress is not being saved--<<")
    startornot = space.textinput("Thank You for playing","Do You Want to play again or not - \"Yes\" or \"No\" or 1")
hl.clear()
bd.clear()
if dmg1 > dmg2 :
    print("Player 2 Wins")
    p1.ht()
    m1.ht()
    wt.pu()
    wt.goto(-50,0)
    wt.pd()
    wt.write("Player 2 Wins!!",align = "left",font = ("Arial",32,"bold","italic"))
    p2.pu()
    for circ in range(5):
            p2.circle(5)
elif dmg1 < dmg2 :
        print("Player 1 Wins")
        p2.ht()
        m2.ht()
        wt.pu()
        wt.goto(-50,0)
        wt.pd()
        wt.write("Player 1 Wins!!",align = "left",font = ("Arial",32,"bold","italic"))
        p1.pu()
        for circ in range(5):
                p1.circle(5)
else:
    #print("Draw")
    p1.ht()
    p2.ht()
    wt.pu()
    wt.goto(-50,0)
    wt.pd()
    wt.write("Bravo 6 going dark",align = "left",font = ("Arial",32,"bold","italic"))
    for circ in range(5):
            p1.circle(5)
space.ontimer(space.bye(),4500)
