import random
UG = None
guess = 0
C = random.randint(1,100)

print("Random N :"+str(C))
while(UG != C):
    try:
        UG = eval (input("Enter Your Guess :"))
        guess +=1
        if (UG == C):
            print("You Had Guess Right Number :"+str(UG))
        elif (UG>C):
            print("You Guess is Larger Than Number")
        elif (UG<C):
            print("You Guess is Smaller Than Number")
        else:
            print("You Had Guess Wrong Number :")
    except Exception as e:
        print("Error",e)
    
print("Total Guest was:"+str(guess))

f = open('record.txt','r')

data = f.read()

if guess < int(data):
    d = open('record.txt','w+')
    d.write(str(guess))
    print("Your New High Score is :"+str(guess))
else:
    print("High Score is :"+str(data))