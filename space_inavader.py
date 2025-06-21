import turtle
import os
import math as m
import random

wn=turtle.Screen()
wn.bgcolor('black')
wn.title('SPACE INVADER')
wn.bgpic("space_invaders_background.gif")

#register the shape
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")

#making_border
border_pen=turtle.Turtle()
border_pen.color('white')
border_pen.pensize(3)
border_pen.shape('arrow')
border_pen.speed(0)
border_pen.penup()
border_pen.setpos(-300,-300)
border_pen.pendown()


#set score to 0;
score=0
scorestring = "score: %s" % score
#draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color("white")
score_pen.setposition(-290,280)
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()


for i in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()

#creating player turtle
player=turtle.Turtle()
player.color('blue')
player.shape("player.gif")
player.speed(0)
player.penup()
player.setpos(0,-250)
player.setheading(90)


#creating bulllet
bullet=turtle.Turtle()
bullet.shape('triangle')
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=60

#bullet states
#ready=bullet is ready to be fired
#fired=bullet is fired
bulletstate="ready"


number_of_enemies=9
enemies=[]

#add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:

    enemy.shape("enemy.gif")
    enemy.color('red')
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setpos(x,y)


enemyspeed=10
playerspeed=15
#moving player left/right
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)


def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)
def fire_bullet():

    global bulletstate
    if bulletstate=="ready":
        #work only in macos
        os.system("afplay laser.wav&")
        bulletstate="fire"
        #moving the bullet to just above the player
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):

    distance=m.sqrt(pow((t1.xcor()-t2.xcor()),2) + pow((t1.ycor()-t2.ycor()),2))
    if distance<30:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,"space")

#main game loop
while True:
    for enemy in enemies:

        #moving enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #moving enemy back and down
        if(enemy.xcor()>280 or enemy.xcor()<-280):
            #moving all enemies down
            for e in enemies:
                y=e.ycor()
                y-=30
                e.sety(y)
            enemyspeed *= -1
            # checking collison

        if isCollision(bullet, enemy):
            # work only in macos
            os.system("afplay explosion.wav&")
            # reset the bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)
            #updating the score
            score+=10
            scorestring="score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            # work only in macos
            os.system("afplay explosion.wav&")
            player.hideturtle()
            for j in enemies:
                j.hideturtle()
            wn.bgpic("gameover_space.png")
            break

            
            
    #moving the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #if bullet reach the roof
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"

turtle.done()