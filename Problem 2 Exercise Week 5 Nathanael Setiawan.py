import random
n = random.randint(-1000,1000)
Multiply = lambda a : a * n
print(Multiply(int(input("Input number to be multiplied by a random number:"))))
print("The random number is: " + str(n))