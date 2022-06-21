#MyStory
#Author: Hok Chiu Shen
#Attack on Godzilla, May 24, 2022


import turtle
import random
import time

t = turtle.Turtle() #background
e = turtle.Turtle() #tree
l = turtle.Turtle() #lake
m = turtle.Turtle() #mountain
c = turtle.Turtle() #mouse clicks
mp = turtle.Turtle() #stickpose
win = turtle.Turtle() #windows
s1 = turtle.Turtle() #downsword
st = turtle.Turtle() #starting screen
g = turtle.Turtle() #godzilla
g1 = turtle.Turtle() #godzilla's mouth
s2 = turtle.Turtle() #upsword
h = turtle.Turtle() #help
q = turtle.Turtle() #text
ar = turtle.Turtle() #arrow
ss = turtle.Turtle() #small sword
f = turtle.Turtle() #fatality screen
moon = turtle.Turtle() #moon
rc = turtle.Turtle() #right cars
lc = turtle.Turtle() #left cars
r1 = turtle.Turtle() #rock1
r2 = turtle.Turtle() #rock2
r3 = turtle.Turtle() #rock3
wo1 = turtle.Turtle() #wood1
wo2 = turtle.Turtle() #wood2
wo3 = turtle.Turtle() #wood3
k = turtle.Turtle() #key
hp1 = turtle.Turtle() #user hp
hp2 = turtle.Turtle() #godzilla hp
screen = turtle.Screen()
screen.setup(640, 480, 0, 0)


#no possible restart option during midgame unless you choose the wrong option
#remove the uses of buttons to return or make scenes appear becuase they will be used to fight godzilla
#a restart logo or button and remove mouse clicks because we need it for fighting game
#a gear looking button to tell the user how to reset if needed by pressing a key
# fighting game, ask user to input a specfic letter (time limit 5 seconds) hp for user and godzilla
#frame4
#frame5

ss.hideturtle()
moon.hideturtle()
lc.hideturtle()
rc.hideturtle()
ss.hideturtle()
k.hideturtle()
hp1.hideturtle()
hp2.hideturtle()
e.hideturtle()
l.hideturtle()
m.hideturtle()
mp.hideturtle()
f.hideturtle()
s1.hideturtle()
h.hideturtle()
s2.hideturtle()
st.hideturtle()
g.hideturtle()
g1.hideturtle()
c.hideturtle()
t.hideturtle()
ar.hideturtle()
win.hideturtle()
r1.hideturtle()
r2.hideturtle()
r3.hideturtle()
wo1.hideturtle()
wo2.hideturtle()
wo3.hideturtle()
q.hideturtle()
screen.tracer(0)


keycounter = 0
rock1there = 1
rock2there = 1
rock3there = 1
smallswordthere = 0
wood1there = 1
wood2there = 1
wood3there = 1

rockpos1 = [0,0,0,0]
rockpos2 = [0,0,0,0]
rockpos3 = [0,0,0,0]
rockcount = 0
smallswordpos = [0,0,0,0]
woodpos1 = [0,0,0,0]
woodpos2 = [0,0,0,0]
woodpos3 = [0,0,0,0]
woodcount = 0

fightswitch = 0

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sw = 0
key = ''
keypress = ''
keytotal = 10
keytotalu = 10

swordie = 0
manie = 0
godie = 0

framie3 = 0
gearie = 0

def text(phrase, lines):
  q.penup()
  q.goto(-320,240)
  q.pendown()

  q.fillcolor('black')
  q.begin_fill()
  for i in range(2):
    q.forward(640)
    q.right(90)
    q.forward(70)
    q.right(90)
  q.end_fill()

  q.penup()
  q.goto(-305,210 - (lines*5))
  q.pendown()
  q.color('white')
  q.write(f'{phrase}', align = 'left', font = ('Arial', 11, 'bold'))

def stickatk(x, y):
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()  

  mp.setheading(90)
  mp.forward(100)

  mp.penup()
  mp.goto(x+30, y+130)  
  mp.pendown()
 
 
  mp.circle(30)

  #right leg
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()

  mp.setheading(0)
  mp.right(45)
  mp.forward(50)

  mp.setheading(0)
  mp.right(90)
  mp.forward(50)

  #left leg
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()

  mp.setheading(0)
  mp.right(135)
  mp.forward(125)


  #right arm
  mp.penup()
  mp.goto(x, y+50)  
  mp.pendown()

  mp.setheading(0)
  mp.right(50)
  mp.forward(40)

  mp.setheading(0)
  mp.left(40)
  mp.forward(60)

  #left arm
  mp.penup()
  mp.goto(x, y+50)  
  mp.pendown()

  mp.setheading(180)
  mp.left(10)
  mp.forward(30)
  
  mp.setheading(180)
  mp.left(110)
  mp.forward(50)

  mp.setheading(180)
  mp.left(50)
  mp.forward(10)

  #moustache
  mp.setheading(270)
  mp.penup()
  mp.goto(x-18, y+110)
  mp.pendown()

  mp.begin_fill()
  mp.circle(10)
  mp.end_fill()
 
  mp.penup()
  mp.goto(x+2, y+110)
  mp.pendown()

  mp.begin_fill()
  mp.circle(10)
  mp.end_fill()

  #eyes
  mp.penup()
  mp.goto(x-15, y+130)
  mp.pendown()

  mp.begin_fill()
  mp.circle(3)
  mp.end_fill()
 
  mp.penup()
  mp.goto(x+15, y+130)
  mp.pendown()

  mp.begin_fill()
  mp.circle(3)
  mp.end_fill()
 
  screen.update()

def winner(x,y, words):

  f.penup()
  f.goto(-320,120)
  f.pendown()
  f.fillcolor('yellow')
  f.begin_fill()
  for i in range(2):
    f.forward(640)
    f.right(90)
    f.forward(240)
    f.right(90)
  f.end_fill()
   
 
  f.penup()
  f.goto(x,y)
  f.pendown()
  f.color('blue')
  f.write(f'{words}', align = 'center', font = ('Eccentric Std', 50, 'bold', 'italic'))

  f.penup()
  f.goto(x,y-50)
  f.pendown()
  f.color('blue')
  f.write('You have beat the game. Returning to menu...', align = 'center', font = ('Eccentric Std', 22, 'bold', 'italic'))

  screen.update()

def smallsword():
    x = random.randrange(-300,300)
    y = random.randrange(-220,-40)
    
    ss.pensize(3)
    ss.penup()
    ss.goto(x,y)
    ss.pendown()

    ss.setheading(90)
    ss.forward(20)
    ss.penup()
    ss.goto(x,y+5)
    ss.pendown()
    ss.setheading(0)
    ss.forward(5)
    ss.forward(-10)

    global smallswordpos
    smallswordpos[0] = (x-5)
    smallswordpos[1] = (x+5)
    smallswordpos[2] = (y+20)
    smallswordpos[3] = (y)

    screen.update()

def rock1():
  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  r1.penup()
  r1.goto(x,y)
  r1.pendown()
  
  r1.color('gray')
  r1.fillcolor('gray')

  r1.begin_fill()
  r1.circle(8)
  r1.end_fill()

  r1.forward(8)
  r1.begin_fill()
  r1.circle(8)
  r1.end_fill()

  global rockpos1
  rockpos1[0] = (x-8)
  rockpos1[1] = (x+16)
  rockpos1[2] = (y+16)
  rockpos1[3] = (y)

def rock2():
  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  r2.penup()
  r2.goto(x,y)
  r2.pendown()
  
  r2.color('gray')
  r2.fillcolor('gray')

  r2.begin_fill()
  r2.circle(8)
  r2.end_fill()

  r2.forward(8)
  r2.begin_fill()
  r2.circle(8)
  r2.end_fill()

  global rockpos2
  rockpos2[0] = (x-8)
  rockpos2[1] = (x+16)
  rockpos2[2] = (y+16)
  rockpos2[3] = (y)

def rock3():
  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  r3.penup()
  r3.goto(x,y)
  r3.pendown()
  
  r3.color('gray')
  r3.fillcolor('gray')

  r3.begin_fill()
  r3.circle(8)
  r3.end_fill()

  r3.forward(8)
  r3.begin_fill()
  r3.circle(8)
  r3.end_fill()

  global rockpos3
  rockpos3[0] = (x-8)
  rockpos3[1] = (x+16)
  rockpos3[2] = (y+16)
  rockpos3[3] = (y)


def wood1():

  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  
  wo1.penup()
  wo1.goto(x,y)
  wo1.pendown()
  
  wo1.color('#D58300')
  wo1.fillcolor('#D58300')

  wo1.begin_fill()
  for i in range(2):
    wo1.forward(25)
    wo1.right(90)
    wo1.forward(12)
    wo1.right(90)
  wo1.end_fill()

  global woodpos1
  woodpos1[0] = (x)
  woodpos1[1] = (x+25)
  woodpos1[2] = (y)
  woodpos1[3] = (y-12)

