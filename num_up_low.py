# program calculates number of uppercase and lower case letters in a statement

def num_upper_lower(phrase):
	my_dict = {"lower":0, "upper":0}

	for char in phrase:
		if char.islower():
			my_dict["lower"]+=1

		elif char.isupper():
			my_dict["upper"]+=1

		else:
			pass

	print "Original string is: ", phrase
	print "Number of lower case letters: " , my_dict["lower"]
	print "Number of upper case letters: " , my_dict["upper"]

num_upper_lower("This Is an Important StateMent")