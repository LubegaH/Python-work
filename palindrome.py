# Checks whether word is a plaindrome or not

def ispalindrome(phrase):

	statement = phrase.replace(' ','')
	if statement == phrase[::-1]:
		print "Qualifies as palindrome"

	else:
		print "Phrase isn't a palindrome"

ispalindrome("Ham")