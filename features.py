def function(x):
	'''When we input an integer inside of this function, we will run it multiple times through a recursive sequence!'''
	if x == 1:
		return 1
	else:
		return x * function(x-1)

y = function(8)

print(y)