def wood2():

  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  
  wo2.penup()
  wo2.goto(x,y)
  wo2.pendown()
  
  wo2.color('#D58300')
  wo2.fillcolor('#D58300')

  wo2.begin_fill()
  for i in range(2):
    wo2.forward(25)
    wo2.right(90)
    wo2.forward(12)
    wo2.right(90)
  wo2.end_fill()

  global woodpos2
  woodpos2[0] = (x)
  woodpos2[1] = (x+25)
  woodpos2[2] = (y)
  woodpos2[3] = (y-12)


def wood3():

  x = random.randrange(-300,300)
  y = random.randrange(-220,-40)
  
  wo3.penup()
  wo3.goto(x,y)
  wo3.pendown()
  
  wo3.color('#D58300')
  wo3.fillcolor('#D58300')

  wo3.begin_fill()
  for i in range(2):
    wo3.forward(25)
    wo3.right(90)
    wo3.forward(12)
    wo3.right(90)
  wo3.end_fill()

  global woodpos3
  woodpos3[0] = (x)
  woodpos3[1] = (x+25)
  woodpos3[2] = (y)
  woodpos3[3] = (y-12)

def start(x, y, text, color):
  st.pensize(4)
  st.penup()
  st.goto(0,85)
  st.pendown()
 
  st.color('white')
  st.write("Godzilla Attack", align = "center", font = ("times new roman", 32, "bold"))

  st.penup()
  st.goto(0,75-30)
  st.pendown()
  st.write("By Hok Chiu Shen", align = "center", font = ("times new roman", 20, "bold"))
  
  st.color('black')
  st.pensize(4)
  st.penup()
  st.goto(x,y)
  st.pendown()
  st.fillcolor(f'{color}')

  st.begin_fill()
  for i in range(2):
    #120x60 pixels rectangle
    st.forward(120)
    st.right(90)
    st.forward(60)
    st.right(90)
  st.end_fill()

  st.penup()
  st.goto(x+63, y-45)
  st.pendown()
  st.write(f"{text}", align = "center", font = ("times new roman", 17, "bold"))
 
  screen.update()

def start2(x, y, text, color):

  st.color('black')
  st.pensize(4)
  st.penup()
  st.goto(x,y)
  st.pendown()
  st.fillcolor(f'{color}')

  st.begin_fill()
  for i in range(2):
    #120x60 pixels rectangle
    st.forward(120)
    st.right(90)
    st.forward(60)
    st.right(90)
  st.end_fill()

  st.penup()
  st.goto(x+63, y-45)
  st.pendown()
  st.write(f"{text}", align = "center", font = ("times new roman", 17, "bold"))
 
  screen.update()


starts = 0
how = 0
arrowie = 0
fr1 = 0
stopier = 0
stopiew = 0
test = 0

