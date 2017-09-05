# Fuctions and methods homework from the Python boot camp class
# Function computes volume of sphere given its radius

from math import pi,pow

# Volume of sphere = 4/3pir3
def vol(rad):
	v = (4.0/3)*pi*pow(rad,3)
	print v

vol(65.2)