import random
a = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
SortTuple = lambda a : sorted(a)
print("Original Tuple: "+str(a))
print("Edited Tuple: "+str(SortTuple(a)))