#User Mouse interactions
def click(x,y):
  global starts
  global how
  global arrowie
  global fr1
  global gearie
  global rockcount
  global woodcount
  global wood1there
  global wood2there
  global wood3there
  global rock1there
  global rock2there
  global rock3there
  global smallswordthere
  global sw
  global stopier
  global stopiew
  global fightswitch
  global smallswordpos
  global test
  test += 1
  
  if test < 30 and fightswitch == 1:
    clickamt = 30-test
    text('You need to power up to fight Godzilla, so please let click become 0. \nReminder to not spam, but click slowly, do not rush!', 2)
    start2(60, -100, f'Clicks: {clickamt}', 'red')
    print(f"You need {clickamt} more clicks to move on")
  elif test >= 30 and fightswitch == 1:
    turtle.clearscreen()
    screen.tracer(0)
    st.clear()
    k.penup()
    k.goto(-40,-80)
    k.pendown()
    k.pensize(3)
    k.color('black')
    k.fillcolor('white')
    print('Press the correct key to hurt Godzilla!')
    k.begin_fill()
    for i in range(4):
      k.forward(80)
      k.right(90)
    k.end_fill()
    st.clear()
    k.penup()
    k.goto(0,-148)
    k.pendown()
    whitereset()
    smallswordthere = 1
    whitereset()
    stickatk(-170,0)
    upsword(-105,50)
    gods(70,90)
    randomkey()
    screen.onkeypress(a_key,'a')
    screen.onkeypress(b_key,'b')
    screen.onkeypress(c_key,'c')
    screen.onkeypress(d_key,'d')
    screen.onkeypress(e_key,'e')
    screen.onkeypress(f_key,'f')
    screen.onkeypress(g_key,'g')
    screen.onkeypress(h_key,'h')
    screen.onkeypress(i_key,'i')
    screen.onkeypress(j_key,'j')
    screen.onkeypress(k_key,'k')
    screen.onkeypress(l_key,'l')
    screen.onkeypress(m_key,'m')
    screen.onkeypress(n_key,'n')
    screen.onkeypress(o_key,'o')
    screen.onkeypress(p_key,'p')
    screen.onkeypress(q_key,'q')
    screen.onkeypress(r_key,'r')
    screen.onkeypress(s_key,'s')
    screen.onkeypress(t_key,'t')
    screen.onkeypress(u_key,'u')
    screen.onkeypress(v_key,'v')
    screen.onkeypress(w_key,'w')
    screen.onkeypress(x_key,'x')
    screen.onkeypress(y_key,'y')
    screen.onkeypress(z_key,'z')
    screen.listen()


  if (x >= smallswordpos[0] and x <= smallswordpos[1] and y <= smallswordpos[2] and y >= smallswordpos[3] and smallswordthere == 0):
    text('You Have found the Sword. Click again.', 1)
    print('You have found the legendary sword!')
    smallswordthere = 1
    ss.clear()
    fightswitch = 1

  
  if (x >= woodpos1[0] and x <= woodpos1[1] and y <= woodpos1[2] and y >= woodpos1[3] and wood1there == 0):
    print('You found a peice wood')
    woodcount += 1
    print('Woods:', woodcount)
    wo1.clear()
    wood1there = 1

  if (x >= woodpos2[0] and x <= woodpos2[1] and y <= woodpos2[2] and y >= woodpos2[3] and wood2there == 0):
    print('You found a peice wood')
    woodcount += 1
    print('Woods:', woodcount)
    wo2.clear()
    wood2there = 1

  if (x >= woodpos3[0] and x <= woodpos3[1] and y <= woodpos3[2] and y >= woodpos3[3] and wood3there == 0):
    print('You found a peice wood')
    woodcount += 1
    print('Woods:', woodcount)
    wo3.clear()
    wood3there = 1
  
  if (x >= rockpos1[0]  and x <= rockpos1[1] and y <= rockpos1[2] and y >= rockpos1[3] and rock1there == 0):
    print("You found a rock")
    rockcount += 1
    print('Rocks:', rockcount)
    r1.clear()
    rock1there = 1
  if (x >= rockpos2[0]  and x <= rockpos2[1] and y <= rockpos2[2] and y >= rockpos2[3] and rock2there == 0):
    print("You found a rock")
    rockcount += 1
    print('Rocks:', rockcount)
    r2.clear()
    rock2there = 1
  if (x >= rockpos3[0]  and x <= rockpos3[1] and y <= rockpos3[2] and y >= rockpos3[3] and rock3there == 0):
    print("You found a rock")
    rockcount += 1
    print('Rocks:', rockcount)
    r3.clear()
    rock3there = 1

  if woodcount == 3 and stopier == 0:
    print("You have found all the wood pieces!")
    stopier += 1
    if rockcount == 3 and sw == 0:
      text('A black sword has appeared. Find it to fight Godzilla', 1)
      print('There is a legendary sword. Find it to fight Godzilla!')
      smallsword()
      print("Spawn?")
      sw = 1
  if rockcount == 3 and stopiew == 0:
    stopiew += 1
    print("You have found all the rock pieces!")
    if woodcount == 3 and sw == 0:
      text('A black sword has appeared, find it to fight Godzilla', 1)
      print('There is a legendary sword. Find it to fight Godzilla!')
      smallsword()
      sw = 1
  if (x >= 250 and x <= 305 and y <= -170 and y >= -225 and gearie == 0):
    print("This is Hok Chiu Shen's Interactive story project featuring the all mighty Godzilla. You are a tiny person walking on a bridge in the city when suddenly Godzilla appears. You have to try you best to escape him while he chases you down trying to satisfy his tummy. Have Fun! Ver.1.0")
  if (x >= -60 and x <= 60 and y <= -80 and y >= -140 and how == 0):
    print('Instructions - Help')
    how = 1
    starts = 1
    st.clear()
    c.penup()
    c.goto(0, 90)
    c.pendown()
    c.color('red')
    c.write("Instructions -Help", align = "center", font = ("times new roman", 25, "bold"))
    c.color('black')
    c.penup()
    c.goto(0,-30)
    c.color('white')
    c.pendown()
    c.write("Instructions will be explained throughout the story so go play \nthe game. There is also a gray gear sign on the bottom right of \nthe screen where you can press for a little description of the game. \nLosing is not recommended as it may worsen game performance.", align = "center", font = ("times new roman", 16, "bold"))
    c.penup()
    c.goto(0, -90)
    c.pendown()
    arrowie = 1
    arrow(-220,-150)
    c.color('red')
    c.write('Press the arrow to return back to menu', align = "center", font = ("times new roman", 28, "bold"))
    
  if (x >= -250 and x <= -170 and y <= -135 and y >= -190 and arrowie == 1):
    arrowie = 0
    restart()

  if (x >= -60 and x <= 60 and y <= 30 and y >= -30 and starts == 0):
    starts = 1
    how = 1
    st.clear()
    c.color('white')
    print('Story is starting soon...')
    c.write("Story is now starting in 3", align = "center", font = ("times new roman", 17, "bold"))
    time.sleep(1)
    c.clear()
    c.write("Story is now starting in 2", align = "center", font = ("times new roman", 17, "bold"))
    time.sleep(1)
    c.clear()
    c.write("Story is now starting in 1", align = "center", font = ("times new roman", 17, "bold"))
    time.sleep(1)
    c.clear()
    c.color('red')
    c.write("Starting Story...", align = "center", font = ("times new roman", 25, "bold"))
    time.sleep(1)
    print('Story Started!')
    c.clear()
    frame1()
    car_colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "black", ]
    col1 = random.choice(car_colors)
    col2 = random.choice(car_colors)
    x1 = 250
    x2 = -310
    inf = 1
    cars = 0
    t.penup()
    t.goto(0,0)
    t.pendown()


    moo = 0
    window = 0
    caring = 0

    while inf != 0:
      moon.clear()
      rc.clear()
      lc.clear()

      moon.color = ('yellow')
      moon.fillcolor('yellow')
      if moo == 1 or moo == 3:
        moon.penup()
        moon.goto(-270, 180)
        moon.pendown()
        moon.begin_fill()
        moon.setheading(0)
        moon.circle(20)
        moon.end_fill()
        moo = 2
        if moo == 3:
          moo = 4
      elif moo == 2:
        moon.penup()
        moon.goto(-270, 190)
        moon.pendown()
        moon.begin_fill()
        moon.setheading(0)
        moon.circle(10)
        moon.end_fill()
        moo = 3
      else:
        moon.penup()
        moon.goto(-270, 170)
        moon.pendown()
        moon.begin_fill()
        moon.setheading(0)
        moon.circle(30)
        moon.end_fill()
        moo = 1
        if moo == 4:
          moo = 0
      
      
      
      if (x1 <= -315):
        x1 = 250
        col1 = random.choice(car_colors)
        cars += 1
        #we can make a sleep function along with random to randomly make cars pop out
      elif (x2 >= 270):
        x2 = -310
        col2 = random.choice(car_colors)
        cars += 1
      else:
        #right cars
        #body
        rc.color(col1)
        rc.fillcolor(col1)
        rc.penup()
        rc.goto(x1, -205)
        rc.pendown()
        rc.begin_fill()
        rc.setheading(90)
        rc.forward(20)
        rc.right(90)
        rc.forward(10)
        rc.left(90)
        rc.forward(15)
        rc.right(90)
        rc.forward(40)
        rc.right(90)
        rc.forward(15)
        rc.left(90)
        rc.forward(10)
        rc.right(90)
        rc.forward(20)
        rc.right(90)
        rc.forward(40)
        rc.end_fill()
        #windows
        rc.color("light blue")
        rc.fillcolor("light blue")
        rc.penup()
        rc.goto((x1 + 15), -175)
        rc.pendown()
        rc.begin_fill()
        rc.setheading(0)
        for i in range(2):
            rc.forward(30)
            rc.right(90)
            rc.forward(12)
            rc.right(90)
        rc.end_fill()
        #car lights()
        rc.color("yellow")
        rc.fillcolor("yellow")
        rc.penup()
        rc.goto((x1 + 5), -198)
        rc.pendown()
        rc.begin_fill()
        rc.setheading(0)
        rc.circle(3)
        rc.end_fill()
        #wheels
        rc.color("black")
        rc.fillcolor("black")
        rc.penup()
        rc.goto((x1 + 10), -220)
        rc.pendown()
        rc.begin_fill()
        rc.circle(10)
        rc.end_fill()
        rc.penup()
        rc.goto((x1 + 50), -220)
        rc.pendown()
        rc.begin_fill()
        rc.circle(10)
        rc.end_fill()

        #left cars
        #body
        lc.color(col2)
        lc.fillcolor(col2)
        lc.penup()
        lc.goto(x2, -205)
        lc.pendown()
        lc.begin_fill()
        lc.setheading(90)
        lc.forward(20)
        lc.right(90)
        lc.forward(10)
        lc.left(90)
        lc.forward(15)
        lc.right(90)
        lc.forward(40)
        lc.right(90)
        lc.forward(15)
        lc.left(90)
        lc.forward(10)
        lc.right(90)
        lc.forward(20)
        lc.right(90)
        lc.forward(40)
        lc.end_fill()
        #windows
        lc.color("light blue")
        lc.fillcolor("light blue")
        lc.penup()
        lc.goto((x2 + 15), -175)
        lc.pendown()
        lc.begin_fill()
        lc.setheading(0)
        for i in range(2):
            lc.forward(30)
            lc.right(90)
            lc.forward(12)
            lc.right(90)
        lc.end_fill()
        #car lights
        lc.color("yellow")
        lc.fillcolor("yellow")
        lc.penup()
        lc.goto((x2 + 55), -198)
        lc.pendown()
        lc.begin_fill()
        lc.setheading(0)
        lc.circle(3)
        lc.end_fill()
        #wheels
        lc.color("black")
        lc.fillcolor("black")
        lc.penup()
        lc.goto((x2 + 10), -220)
        lc.pendown()
        lc.begin_fill()
        lc.circle(10)
        lc.end_fill()
        lc.penup()
        lc.goto((x2 + 50), -220)
        lc.pendown()
        lc.begin_fill()
        lc.circle(10)
        lc.end_fill()
        screen.update()
        time.sleep(0.1/6)
       
        
        
        
        x1 -= 50
        x2 += 50
        caring += 1
        if caring == 70:
            break
        else:
            continue
    fr1 = 1
    frame1()

def fat(x,y, words):

  f.penup()
  f.goto(-320,120)
  f.pendown()
  f.fillcolor('black')
  f.begin_fill()
  for i in range(2):
    f.forward(640)
    f.right(90)
    f.forward(240)
    f.right(90)
  f.end_fill()
   
 
  f.penup()
  f.goto(x,y)
  f.pendown()
  f.color('red')
  f.write(f'{words}', align = 'center', font = ('Eccentric Std', 40, 'bold', 'italic'))

  f.penup()
  f.goto(x,y-50)
  f.pendown()
  f.color('red')
  f.write('Returning to menu...', align = 'center', font = ('Eccentric Std', 20, 'bold', 'italic'))

  screen.update()

def manatkmov():
  global manie
  global swordie
  mov = 10
  mov2 = -10
  spot = 0
  x1 = -170
  x2 = -105
  
  while True:
    if spot == 1:
      mp.clear()
      s2.clear()
      
      stickatk((x1 + mov) + mov2,0)
      upsword((x2 + mov) + mov2,50)
      mov2 -= 25
      if mov2 <= -170:
        break
    else:
      mp.clear()
      s2.clear()
      
      stickatk(x1 + mov,0)
      upsword(x2 + mov,50)
      mov += 25
      if mov >= 130:
        spot = 1
  screen.update()

def godatkmov():
  global godie
  g.speed(100)
  mov = 10
  mov2 = -10
  spot = 0
  x1 = 70
  
  while True:
    if spot == 1:
      g.clear()
      g1.clear()
      gods((x1 + mov) + mov2,90)
      mov2 += 50
      screen.update()
      if mov2 >= 150:
        break
    else:
      g.clear()
      g1.clear()
      gods(x1 + mov,90)
      mov -= 50
      if mov <= -140:
        spot = 1
      screen.update()

