import random
flag = 0
i=1
random_number = random.randint(0,100)
print("WELCOME TO THE NUMEBR GUESSING GAME ")
play = input("DO YOU READY TO PLAY y/n : ")
if(play.lower() == "y"):
        while flag!= 1:
            answer = int(input("ENTER THE NUMBER BETWEEN 0 TO 100 : "))
            if (answer>random_number):
                print("THE NUMBER IS TOO HIGH")
                print("TRY AGAIN")
            elif (answer<random_number):
                print("THE ANSWER IS TOO LOW") 
                print("TRY AGAIN")
            else:
                print("NICE!! YOU HAVE WON THE GAME")
                print("~~~~YOU HAVE CLEAR THE GAME IN THE",i,"CHANCES~~~~")
                break
            i+=1
else:
        print("OKIE BYEE WE MAY PLAY NEXT TIME")
