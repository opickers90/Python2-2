def is_int(x):
	if x % 1 == 0:
		return True
	else:
		return False
  
print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True  
