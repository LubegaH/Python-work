# Generates fibonacci sequence up to user input number

"""
def fibona():
	n = int(raw_input("Enter a number: "))
	a = 1
	b = 1
	out = []
	for i in range(n):
		out.append(a)
		a, b = b, a+b

	print out

fibona()"""

# explore option of using yield
# need to understand generators better
def genfibona(n):
	n = int(raw_input("Enter a number: "))
	a = 1
	b = 1
	for i in range(n):
		yield a
		a, b = b, a+b


for k in genfibona(3):
	print k


