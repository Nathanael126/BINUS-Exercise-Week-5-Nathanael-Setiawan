a = 0
b = 0
c = 0
x = 0
Fibbonachi = lambda a,b : a+b
loop = int(input("How much units?:"))
while x < loop:
    if(x == 1):
        b += 1
    elif(x == 2):
        print("1")
    else:
        c = Fibbonachi(a,b)
        print(c)
        a = b
        b = c
    x += 1