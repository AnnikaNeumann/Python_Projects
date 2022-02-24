# Turtle Game using the package 'turtle'

# import relevant modules
import turtle
import random
import time

# Setting up a nice screen for the game

screen = turtle.Screen()
screen.bgcolor('lightgrey') #background color

# 2 players in the game and idea is that whoever gets to other side wins

#player 1
player_one = turtle.Turtle()
player_one.color('green')
player_one.shape('turtle')

#player 2
player_two = player_one.clone()
player_two.color('red')

# Let's postion the players
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

#draw a finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish', font=24)

#let player one return to start position
player_one.penup()
player_one.color('green')
player_one.goto(-300, 200)
player_one.right(90)

#have players pens down
player_one.pendown()
player_two.pendown()

#let's create values for the die
die = [1, 2, 3, 4, 5, 6]

#let's create the game
for i in range(30):
    if player_one.pos() >= (300, 250):
        print("Player One wins the race!")
        break
    elif player_two.pos() >= (300, -250):
        print("Player Two wins the race!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(10*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        time.sleep(1)
        player_two.forward(10*die_roll2)


#this keeps the turtle drawing on the screen
#turtle.done()