def userhp(per):
  hp1.penup()
  hp1.goto(-100,-150)
  hp1.pendown()

  hp1.color('red')
  hp1.fillcolor('red')
  hp1.setheading(180)
  hp1.begin_fill()
  for i in range(2):
    hp1.forward(20*per)
    hp1.left(90)
    hp1.forward(30)
    hp1.left(90)
  hp1.end_fill()



def godhp(per):
  hp2.penup()
  hp2.goto(100,-150)
  hp2.pendown()

  hp2.color('red')
  hp2.fillcolor('red')
  hp2.setheading(0)
  hp2.begin_fill()
  for i in range(2):
    hp2.forward(20*per)
    hp2.right(90)
    hp2.forward(30)
    hp2.right(90)
  hp2.end_fill()




def a_key():
  key = 'a'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def b_key():
  key = 'b'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def c_key():
  key = 'c'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def d_key():
  key = 'd'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def e_key():
  key = 'e'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def f_key():
  key = 'f'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def g_key():
  key = 'g'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def h_key():
  key = 'h'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def i_key():
  key = 'i'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def j_key():
  key = 'j'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def k_key():
  key = 'k'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def l_key():
  key = 'l'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def m_key():
  key = 'm'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def n_key():
  key = 'n'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def o_key():
  key = 'o'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def p_key():
  key = 'p'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def q_key():
  key = 'q'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def r_key():
  key = 'r'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def s_key():
  key = 's'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def t_key():
  key = 't'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def u_key():
  key = 'u'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def v_key():
  key = 'v'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def w_key():
  key = 'w'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def x_key():
  key = 'x'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def y_key():
  key = 'y'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()
def z_key():
  key = 'z'
  global keypress
  global keytotal
  global keytotalu
  if key == keypress:
    if keytotal == 0:
      print('You have defeated Godzilla!')
      hp2.clear()
      godhp(keytotal)
      turtle.clearscreen()
      turtle.tracer(0)
      frame5()
      time.sleep(3)
      winner(0,0, 'Winner!')
      time.sleep(3)
      restart()
    else:
      if keytotal != 0:
        manatkmov()
        randomkey()
        keytotal -= 1
  else:
    if keytotalu == 0:
      print('You have been defeated by Godzilla!')
      fat(0,0, 'Defeated By Godzilla')
      print('Weak.')
      time.sleep(3)
      restart()
    else:
      print('Incorrect!')
      godatkmov()
      keytotalu -= 1
      randomkey()

def randomkey():
  global keypress
  global keytotal
  global keytotalu
  keypress = random.choice(alphabet)
  showkey(f'{keypress}')
  hp1.clear()
  hp2.clear()
  userhp(keytotalu)
  godhp(keytotal)

def showkey(key):
  k.penup()
  k.goto(-40,-80)
  k.pendown()
  k.pensize(3)
  k.color('black')
  k.fillcolor('white')

  k.begin_fill()
  for i in range(4):
    k.forward(80)
    k.right(90)
  k.end_fill()

  k.penup()
  k.goto(0,-148)
  k.pendown()
  
  k.write(f'{key}', align = 'center', font = ('Chewy', 35, 'bold'))

  screen.update()

def gear(x,y):
  h.color('gray')
  h.fillcolor('gray')
  h.setheading(0)
  h.penup()
  h.goto(x,y)
  h.pendown()

  h.begin_fill()
  h.circle(13)
  h.end_fill()

  h.penup()
  h.goto(x,y+13)
  h.pendown()
  hr = 0
  for i in range(8):
    h.right(hr)
    hr+=45
    h.pensize(5)
    h.forward(25)
    h.forward(-25)

  screen.update()

def restart(x,y):
  h.pensize(7)
  h.setheading(270)
  h.penup()
  h.goto(x,y)
  h.pendown()
 
  h.circle(25, 260)

  screen.update()


def dead(x,y):
  #open mouth
  g.setheading(0)
  g.clear()
  g.color("red")
  g.fillcolor("red")
  g.penup()
  g.goto(x-5, y)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  g.forward(10)
  g.right(110)
  g.forward(10)
  g.end_fill()
 
  g.color('black')
  g.fillcolor('black')
  g.setheading(0)
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  for i in range(3):
    g.forward(50)
    g.right(90)
  g.right(70)
  g.forward(25)
  g.left(90)
  g.forward(15)
  g.left(70)
  g.forward(20)
  g.goto(x-25, y+25)
  g.end_fill()
 
  #top head
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  g.setheading(45)
  g.goto(x, y+35)
  g.goto(x+25, y+25)
  g.end_fill()


  g.pensize(1)
  g.color("dark blue")
  g.fillcolor("dark blue")
  x1 = x
  y1 = y
  for i in range(1, 5):
    g.penup()
    g.goto(x1+(30*i), y1-(10*i))
    g.pendown()
    g.begin_fill()
    g.setheading(25)
    g.forward(40)
    g.right(145)
    g.forward(40)
    g.goto(x1+(30*i), y1-(10*i))
    g.end_fill()
   
  g.penup()
  g.goto(x1+(140), y1-(58))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(140), y1-(58))
  g.end_fill()

  g.penup()
  g.goto(x1+(160), y1-(75))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(160), y1-(75))
  g.end_fill()

  g.penup()
  g.goto(x1+(180), y1-(95))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(180), y1-(95))
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+25, y-10)
  g.pendown()
  g.setheading(315)
  g.begin_fill()
  g.goto(x+130, y-45)
  g.forward(100)
  g.setheading(180)
  g.forward(190)
  g.goto(x+25, y-10)
  g.end_fill()

  g.color("dark blue")
  g.fillcolor("dark blue")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  x2 = x+195
  y2 = y-113
  g.pensize(2)
  for i in range(1, 9):
    g.penup()
    g.goto(x2 + (8*i), y2)
    g.pendown()
    g.setheading(90)
    g.forward(10)
   
 
  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  g.setheading(0)
  for i in range(6, 3, -1):
    g.pensize(i)
    g.forward(25)

  g.penup()
  g.goto(x+170, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+80, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+35, y-60)
  g.pendown()
  g.setheading(155)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+30, y-60)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.color("light blue")
  g.fillcolor("light blue")
  g.penup()
  g.goto(x-17, y+20)
  g.pendown()
  g.begin_fill()
  g.circle(4)
  g.end_fill()

  g.color("red")
  g.fillcolor("red")
  g.penup()
  g.goto(x+50, y-50)
  g.pendown()
  g.begin_fill()
  g.circle(30)
  g.end_fill()

  g.penup()
  g.goto(x+90, y-80)
  g.pendown()
  g.begin_fill()
  g.circle(15)
  g.end_fill()
 
  screen.update()

def gods(x, y):
  g.color("black")
  g.fillcolor("black")
  #open mouth
  g.setheading(0)
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  for i in range(3):
    g.forward(50)
    g.right(90)
  g.right(70)
  g.forward(25)
  g.left(90)
  g.forward(15)
  g.left(70)
  g.forward(20)
  g.goto(x-25, y+25)
  g.end_fill()
 
  #top head
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  g.setheading(45)
  g.goto(x, y+35)
  g.goto(x+25, y+25)
  g.end_fill()


  g.pensize(1)
  g.color("dark blue")
  g.fillcolor("dark blue")
  x1 = x
  y1 = y
  for i in range(1, 5):
    g.penup()
    g.goto(x1+(30*i), y1-(10*i))
    g.pendown()
    g.begin_fill()
    g.setheading(25)
    g.forward(40)
    g.right(145)
    g.forward(40)
    g.goto(x1+(30*i), y1-(10*i))
    g.end_fill()
   
  g.penup()
  g.goto(x1+(140), y1-(58))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(140), y1-(58))
  g.end_fill()

  g.penup()
  g.goto(x1+(160), y1-(75))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(160), y1-(75))
  g.end_fill()

  g.penup()
  g.goto(x1+(180), y1-(95))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(180), y1-(95))
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+25, y-10)
  g.pendown()
  g.setheading(315)
  g.begin_fill()
  g.goto(x+130, y-45)
  g.forward(100)
  g.setheading(180)
  g.forward(190)
  g.goto(x+25, y-10)
  g.end_fill()

  g.color("dark blue")
  g.fillcolor("dark blue")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  x2 = x+195
  y2 = y-113
  g.pensize(2)
  for i in range(1, 9):
    g.penup()
    g.goto(x2 + (8*i), y2)
    g.pendown()
    g.setheading(90)
    g.forward(10)
   
 
  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  g.setheading(0)
  for i in range(6, 3, -1):
    g.pensize(i)
    g.forward(25)

  g.penup()
  g.goto(x+170, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+80, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+35, y-60)
  g.pendown()
  g.setheading(155)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+30, y-60)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.color("light blue")
  g.fillcolor("light blue")
  g.penup()
  g.goto(x-17, y+20)
  g.pendown()
  g.begin_fill()
  g.circle(4)
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x-14, y+15)
  g.pendown()
  g.setheading(90)
  g.forward(6)

  #eyes
  g.penup()
  g.goto(x-14, y+14)
  g.pendown()
  g.setheading(90)
  g.color("red")
  g.fillcolor("red")
  g.pensize(4)
  g.forward(6)
 
  screen.update()
 
