# Multiplies all numbers numbers in a list

def multiply_list(l):
	total = 1

	for x in l:
		total*=x

	print total

multiply_list([2.3,1,4,2])