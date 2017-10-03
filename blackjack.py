# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import random

# boolean used to know if hand is in play
playing = False

chip_pool = 200 # Explore on how to make a raw input
bet = 1
restart_phrase = "Press 'D' to deal the cards again, or 'Q' to quit"

# The suits - Hearts, Diamonds, Clubs and Spades
suits = ('H','D','C','S')

# Possible card rank
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Point Values dict (Aces can be 1 or 11, check self.ace for details)
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# The Card class
class Card(object):
 	
	def __init__(self, suit, rank):
		self.suit = suit
 		self.rank = rank

 	def __str__(self):
 		return self.suit + self.rank

 	def grab_suit(self):
 		return self.suit

 	def grab_rank(self):
 		return self.rank

 	def draw(self):
 		print(self.suit + self.rank)


# The hand class

class Hand(object):
	def __init__(self):
		self.cards = []
		self.value = 0
		# define aces here since it can be 1 or 11
		self.ace = False


	def __str__(self):
		'''Return a string of the current hand composition'''
		hand_composition = ""

		# try using another way to do this, may be list comprehension
		for card in self.cards:
			card_name = card.__str__()
			hand_composition += " " + card_name

		return 'The hand has %s' %hand_composition


	def card_add(self, card):
		'''Adds another card to the hand'''
		self.cards.append(card)
		# check for aces
		if card.rank == 'A':
			self.ace = True
		self.value += card_val[card.rank]


	def calculate_value(self):
		'''Calculates the value of the hand and makes Aces 11 if it does not burst the hand'''
		if (self.ace == True and self.value < 12):
			return self.value + 10

		else:
			return self.value


	def draw(self, hidden):
		if hidden == True and playing == False:
			# dont show first hidden card
			first_card = 1
		else:
			first_card = 0

		for i in range(first_card, len(self.cards)):
			self.cards[i].draw()



class Deck(object):
	def __init__(self):
		# creates the deck in order
		self.deck = []
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit, rank))

	def shuffle(self):
		# use shuffle method that exists within python in the random lib
		random.shuffle(self.deck)

	def deal(self):
		# Grab first item in the deck
		single_card = self.deck.pop()
		return single_card

	def __str__(self):
		deck_composition = ""
		for card in self.cards:
			deck_compostion += " " + deck_composition.__str__()

		return "The deck has " + deck_composition

# First bet
def make_bet():
	# asks player for the bet amount
	global bet
	bet = 0
	print "Please place your bet. (Enter a whole integer)"

	while bet == 0:
		bet_comp = int(raw_input())
		# checking to make sure bet is within remaining amount of chips
		if bet_comp >= 1 and bet_comp <= chip_pool:
			bet = bet_comp
		else:
			print "You don't have enough chips to bet, you only have " + str(chip_pool) + " remaining"


# Setting up the game and dealing out the cards
def deal_cards():
	# global variables
	global result, playing, deck, pHand, dHand, chip_pool, bet


	# creates deck from the Deck() class
	deck = Deck()

	#Shuffle the deck
	deck.shuffle()

	# make the desired bet
	make_bet()

	# setup both player hands
	pHand = Hand()
	dHand = Hand()

	# deal out initial cards
	pHand.card_add(deck.deal())
	pHand.card_add(deck.deal())

	dHand.card_add(deck.deal())
	dHand.card_add(deck.deal())

	result = "Hit or Stand? (Press either H or S)"

	if playing == True:
		print "Fold"
		chip_pool -= bet

	# this tells currently playing hand
	playing = True
	game_step()



def hit():
	# implement the hit Button - H
	global playing,chip_pool,deck,player_hand,dealer_hand,result,bet

	# If hand is in play, add card
	if playing:
		if pHand.calculate_value() <= 21:
			pHand.card_add(deck.deal())

		print "Player hand is %s" %pHand

		if pHand > 21:
			result = 'Busted!! ' + restart_phrase

			chip_pool -= bet
			playing = False

	else:
		result = "Sorry, can't hit " + restart_phrase

	game_step()


# The Stand function: Plays the dealer's hand since the player hit stand
def stand():
	global playing,chip_pool,deck,player_hand,dealer_hand,result,bet

	if playing == False:
		if pHand.calculate_value() > 0:
			result = "Sorry, you can't stand..."

	# have to go through all options for win or bust
	else:
		# soft 17 rule
		while dHand.calculate_value() < 17:
			dHand.card_add(deck.deal())

		# Dealer bursts
		if dHand.calculate_value() > 21:
			result = 'Dealer busts! You win!! ' + restart_phrase
			chip_pool += bet
			playing = False

		# Player has better hand than dealer
		elif dHand.calculate_value() < pHand.calculate_value():
			result = 'You beat the dealer, You win! ' + restart_phrase
			chip_pool += bet
			playing = False
	
		# Push
		elif dHand.calculate_value() == pHand.calculate_value():
			result = 'Tied up, push ' + restart_phrase
			playing = False

		# dealer wins
		else:
			result = 'Dealer WINS! ' + restart_phrase
			chip_pool -= bet
			playing = False

	game_step()


# Function to print results and ask user for next step
def game_step():
	# Display player hand
	print ""
	print('Your hand is: '),
	pHand.draw(hidden =False)
	print "Your hand total is: " + str(pHand.calculate_value())

	# display dealer hand
	print("Dealer hand is: "),
	dHand.draw(hidden=True)

	# if game round is over
	if playing == False:
		print "--- for a total of " + str(dHand.calculate_value())
		print "Chip total: " + str(chip_pool)
	# otherwise dont know the second card yet
	else:
		print "with another card hidden upside down"
	# print result of hit or stand
	print result
	player_input()

# Exiting game
def game_exit():
	print "Thanks for playing"
	exit()

# Reading user input, convert to lowercase
def player_input():
	player_in = raw_input()

	if player_in == 'H':
		hit()
	elif player_in == 'S':
		stand()
	elif player_in == 'D':
		deal_cards()
	elif player_in == 'Q':
		game_exit()
	else:
		print "Invalid input, please enter H, S, D or Q:"
		player_input()

	# Quick intro to the game
def intro():
	print "This is the black jackgame or popularly known as 21"

'''Running the game'''
# Create deck
deck = Deck()

# shuffle the deck
deck.shuffle()

# Create player and dealer hands
pHand = Hand()
dHand = Hand()

# Intro
intro()

# Deal out cards and start game
deal_cards()


























