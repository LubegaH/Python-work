#!/usr/local/bin/python
# coding: latin-1

# Designed in python 2.7 for Mac
# V 1.0
'''Use Keyboard left and right to turn those directions respectively.
Use Arrow Key up to increase speed
Use arrow key down to reduce speed
Use space bar to fire missile'''

import os
import random
import turtle
import time


turtle.fd(0)
# Animation speed set to max
turtle.title("Galaxy Wars")
turtle.speed(0)
# Background image
turtle.bgpic("bg_.gif")
turtle.bgcolor("black")
# Hide default turtle
turtle.ht()
# Save memory
turtle.setundobuffer(1)
turtle.tracer(0)

# Registering the shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("friendly.gif")
turtle.register_shape("bullet.gif")


# setting up a class for sprites
class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1

	def move(self):
		self.fd(self.speed)

		# Boundary checks and resets
		if self.xcor() > 290:
			self.setx(290)
			self.rt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.rt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.rt(60)

	def isCollision(self, other):
		if (self.xcor() >= (other.xcor() - 15)) and \
		(self.xcor() <= (other.xcor() + 15)) and \
		(self.ycor() >= (other.ycor() - 15)) and \
		(self.ycor() <= (other.ycor() + 15)):
			return True
		else:
			return False

# Player class
class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
		self.speed = 2
		self.lives = 3

	def turn_left(self):
		self.lt(45)

	def turn_right(self):
		self.rt(45)

	def accelerate(self):
		self.speed += 0.5

	def decelarate(self):
		self.speed -= 0.5

# Enemy class
class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 6
		self.setheading(random.randint(0, 360))

# Friend class
class Friend(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 8
		self.setheading(random.randint(0, 360))

	def move(self):
		self.fd(self.speed)

		# Boundary checks and resets
		if self.xcor() > 290:
			self.setx(290)
			self.lt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.lt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.lt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.lt(60)

# Payload class - Missile
class Payload(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid = 0.3, stretch_len = 0.5, outline=None)
		self.speed = 25
		self.status = "loaded"
		self.goto(-1000,1000)

		

	def fire(self):
		if self.status == "loaded":
			# play payload sound
			os.system("afplay laser.mp3&")
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.status = "fired"

	def move(self):
		if self.status == "loaded":
			self.goto(-1000,1000)

		if self.status == "fired":
			self.fd(self.speed)

		# Checking if missile hit the border
		if self.xcor() < -290 or self.xcor() > 290 or \
			self.ycor() < -290 or self.ycor() >290:
			self.goto(-1000, 1000)
			self.status = "loaded"

# Particle system
class Particles(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
		self.goto(-1000,-1000)
		self.frame = 0

	def explode(self, startx, starty):
		self.goto(startx, starty)
		self.setheading(random.randint(0, 360))
		self.frame = 1

	def move(self):
		if self.frame > 0:
			self.fd(10)
			self.frame += 1

		if self.frame > 15:
			self.frame = 0
			self.goto(-1000, 1000)

# Game info class. Keeps track of important events in the game like lives, state etc
class Game_info():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "playing"
		self.lives = 3
		self.pen = turtle.Turtle()

	def draw_border(self):
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300,300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()
		self.pen.pendown()

	def show_status(self):
		self.pen.undo()
		player_score = "Score: %s" %(self.score)
		self.pen.penup()
		self.pen.goto(-300, 310)
		self.pen.write(player_score, font = ("Arial", 16, "normal"))

# Game_info object
game = Game_info()

# Draw border
game.draw_border()
game.show_status()


# Initializing sprites
player = Player("triangle", "white", 0, 0)
payload = Payload("bullet.gif", "yellow", 0, 0)
# friend = Friend("circle", "blue", 100, 100)
# Creating multiple friends
friends = []
for k in range(3):
	friends.append(Friend("friendly.gif", "blue", 100, 100))
# Creating a single enemy
# enemy = Enemy("triangle", "red", 220, 220)

# Creating multiple enemies
enemies = []
for i in range(8):
	enemies.append(Enemy("enemy.gif", "red", 220, 220))

# Creating the particles
particles = []
for i in range(20):
	particles.append(Particles("circle", "orange", 0, 0))


# Keyboard bindings
def keyboard_bindings():
	turtle.listen()
	turtle.onkey(player.turn_left, "Left")
	turtle.onkey(player.turn_right, "Right")
	turtle.onkey(player.accelerate, "Up")
	turtle.onkey(player.decelarate, "Down")
	turtle.onkey(payload.fire, "space")
keyboard_bindings()



# Main game loop
while True:
	# Moving the sprites
	player.move()
	payload.move()

	for friend in friends:
		friend.move()

		# check for collision with friend
		if player.isCollision(friend):
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			friend.goto(x, y)
			game.score -= 10
			game.show_status()

		# check for friend destruction by payload
		if payload.isCollision(friend):
			os.system("afplay explosion.mp3&")
			for particle in particles:
				particle.explode(payload.xcor(), payload.ycor())
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			friend.goto(x, y)
			payload.status = "loaded"
			# Update game score
			game.score -= 10
			game.show_status()


	for enemy in enemies:
		enemy.move()

		# check for collision between enemy and player
		if player.isCollision(enemy):
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			enemy.goto(x, y)
			game.score -= 10
			game.show_status()

		# check for enemy destruction by payload
		if payload.isCollision(enemy):
			# play explosion sound
			os.system("afplay explosion.mp3&")
			for particle in particles:
				particle.explode(payload.xcor(), payload.ycor())
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			enemy.goto(x, y)
			payload.status = "loaded"
			# update game score
			game.score += 10
			game.show_status()
			

	for particle in particles:
		particle.move()

	turtle.update()
	time.sleep(0.02)
	

	

	

	






delay = raw_input("Press Enter to finish...")