#godzilla
def god(x, y):
  g.speed(100)
  g.setheading(0)
  g.clear()
  g.color("red")
  g.fillcolor("red")
  g.penup()
  g.goto(x-5, y)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  g.forward(10)
  g.right(110)
  g.forward(10)
  g.end_fill()
  g.penup()#godzilla
  g.goto(x-15, y)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  g.forward(10)
  g.right(110)
  g.forward(10)
  g.end_fill()

  g.penup()
  g.goto(x-8, y-22)
  g.pendown()
  g.setheading(135)
  g.begin_fill()
  g.forward(10)
  g.left(110)
  g.forward(10)
  g.end_fill()


  #head
  g.color("black")
  g.fillcolor("black")
  g1.color("black")
  g1.fillcolor("black")
 
 
 
  #closed mouth
  g1.setheading(0)
  g1.penup()
  g1.goto(x-25, y+25)
  g1.pendown()
  g1.begin_fill()
  for i in range(4):
    g1.forward(50)
    g1.right(90)
  g1.end_fill()

  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  g.setheading(45)
  g.goto(x, y+35)
  g.goto(x+25, y+25)
  g.end_fill()


  g.pensize(1)
  g.color("dark blue")
  g.fillcolor("dark blue")
  x1 = x
  y1 = y
  for i in range(1, 5):
    g.penup()
    g.goto(x1+(30*i), y1-(10*i))
    g.pendown()
    g.begin_fill()
    g.setheading(25)
    g.forward(40)
    g.right(145)
    g.forward(40)
    g.goto(x1+(30*i), y1-(10*i))
    g.end_fill()
   
  g.penup()
  g.goto(x1+(140), y1-(58))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(140), y1-(58))
  g.end_fill()

  g.penup()
  g.goto(x1+(160), y1-(75))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(160), y1-(75))
  g.end_fill()

  g.penup()
  g.goto(x1+(180), y1-(95))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(180), y1-(95))
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+25, y-10)
  g.pendown()
  g.setheading(315)
  g.begin_fill()
  g.goto(x+130, y-45)
  g.forward(100)
  g.setheading(180)
  g.forward(190)
  g.goto(x+25, y-10)
  g.end_fill()

  g.color("dark blue")
  g.fillcolor("dark blue")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  x2 = x+195
  y2 = y-113
  g.pensize(2)
  for i in range(1, 9):
    g.penup()
    g.goto(x2 + (8*i), y2)
    g.pendown()
    g.setheading(90)
    g.forward(10)
   
 
  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  g.setheading(0)
  for i in range(6, 3, -1):
    g.pensize(i)
    g.forward(25)

  g.penup()
  g.goto(x+170, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+80, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+35, y-60)
  g.pendown()
  g.setheading(155)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+30, y-60)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.color("light blue")
  g.fillcolor("light blue")
  g.penup()
  g.goto(x-17, y+20)
  g.pendown()
  g.begin_fill()
  g.circle(4)
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x-14, y+15)
  g.pendown()
  g.setheading(90)
  g.forward(6)
 
  #CHANGE from open mouth to closed mouth
  screen.update()
  time.sleep(2)
  g1.clear()
  g.color("black")
  g.fillcolor("black")
 
  #open mouth
  g.setheading(0)
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  for i in range(3):
    g.forward(50)
    g.right(90)
  g.right(70)
  g.forward(25)
  g.left(90)
  g.forward(15)
  g.left(70)
  g.forward(20)
  g.goto(x-25, y+25)
  g.end_fill()
 
  #top head
  g.penup()
  g.goto(x-25, y+25)
  g.pendown()
  g.begin_fill()
  g.setheading(45)
  g.goto(x, y+35)
  g.goto(x+25, y+25)
  g.end_fill()


  g.pensize(1)
  g.color("dark blue")
  g.fillcolor("dark blue")
  x1 = x
  y1 = y
  for i in range(1, 5):
    g.penup()
    g.goto(x1+(30*i), y1-(10*i))
    g.pendown()
    g.begin_fill()
    g.setheading(25)
    g.forward(40)
    g.right(145)
    g.forward(40)
    g.goto(x1+(30*i), y1-(10*i))
    g.end_fill()
   
  g.penup()
  g.goto(x1+(140), y1-(58))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(140), y1-(58))
  g.end_fill()

  g.penup()
  g.goto(x1+(160), y1-(75))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(160), y1-(75))
  g.end_fill()

  g.penup()
  g.goto(x1+(180), y1-(95))
  g.pendown()
  g.begin_fill()
  g.setheading(25)
  g.forward(30)
  g.right(145)
  g.forward(30)
  g.goto(x1+(180), y1-(95))
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+25, y-10)
  g.pendown()
  g.setheading(315)
  g.begin_fill()
  g.goto(x+130, y-45)
  g.forward(100)
  g.setheading(180)
  g.forward(190)
  g.goto(x+25, y-10)
  g.end_fill()

  g.color("dark blue")
  g.fillcolor("dark blue")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  x2 = x+195
  y2 = y-113
  g.pensize(2)
  for i in range(1, 9):
    g.penup()
    g.goto(x2 + (8*i), y2)
    g.pendown()
    g.setheading(90)
    g.forward(10)
   
 
  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x+190, y-113)
  g.pendown()
  g.setheading(0)
  for i in range(6, 3, -1):
    g.pensize(i)
    g.forward(25)

  g.penup()
  g.goto(x+170, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+80, y-113)
  g.pendown()
  g.setheading(270)
  g.begin_fill()
  for i in range(2):
    g.forward(55)
    g.right(90)
    g.forward(25)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+35, y-60)
  g.pendown()
  g.setheading(155)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.penup()
  g.goto(x+30, y-60)
  g.pendown()
  g.setheading(225)
  g.begin_fill()
  for i in range(2):
    g.forward(40)
    g.right(90)
    g.forward(10)
    g.right(90)
  g.end_fill()

  g.color("light blue")
  g.fillcolor("light blue")
  g.penup()
  g.goto(x-17, y+20)
  g.pendown()
  g.begin_fill()
  g.circle(4)
  g.end_fill()

  g.color("black")
  g.fillcolor("black")
  g.penup()
  g.goto(x-14, y+15)
  g.pendown()
  g.setheading(90)
  g.forward(6)

 
  screen.update()

def arrow(x,y):
  ar.penup()
  ar.goto(x,y)
  ar.pendown()
  ar.setheading(0)
  ar.color('red')
  ar.fillcolor('red')

  ar.begin_fill()
  for i in range(2):
    ar.forward(50)
    ar.right(90)
    ar.forward(20)
    ar.right(90)
  ar.end_fill()

  ar.penup()
  ar.goto(x,y)
  ar.pendown()
  ar.begin_fill()
  ar.setheading(270)
  ar.forward(40)
  ar.right(135)
  ar.forward(40)
  ar.right(90)
  ar.forward(40)
  ar.end_fill()

  screen.update()

def downsword(x, y):
  s1.penup()
  s1.goto(x, y)  
  s1.pendown()
  #handle
  s1.setheading(270)
  s1.fillcolor('yellow')
  s1.begin_fill()
  for i in range(2):
    s1.forward(25)
    s1.left(90)
    s1.forward(10)
    s1.left(90)
  s1.end_fill()
 
  #sword blade
  s1.penup()
  s1.goto(x-10, y-25)  
  s1.pendown()
  s1.setheading(0)
  s1.fillcolor('white')
  s1.begin_fill()
  s1.forward(30)
  s1.right(90)
  s1.forward(60)
  s1.goto(x+5, y-105)
  s1.goto(x-10, y-85)
  s1.right(180)
  s1.forward(60)
  s1.end_fill()

  s1.penup()
  s1.goto(x+5, y-105)
  s1.pendown()
  s1.setheading(90)
  s1.forward(80)
 
  #wooden guard
  s1.fillcolor('brown')
  s1.penup()
  s1.goto(x-20, y-25)  
  s1.pendown()
  s1.setheading(0)
  s1.begin_fill()
  s1.forward(50)
  for i in range(2):
    s1.right(90)
    s1.forward(5)
    s1.right(90)
    s1.forward(50)
  s1.end_fill()
 
 
 
  screen.update()

