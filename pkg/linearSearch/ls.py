def linear_search(l,key):
	for value in l:
		if key == value:
			return True
	else:
		return False
		
l = [10,20,30,40,50,60]
key = 4
result =  linear_search(l,key)
print(result)
