my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

def filter_by_three(x):
  for num in x:
    return num
  
print filter_by_three(my_list)