def upsword(x, y):
  s2.penup()
  s2.goto(x, y)  
  s2.pendown()

  #handle
  s2.setheading(90)
  s2.fillcolor('yellow')
  s2.begin_fill()
  for i in range(2):
    s2.forward(25)
    s2.right(90)
    s2.forward(10)
    s2.right(90)
  s2.end_fill()

  #sword blade
  s2.penup()
  s2.goto(x-10, y+25)  
  s2.pendown()
  s2.fillcolor('white')
  s2.setheading(0)
  s2.begin_fill()
  s2.forward(30)
  s2.left(90)
  s2.forward(60)
  s2.goto(x+5, y+105)
  s2.goto(x-10, y+85)
  s2.right(180)
  s2.forward(60)
  s2.end_fill()

  s2.penup()
  s2.goto(x+5, y+105)
  s2.pendown()
  s2.setheading(270)
  s2.forward(80)

  #wooden guard
  s2.fillcolor('brown')
  s2.penup()
  s2.goto(x-20, y+25)  
  s2.pendown()
  s2.setheading(0)
  s2.begin_fill()
  s2.forward(50)
  for i in range(2):
    s2.right(90)
    s2.forward(5)
    s2.right(90)
    s2.forward(50)
  s2.end_fill()

 
  screen.update()


def stick(x,y,colour):
  mp.color(f'{colour}')
  mp.pensize(5)
  mp.setheading(0)

  mp.penup()
  mp.goto(x,y)
  mp.pendown()
 
  mp.circle(10)

  mp.penup()
  mp.goto(x,y)
  mp.pendown()

  mp.setheading(270)
  mp.forward(20)

  mp.left(45)
  mp.forward(10)
  mp.forward(-10)
 
  mp.right(90)
  mp.forward(10)
  mp.forward(-10)

  mp.penup()
  mp.goto(x,y)
  mp.pendown()

  mp.setheading(270)
  mp.forward(15)

  mp.setheading(45)
  mp.forward(8)
  mp.forward(-8)
 
  mp.left(90)
  mp.forward(8)
  mp.forward(-8)

  mp.color('black')
  mp.pensize(1)

  mp.penup()
  mp.goto(x-2,y+12)
  mp.pendown()

  mp.circle(1)

  mp.penup()
  mp.goto(x+3,y+12)
  mp.pendown()

  mp.circle(1)
  screen.update()




def stick2(x, y):
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()  

  mp.setheading(90)
  mp.forward(100)

  mp.penup()
  mp.goto(x+30, y+130)  
  mp.pendown()
 
 
  mp.circle(30)

  #right leg
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()

  mp.setheading(0)
  mp.right(45)
  mp.forward(50)

  mp.setheading(0)
  mp.right(90)
  mp.forward(50)

  #left leg
  mp.penup()
  mp.goto(x, y)  
  mp.pendown()

  mp.setheading(0)
  mp.right(135)
  mp.forward(50)

  mp.setheading(0)
  mp.right(90)
  mp.forward(50)

  #right arm
  mp.penup()
  mp.goto(x, y+50)  
  mp.pendown()

  mp.setheading(0)
  mp.right(10)
  mp.forward(30)

  mp.setheading(0)
  mp.right(110)
  mp.forward(70)

  #left arm
  mp.penup()
  mp.goto(x, y+50)  
  mp.pendown()

  mp.setheading(180)
  mp.left(10)
  mp.forward(30)

  mp.setheading(180)
  mp.left(110)
  mp.forward(70)

  #moustache
  mp.penup()
  mp.goto(x-18, y+110)
  mp.pendown()

  mp.begin_fill()
  mp.circle(10)
  mp.end_fill()
 
  mp.penup()
  mp.goto(x+2, y+110)
  mp.pendown()

  mp.begin_fill()
  mp.circle(10)
  mp.end_fill()

  #eyes
  mp.penup()
  mp.goto(x-15, y+130)
  mp.pendown()

  mp.begin_fill()
  mp.circle(3)
  mp.end_fill()
 
  mp.penup()
  mp.goto(x+15, y+130)
  mp.pendown()

  mp.begin_fill()
  mp.circle(3)
  mp.end_fill()
 
  screen.update()


def mountain(x, y, colour, size):
  m.color(f'{colour}')
  m.fillcolor(f'{colour}')

  m.penup()
  m.goto(x, y)  
  m.pendown()

  m.begin_fill()
  m.setheading(0)
  m.left(45)
  m.forward(size)
  m.right(90)
  m.forward(size)
  m.right(135)
  m.forward(size+50)
  m.end_fill()


def tree(times):
  for i in range(times):
    randtreex = random.randrange(-300,0)
    randtreey = random.randrange(-200,150)
    x = randtreex
    y = randtreey
   
    e.penup()
    e.goto(x, y)
    e.pendown()
   
    e.color('brown')
    e.fillcolor('brown')
   
    e.begin_fill()
    e.setheading(90)
    for i in range(2):
      e.forward(70)
      e.left(90)
      e.forward(20)
      e.left(90)
    e.end_fill()
   
    e.color('light green')
    e.fillcolor('light green')
 
   
    for i in range(60):
 
      addx = random.randrange((x-33), (x+21))
      addy = random.randrange((y+40), (y+90))
     
      e.penup()
      e.goto(addx, addy)
      e.pendown()
     
      e.begin_fill()
      e.circle(8)
      e.end_fill()

    screen.update()

def tree2(times):
  for i in range(times):
    randtreex = random.randrange(-320,320)
    randtreey = random.randrange(-240,-40)
    x = randtreex
    y = randtreey
   
    e.penup()
    e.goto(x, y)
    e.pendown()
   
    e.color('brown')
    e.fillcolor('brown')
   
    e.begin_fill()
    e.setheading(90)
    for i in range(2):
      e.forward(70)
      e.left(90)
      e.forward(20)
      e.left(90)
    e.end_fill()
   
    e.color('light green')
    e.fillcolor('light green')
 
   
    for i in range(60):
 
      addx = random.randrange((x-33), (x+21))
      addy = random.randrange((y+40), (y+90))
     
      e.penup()
      e.goto(addx, addy)
      e.pendown()
     
      e.begin_fill()
      e.circle(8)
      e.end_fill()

    screen.update()




#-----------------------------------------------------------------------------------------------------------------------------------------------------

def frame5():
  addy = 0
  
  while True:
    if ((200+addy) == 50):
      break
    else:
      s1.clear()
      mp.clear()
      g1.clear()
      g.clear()
      dead(-80,10) #(-80,10)
      stick2(-5,200+addy) #(-5,50)
      downsword(-10,180+addy) #(-10,30)
      addy -= 5
  screen.update()


#frame4 done


def frame3():
  global framie3
  l.penup()
  l.goto(-320,240)
  l.pendown()
  l.color('#060F48')
  l.fillcolor('#060F48')
  l.setheading(0)
  l.begin_fill()
  for i in range(2):
    l.forward(640)
    l.right(90)
    l.forward(480)
    l.right(90)
  l.end_fill()

  l.penup()
  l.goto(-320,0)
  l.pendown()
  l.color('#3FD849')
  l.fillcolor('#3FD849')
  l.setheading(0)
  l.begin_fill()
  for i in range(2):
    l.forward(640)
    l.right(90)
    l.forward(480)
    l.right(90)
  l.end_fill()
 
  mountain(-330,-10, '#3b8c3b', 250)
  mountain(0,0, '#03fc03', 200)
  mountain(-380,0, '#92de92', 120)
  mountain(100,0, '#3b8c3b', 100)
  mountain(150,0, '#0e4a0e', 100)
  mountain(-250,0, '#0e4a0e', 100)
  mountain(-100,0, '#92de92', 100)
  mountain(-150,0, '#03fc03', 100)
  mountain(230,0, '#92de92', 80)

  if framie3 == 1:
    tree2(40)
  
  screen.update()


