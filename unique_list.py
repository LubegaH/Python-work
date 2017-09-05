# program turns a list with repeated elements to unique list

'''def uni_list(l):
	my_new_list = set(l)
	print my_new_list

uni_list([1,1,1,1,2,3,3,3,4,5,6,6,6,7])'''


def uni_list(l):
	my_new_list = []

	for k in l:
		if k not in my_new_list:
			my_new_list.append(k)

	print my_new_list

	
uni_list([1,1,1,1,2,3,3,3,4,5,6,6,6,7])
