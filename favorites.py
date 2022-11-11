1.
cookies = int(input("how many cookies do you have?"))
if cookies <3:
    print("you don't have enough cookies")
elif cookies <10:
    print("you have good amount")
else:
    print("you have too many")
2.
side = input("are you a jedi master or sith lord?")
if side == 'jedi':
    print("you get a green light saber")
elif side == 'sith':
    print("you get a red light saber")
else:
    print("you get breadstick")
3.
print("loop #1:")
for i in range(4, 41, 2):
    print(i, end =" ")
4.
i = 100
while i > 50:
    print(i)
    i -= 10
5.
quit=False
while quit == False:
    choice=input("knock knock, who's there banana")
    if choice == 'orange':
        print("yes")
    else:
        print("no")
        quit=True
        
print("orange you glad I didn't say banana")
6.
def multiple (x,y,z):
    if x<y<z:
        return x*y*z
    else:
        return x/y/z
print(multiple(2,3,4))
7.
I think it's better if I try this one again next friday, sorry


Midterm retakes retake:
4.
num = 20
while num <= 60:
    print(num, end = " ")
    num += 2
    
print()
for i in range (20,62,2):
    print (i, end = " ")
5.
doExist = False
while doExist == False:
    password = input("enter password")
    if password == "12345":
        doExist = True
        print("accepted")
    else:
        print("not accepted")
6.
def  mathy(a, b, c, d):
    return a+b-c+d

print(mathy(10, 20, 30, 40))
7.
def garden(p):
    print("your pumpkins are growing")
    num = 1
    while num <= p:
        print("now you have", num, "pumpkins")
        num+=1
        
seeds = int(input("enter number of seeds planted"))
garden(seeds)
Midterm retake retake retake:
5.
doExist = False
while doExist == False:
    password = input("ring ring")
    if password == "hello?":
        doExist = True
        print("we've been trying to reach you over your car's extented warranty")
    else:
        print("ring ring")
6.
def mathy(x,y):
    return x % y

print(mathy(8,3))
7.

