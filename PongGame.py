import turtle
import json
import numpy as np
import winsound
from playsound import playsound
from random import randrange

with open (r"C:\Users\Usuario\Desktop\Python\PongGame\config.json", "r") as jsonfile:
    details_dict=json.load(jsonfile)

wi=float(details_dict["wid"])
he=float(details_dict["he"])

soundPathPaddle="C:/Users/Usuario/Desktop/Python/PongGame/sounds/Bouncepaddle.wav"
soundPathBorder="C:/Users/Usuario/Desktop/Python/PongGame/sounds/Bounceborder.wav"
soundPathBck="C:/Users/Usuario/Desktop/Python/PongGame/sounds/Techno.wav"
arrayColors=np.array(["blue", "yellow", "white", "red", "green", "orange", "pink"])

wn = turtle.Screen()
wn.title("Crazy Pong by SpanishGenghisKhan")
wn.bgcolor("black")
wn.setup(width=wi, height=he)
wn.tracer(0)
score_a=0
score_b=0
#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5,stretch_len=1,outline=2)
paddle_a.penup()
paddle_a.goto(float(details_dict["pos_pad_a"]),0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5,stretch_len=1,outline=2)
paddle_b.penup()
paddle_b.goto(float(details_dict["pos_pad_b"]),0)
#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
paddle_b.shapesize()
ball.penup()
ball.goto(0,0)
ball.dx=float(details_dict["speed_ball"])
ball.dy=float(details_dict["speed_ball"])
#Score title
score=turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0,260)
score.color("white")
score.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Arial",24,"normal"))


#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=float(details_dict["speed_paddle"])
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=float(details_dict["speed_paddle"])
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
    y+=float(details_dict["speed_paddle"])
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=float(details_dict["speed_paddle"])
    paddle_b.sety(y)


#Key Binds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#Main loop
x=randrange(4)
cont=0

#techno=winsound.PlaySound(soundPathBck, winsound.SND_NOSTOP)
showon=True
while True:
    wn.update()

    if showon==True:


    
        #moveball
        if x == 0:

            ball.setx(ball.xcor()+ball.dx*-1)
            ball.sety(ball.ycor()+ball.dy)
        elif x==1:
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy*-1)
        elif x==2:
            ball.setx(ball.xcor()+ball.dx*-1)
            ball.sety(ball.ycor()+ball.dy*-1)
        elif x==3:
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
        


            

        #Border Checking

        if ball.xcor() > float(details_dict["limitx"]):
            ball.goto(0,0)
            ball.dx=float(details_dict["speed_ball"])
            ball.dy=float(details_dict["speed_ball"])
            score_a+=1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Arial",24,"normal"))
        if ball.xcor() < - float(details_dict["limitx"]):
            ball.goto(0,0)
            ball.dx=float(details_dict["speed_ball"])
            ball.dy=float(details_dict["speed_ball"])
            score_b+=1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Arial",24,"normal"))

        if ball.ycor() > float(details_dict["limity"]):
            ball.sety(float(details_dict["limity"]))
            ball.dy*=-1
            winsound.PlaySound(soundPathBorder, winsound.SND_ASYNC)
        if ball.ycor() < -float(details_dict["limity"]):
            ball.sety(-float(details_dict["limity"]))
            ball.dy*=-1
            winsound.PlaySound(soundPathBorder, winsound.SND_ASYNC)
        #Bounce
        if ball.xcor()>float(details_dict["pos_pad_b"])-10 and (ball.ycor()>paddle_b.ycor()-40 and ball.ycor()<paddle_b.ycor()+40):
            ball.dx*=-1
            ball.dx*=1.1
            ball.dy*=1.1
            winsound.PlaySound(soundPathBorder, winsound.SND_ASYNC)
            if cont==len(arrayColors):
                cont=0
                ball.color(arrayColors[cont])
                paddle_a.color(arrayColors[cont])
                paddle_b.color(arrayColors[cont])

                
            else:
                ball.color(arrayColors[cont])
                paddle_a.color(arrayColors[cont])
                paddle_b.color(arrayColors[cont])
            cont+=1
        if ball.xcor()<float(details_dict["pos_pad_a"])+5 and (ball.ycor()>paddle_a.ycor()-40 and ball.ycor()<paddle_a.ycor()+40):
            winsound.PlaySound(soundPathBorder, winsound.SND_ASYNC)
            if cont==len(arrayColors):
                cont=0
                ball.color(arrayColors[cont])
                paddle_a.color(arrayColors[cont])
                paddle_b.color(arrayColors[cont])
                
            else:
                ball.color(arrayColors[cont])
                paddle_a.color(arrayColors[cont])
                paddle_b.color(arrayColors[cont])
            cont+=1
            ball.dx*=-1
            ball.dx*=1.1
            ball.dy*=1.1
            

    #winner

    if score_a==5:
        score.clear()
        ball.color("black")
        paddle_a.color("black")
        paddle_b.color("black")
        score.goto(0,0)
        score.write("Player A Wins!", align="center", font=("Courier",32,"normal"))
        showon=False
        

    if score_b==5:
        score.clear()
        ball.color("black")
        paddle_a.color("black")
        paddle_b.color("black")
        score.goto(0,0)
        score.write("Player B Wins!", align="center", font=("Courier",32,"normal"))
        showon=False
    