def frame2():
  t.color('dark blue')
  t.fillcolor('dark blue')
  t.setheading(0)
  t.goto(-500,500)
  t.begin_fill()
  for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
  t.end_fill()
  l.penup()
  l.goto(0,180)
  l.pendown()
  l.color('#26e6ff')
  l.fillcolor('#26e6ff')
  l.setheading(0)
  l.begin_fill()
  for i in range(2):
        l.forward(320)
        l.right(90)
        l.forward(480)
        l.right(90)
  l.end_fill()

  x = 70
  y = 110
 
  l.penup()
  l.goto(x,y)
  l.pendown()
  l.setheading(90)
  countex = 0
  for i in range(9):
    l.penup()
    l.goto(x+countex,y)
    l.pendown()
    countex = (i*60)    
    l.color('dark blue')
    l.pensize(3)
    l.circle(15,180)

  x = 70
  y = 40
 
  l.penup()
  l.goto(x,y)
  l.pendown()
  l.setheading(90)
  countex = 0
  for i in range(9):
    l.penup()
    l.goto(x+countex,y)
    l.pendown()
    countex = (i*60)    
    l.color('dark blue')
    l.pensize(3)
    l.circle(15,180)
   

  x = 70
  y = -30
 
  l.penup()
  l.goto(x,y)
  l.pendown()
  l.setheading(90)
  countex = 0
  for i in range(9):
    l.penup()
    l.goto(x+countex,y)
    l.pendown()
    countex = (i*60)    
    l.color('dark blue')
    l.pensize(3)
    l.circle(15,180)

  x = 70
  y = -100
 
  l.penup()
  l.goto(x,y)
  l.pendown()
  l.setheading(90)
  countex = 0
  for i in range(9):
    l.penup()
    l.goto(x+countex,y)
    l.pendown()
    countex = (i*60)    
    l.color('dark blue')
    l.pensize(3)
    l.circle(15,180)
 
  screen.update()

  l.penup()
  l.goto(0,180)
  l.pendown()
  l.color('#00ff44')
  l.fillcolor('#00ff44')

  l.begin_fill()
  l.setheading(180)
  for i in range(2):
        l.forward(320)
        l.left(90)
        l.forward(480)
        l.left(90)
  l.end_fill()

  tree(40)
 
 
  screen.update()

