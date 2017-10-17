#!/usr/local/bin/python
# coding: latin-1

import turtle
import os
import math
import random



player_speed = 20
enemy_speed = 2
score = 0
bullet_speed = 20
# bullet should only be fired if bullet state loaded
bullet_state = "loaded"

# screen setup
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("bg_.gif")

# register shapes to use
turtle.register_shape("hero_ship.gif")
turtle.register_shape("enemy2.gif")
turtle.register_shape("bullet.gif")

# Draw border
def border():
	border_pen = turtle.Turtle()
	border_pen.speed(0)
	border_pen.color("white")
	border_pen.penup()
	border_pen.setposition(-300,-300)
	border_pen.pendown()
	border_pen.hideturtle()
	border_pen.pensize(3)
	for side in range(4):
		border_pen.fd(600)
		border_pen.lt(90)
border()

# drawing the score on the board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_reading = "Score: %s" %score
score_pen.write(score_reading, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("hero_ship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Creating an enemy
enemies = []
for i in range(5):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("enemy2.gif")
	enemy.penup()
	enemy.speed(0)
	x_pos = random.randint(-200,200)
	y_pos = random.randint(100,250)
	enemy.setposition(-x_pos, y_pos)

# creating the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.setheading(90)
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# defining bullet actions
def fire():
	# declare bullet_state as global variabel so it can change state
	global bullet_state
	if bullet_state == "loaded":
		bullet_state = "fired"
		# set position of the bullet to position of the player
		x = player.xcor()
		y = player.ycor()
		bullet.setposition(x, y+5)
		bullet.showturtle()

# destroying the enemy, by determining if a collision has happened
# used pythogoras theorem to determine distance between two objects
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
	if distance < 15:
		return True
	else:
		return False


# Moving the player left and right
def move_left():
	x = player.xcor()
	x -= player_speed
	# making sure x does not go over the boundary
	if x < -290:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += player_speed
	if x > 280:
		x = 280
	player.setx(x)


# Create keyboard bindings
def keyboard_bindings():
	turtle.listen()
	turtle.onkey(move_left, "Left")
	turtle.onkey(move_right, "Right")
	turtle.onkey(fire, "space")

keyboard_bindings()



# main game loop
while True:
	for enemy in enemies:
		# move enemy
		x = enemy.xcor()
		x += enemy_speed
		enemy.setx(x)

		# moving the enemy back and forth and down
		if enemy.xcor() > 280:
			# move all enemies down
			for k in enemies:
				y = k.ycor()
				y -= 30
				k.sety(y)
			# Change enemy direction
			enemy_speed *= -1
			

		if enemy.xcor() < -280:
			# move all enemies down
			for k in enemies:
				y = k.ycor()
				y -= 30	
				k.sety(y)
			# change enemy direction
			enemy_speed *= -1


		if isCollision(bullet, enemy):
				# Reset bullet
				bullet.hideturtle()
				bullet_state = "loaded"
				# take bullet off screen so other enemies dont run into it
				bullet.setposition(0, -400)
				x_pos = random.randint(-200,200)
				y_pos = random.randint(100,250)
				enemy.setposition(-x_pos, y_pos)

				# update score
				score += 10
				score_string = "Score %s" %score
				score_pen.clear()
				score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

			# Game over state
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print "Enemy got to the home base"
			break

	# moving the bullet 
	# Avoid wasting memory, only move the bullet when fired
	if bullet_state == "fired":
		y_bu = bullet.ycor()
		y_bu += bullet_speed
		bullet.sety(y_bu)

	# check to see if bullet has reached the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bullet_state = "loaded"

	# check for collision - this destroys enemy
	





delay = raw_input("Press enter to finish...")