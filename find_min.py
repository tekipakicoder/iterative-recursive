#!/usr/bin/env python3


#Iterable version
def find_min(my_list):
	min = None
	for element in my_list:
		if not min or (element < min):
			min = element
	return min

find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5


#Recursive version

def find_minR(my_list, min=None):
	if len(my_list) == 0:
		return min
	else:
		if not min or my_list[0] < min:
			min = my_list[0]
		print(my_list)

		return find_minR(my_list[1:], min)


print(find_minR([42, 17, 2, -1, 67]))
# -1
#find_mindR([])
# None
print(find_minR([13, 72, 19, 5, 86]))
# 5