def frame1():
  global gearie
  gearie = 1
  t.pencolor("#110E67")
  t.fillcolor("#110E67")
  t.penup()
  t.goto(-320, -100)
  t.pendown()
  t.begin_fill()
  t.forward(640)
  t.right(90)
  t.forward(140)
  t.right(90)
  t.forward(640)
  t.right(90)
  t.forward(140)
  t.end_fill()

  t.pencolor("black")
  t.fillcolor("black")
  t.penup()
  t.goto(-320, -240)
  t.pendown()
  t.setheading(90)
  for i in range(2):
    t.forward(480)
    t.right(90)
    t.forward(640)
    t.right(90)

  #buildings
  t.penup()
  t.goto(-320, 10)
  t.pendown()
  t.setheading(0)
  t.begin_fill()
  t.forward(40)
  t.left(90)
  t.forward(30)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(30)
  t.left(90)
  t.forward(20)

  t.left(90)
  t.forward(90)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(60)
  t.left(90)
  t.forward(80)

  t.left(90)
  t.forward(40)
  t.right(90)
  t.forward(180)
  t.right(90)
  t.forward(60)
  t.left(90)
  t.forward(40)

  t.left(45)
  t.goto(190, 80)
  t.goto(220, 20)
  t.setheading(0)

  t.left(90)
  t.forward(80)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(220)
  t.right(90)
  t.forward(640)
  t.right(90)
  t.forward(130)
  t.end_fill()

  #windows
  win.pencolor("yellow")
  win.fillcolor("yellow")
  win.penup()
  win.goto(-290, -20)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.right(180)
  win.forward(35)
  win.setheading(90)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.right(180)
  win.forward(35)
  win.setheading(90)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(-250, -20)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.right(180)
  win.forward(35)
  win.setheading(90)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.right(180)
  win.forward(35)
  win.setheading(90)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(-220, 80)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  for i in range(4):
    win.forward(60)
    win.right(90)
  win.end_fill()

  win.penup()
  win.goto(-210, -25)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(-170, -25)
  win.pendown()
  win.begin_fill()
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(-220, -60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.right(90)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.end_fill()

  win.penup()
  win.goto(-120, 20)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  for i in range(4):
    win.forward(40)
    win.right(90)
  win.end_fill()

  win.penup()
  win.goto(-120, -60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  for i in range(4):
    win.forward(40)
    win.right(90)
  win.end_fill()

  x = -40
  y = 120

  for i in range(3):
    y -= 60
    x = -40
    for n in range(4):
      win.penup()
      win.goto(x, y)
      win.pendown()
      win.begin_fill()
      win.setheading(0)
      win.forward(20)
      win.right(90)
      win.forward(40)
      win.right(90)
      win.forward(20)
      win.right(90)
      win.forward(40)
      win.end_fill()
      x += 40

  win.penup()
  win.goto(140, 0)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.right(90)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.end_fill()

  win.penup()
  win.goto(150, -60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(190, -60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(140, -80)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.right(90)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.end_fill()

  win.penup()
  win.goto(250, 60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.circle(10)
  win.end_fill()

  win.penup()
  win.goto(290, 60)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.circle(10)
  win.end_fill()

  y = 100

  for i in range(2):
    y -= 60
    x = 240
    for n in range(2):
      win.penup()
      win.goto(x, y)
      win.pendown()
      win.begin_fill()
      win.setheading(0)
      win.forward(20)
      win.right(90)
      win.forward(40)
      win.right(90)
      win.forward(20)
      win.right(90)
      win.forward(40)
      win.end_fill()
      x += 40

  win.penup()
  win.goto(240, -80)
  win.pendown()
  win.begin_fill()
  win.setheading(0)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.right(90)
  win.forward(60)
  win.right(90)
  win.forward(20)
  win.end_fill()

  #water light

  yellow_shades = ["#fffee8", "#d6d38d", "#e6dc09", "#fff866", "#d4ca06", "#c4c066", "#fff400", "#d6cf3a", "#e6de45", "#faf8d2", "#bdb746", "#fff754", "#fcf9c0", "#e8e166"]

  for i in range(120):
      x = random.randrange(-305, 310)
      y = random.randrange(-225, -130)
      random_yellow = random.choice(yellow_shades)
      t.penup()
      t.goto(x, y)
      t.pencolor(random_yellow)
      t.fillcolor(random_yellow)
      t.pendown()
      t.begin_fill()
      t.circle(8)
      t.end_fill()
         


  #Sky
  t.pencolor("yellow")
  t.fillcolor("yellow")
  #moon
  m.pencolor("yellow")
  m.fillcolor("yellow")
  m.penup()
  m.goto(-270, 170)
  m.pendown()
  m.begin_fill()
  m.setheading(0)
  m.circle(30)
  m.end_fill()
 
  t.pensize(5)
  t.penup()
  t.setheading(0)
  t.goto(-160, 220)
  t.pendown()
  t.begin_fill()
  for i in range(5):
    t.forward(15)
    t.right(144)
  t.end_fill()

  t.penup()
  t.goto(-40, 120)
  t.pendown()
  t.begin_fill()
  for i in range(5):
    t.forward(8)
    t.right(144)
  t.end_fill()

  t.penup()
  t.goto(240, 200)
  t.pendown()
  t.begin_fill()
  for i in range(5):
      t.forward(15)
      t.right(144)

  t.pensize(1)
  t.penup()
  t.goto(-160, 120)
  t.pendown()
  t.setheading(45)
  t.begin_fill()
  for i in range(4):
    t.forward(10)
    t.right(90)
  t.end_fill()

  t.penup()
  t.goto(132, 180)
  t.pendown()
  t.setheading(45)
  t.begin_fill()
  for i in range(4):
    t.forward(10)
    t.right(90)
  t.end_fill()

  t.penup()
  t.goto(290, 210)
  t.pendown()
  t.setheading(45)
  t.begin_fill()
  for i in range(4):
    t.forward(10)
    t.right(90)
  t.end_fill()
 
  t.pensize(2)
  t.color("yellow")
  t.penup()
  t.goto(-100, 160)
  t.pendown()
  t.begin_fill()
  t.setheading(225)
  t.forward(30)
  t.left(135)
  t.forward(20)
  t.right(125)
  t.forward(30)
  t.end_fill()

  t.penup()
  t.goto(80, 160)
  t.pendown()
  t.begin_fill()
  t.setheading(225)
  t.forward(30)
  t.left(135)
  t.forward(20)
  t.right(125)
  t.forward(40)
  t.end_fill()

  t.penup()
  t.goto(110, 160)
  t.pendown()
  t.begin_fill()
  t.setheading(225)
  t.forward(30)
  t.left(135)
  t.forward(20)
  t.right(125)
  t.forward(40)
  t.end_fill()

  t.penup()
  t.goto(180, 190)
  t.pendown()
  t.begin_fill()
  t.setheading(225)
  t.forward(30)
  t.left(135)
  t.forward(20)
  t.right(125)
  t.forward(40)
  t.end_fill()

  t.penup()
  t.goto(210, 190)
  t.pendown()
  t.begin_fill()
  t.setheading(225)
  t.forward(30)
  t.left(135)
  t.forward(20)
  t.right(125)
  t.forward(40)
  t.end_fill()

  t.pensize(1)
  t.fillcolor("grey")
  t.pencolor("grey")
  y = 150
  for i in range(2):
    y -= 15
    x = -300
    for n in range(3):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(10)
      t.end_fill()

  y = 170
  for i in range(5):
    y -= 5
    x = -220
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  y = 190
  for i in range(5):
    y -= 5
    x = -130
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  y = 210
  for i in range(5):
    y -= 5
    x = -30
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  y = 180
  for i in range(5):
    y -= 5
    x = 70
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  y = 210
  for i in range(5):
    y -= 5
    x = 160
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  y = 190
  for i in range(5):
    y -= 5
    x = 260
    for n in range(4):
      x += 10
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.left(20)
      t.end_fill()

  #cloud fixup
  t.penup()
  t.goto(-270, 150)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()
     
  t.penup()
  t.goto(-200, 190)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(-180, 170)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(0, 210)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(0, 220)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(10, 210)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(70, 190)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(90, 180)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(110, 170)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(170, 205)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(190, 195)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.penup()
  t.goto(210, 185)
  t.pendown()
  t.begin_fill()
  t.circle(10)
  t.left(20)
  t.end_fill()

  t.color("white")
  t.fillcolor("white")
  t.penup()
  t.goto(-300, 100)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(-235, 130)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(-200, 210)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(0, 135)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(-65, 105)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(90, 210)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(120, 120)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(240, 140)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.goto(280, 220)
  t.pendown()
  t.begin_fill()
  t.circle(5)
  t.end_fill()


  #bridge
  t.fillcolor("yellow")
  t.pencolor("black")
  t.penup()
  t.goto(-230, -200)
  t.pendown()
  t.begin_fill()
  t.setheading(0)
  t.circle(10)
  t.end_fill()

  t.penup()
  t.goto(230, -200)
  t.pendown()
  t.begin_fill()
  t.setheading(0)
  t.circle(10)
  t.end_fill()

  t.fillcolor("brown")
  t.pencolor("brown")
  t.pensize(5)
  t.penup()
  t.goto(220, -200)
  t.pendown()
  t.setheading(125)
  t.circle(268, 110)

  t.penup()
  t.goto(220, -230)
  t.pendown()
  t.setheading(125)
  t.circle(268, 110)

  t.pensize(10)
  t.penup()
  t.goto(-315, -220)
  t.pendown()
  t.goto(315, -220)

  t.fillcolor("turquoise")
  t.pencolor("turquoise")
  t.pensize(1)
  t.penup()
  t.goto(-240, -200)
  t.pendown()
  t.begin_fill()
  t.setheading(0)
  t.forward(20)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(40)
  t.end_fill()

  t.penup()
  t.goto(220, -200)
  t.pendown()
  t.begin_fill()
  t.setheading(0)
  t.forward(20)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(40)
  t.end_fill()

  #bidge right strings
  t.color("brown")
  t.pensize(3)
  x = 200
  y = -180
  list = []

  for i in range(3):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x -= 20
      y += 20
      list.append(x)
      list.append(y)
   
  x += 20
  y -= 20

  for i in range(5):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x -= 20
      y += 10
      list.append(x)
      list.append(y)

  x += 20
  y -= 10

  for i in range(5):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x -= 20
      y += 2.5
      list.append(x)
      list.append(y)
     

  #bride left strings
  x = -200
  y = -180

  for i in range(3):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x += 20
      y += 20
      list.append(x)
      list.append(y)

  x -= 20
  y -= 20

  for i in range(5):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x += 20
      y += 10
      list.append(x)
      list.append(y)

  x -= 20
  y -= 10

  for i in range(5):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(270)
      t.forward(23)
      x += 20
      y += 2.5
      list.append(x)
      list.append(y)


  x = 0
  y = 1

  t.penup()
  t.goto(180, -160)
  t.pendown()

  for i in range(26):
    if (i == 13):
      t.penup()
      t.goto(list[x], list[y])
      t.pendown()
      t.forward(25)
      x += 2
      y += 2
    else:
      t.goto(list[x], list[y])
      t.forward(25)
      x += 2
      y += 2

  t.penup()
  t.goto(220, -200)
  t.pendown()
  t.goto(200, -205)
  t.goto(180, -160)

  t.penup()
  t.goto(-220, -200)
  t.pendown()
  t.goto(-200, -205)
  t.goto(-180, -160)
  global fr1
  time.sleep(5)
  if fr1 == 1:
    mp.fillcolor('white')
    mp.color('white')
    stick(-100,-185,'white')
    god(90,-70)
    time.sleep(1)
    text('Godzilla has appeared in the city and is rampaging!', 1)
    time.sleep(2)
    text('What would you do? Run away or hide in the city?', 1)
    answer = screen.textinput("Godzilla Has Appeared", "Run or Hide?")
    time.sleep(2)
    if answer is None or (answer.lower() == 'hide'):
      text("You have been killed by Godzilla! Returning to menu...", 1)
      print('Cowardly death')
      fat(0,0, 'Death By Cowardice')
      time.sleep(3)
      restart()
    elif answer.lower() == 'run':
      text('You have sucessfully ran away from Godzilla!', 1)
      time.sleep(2)
      whitereset()
      frame2()
      stick(0,-185,'black')
      text('Oh no, there are two paths, please choose the correct path', 1)
      time.sleep(2)
      answer = screen.textinput("Two Roads", "Forest or Lake?")
      if answer is None or (answer.lower() == 'lake'):
        text("You have drowned to death! Returning to menu...", 1)
        fat(0,0, 'Death By Water')
        print('Incapable of Swimming')
        time.sleep(3)
        restart()
      elif answer.lower() == 'forest':
        text("You continued running into the forest. You are cold and want to find some wood and \nrocks for fire.", 2)
        time.sleep(5)
        whitereset()
        global framie3
        framie3 = 1
        frame3()
        global rock1there
        global rock2there
        global rock3there
        global wood1there
        global wood2there
        global wood3there
        global keycount
        rock1there = 0
        rock2there = 0
        rock3there = 0
        wood1there = 0
        wood2there = 0
        wood3there = 0
        rock1()
        rock2()
        rock3()
        wood1()
        wood2()
        wood3()
        stick(0,-185,'black')
        text("There are 3 rocks and 3 wooden planks spread across the forest, collect them by \nclicking on them to obtain them. Find all 6 items to continue.", 2)
      else:
        text("You have drowned to death! Returning to menu...", 1)
        fat(0,0, 'Death By Water')
        print('Incapable of Swimming')
        time.sleep(3)
        restart()
    else:
      text("You have been killed by Godzilla! Returning to menu...", 1)
      print('Cowardly death')
      fat(0,0, 'Death By Cowardice')
      time.sleep(3)
      restart()




def restart():
  screen.tracer(0)
  t.color('white')
  t.fillcolor('white')
  t.setheading(0)
  t.goto(-500,500)
  t.begin_fill()
  for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
  t.end_fill()
  screen.update()
  frame3()
  start(-60, 30, 'Start', 'yellow')
  start(-60, -80, 'How-2', 'white')
  gear(280,-210)
  global starts
  global keycount
  global how
  global arrowie
  global framie3
  global fr1
  global gearie
  global rockcount
  global woodcount
  global wood1there
  global wood2there
  global wood3there
  global rock1there
  global rock2there
  global rock3there
  global smallswordthere
  global sw
  global stopier
  global stopiew
  global smallswordpos
  global fightswitch
  global test
  starts = 0
  how = 0
  arrowie = 0
  framie3 = 0
  fr1 = 0
  keycount = 0
  stopier = 0
  test = 0
  sopiew = 0
  rock1there = 1
  rock2there = 1
  rock3there = 1
  smallswordthere = 0
  wood1there = 1
  wood2there = 1
  wood3there = 1
  rockpos1 = [0,0,0,0]
  rockpos2 = [0,0,0,0]
  rockpos3 = [0,0,0,0]
  rockcount = 0
  smallswordpos = [0,0,0,0]
  woodpos1 = [0,0,0,0]
  woodpos2 = [0,0,0,0]
  woodpos3 = [0,0,0,0]
  woodcount = 0
  fightswitch = 0
  sw = 0
  key = ''
  keypress = ''
  keytotal = 10
  keytotalu = 10
  swordie = 0
  manie = 0
  godie = 0
  framie3 = 0
  gearie = 0
  screen.onclick(click)
  screen.listen()
  screen.update()
 
def whitereset():
  t.color('white')
  t.fillcolor('white')
  t.setheading(0)
  t.goto(-500,500)
  t.begin_fill()
  for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(1000)
    t.right(90)
  t.end_fill()
  screen.update()





screen.onclick(click)



#screen.onkeypress(METHOD, '#key')


frame3()
start(-60, 30, 'Start', 'yellow')
start(-60, -80, 'How-2', 'white')
gear(280,-210)




screen.listen()
