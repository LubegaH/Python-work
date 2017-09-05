# Checks for whether statement is a panagram
# A panagram is a statement containing all letters of the alphabet

import string

def ispanagram(phrase, alphabet=string.ascii_lowercase):
	alphabet_set = set(alphabet)

	# compare the two sets for equivalence
	if alphabet_set<=set(phrase.lower()):
		print "Statement is a panagram"

	else:
		print "Statement not a panagram"

ispanagram("The quick brown fox jumps")