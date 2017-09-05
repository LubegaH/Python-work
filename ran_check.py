# program checks if a number is in a given range

def ran_check(num,low,high):
	if num in range(low,high+1):
		print "%s is in the range" %str(num)
	else:
		print "%s is out of range" %str(num)

ran_check(21,1,20)

"""
def ran_bool(num,low,high):
	bool_value = num in range(low,high)
	print bool_value


ran_bool(21,1,20)
"""