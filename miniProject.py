#guess the number

import random

target=random.randint(1,100)
count=0
while(True):
    num=input("enter any number between 1 to 100 OR QUIT (Q):")
    
    if(num.isdigit()):
        num=int(num)
        if(num==target):
            print("congoo!! you guess the right number ")
            count+=1
            print(f"you guessed the number in {count} {'try' if count == 1 else 'tries'}")
            print("---------- SUCCESS --------")
            print("--------- GAME OVER ---------")
            break

        elif(num>target and num<=100):
            print("your number was too BIG.......\nplease guess a LESSER number...")
            count+=1

        elif(num<target and num>=1):
            print("your number was too SHORT.....\nplease guess a BIGGER number.....")
            count+=1

        else:
            print("your are guessing in wrong direction range is (1 to 100)")
            count+=1

    elif(num=="Q" or "q"):
        print("---------   EXIT  ---------")
        break
    else:
        print("invalid choice")