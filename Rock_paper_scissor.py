import random 
from PRACTICE.art import logo
def working(user,computer):
    if user == "r" and computer == "p":
        print(f"Computer choice : {computer}")
        return False
    elif  user == "r" and computer == "s":
        print(f"Computer choice : {computer}")
        return True
    elif  user == "p" and computer == "s":
        print(f"Computer choice : {computer}")
        return False
    elif  user == "p" and computer == "r":
        print(f"Computer choice : {computer}")
        return True
    elif  user == "s" and computer == "p":
        print(f"Computer choice : {computer}")
        return True
    elif  user == "s" and computer == "r":
        print(f"Computer choice : {computer}")
        return False
def main():
    print(logo())
    print("___________________________________Welcome to the Rock, Paper, Scissors game!____________________________\n")
    print("For each win you will get 10 points")
    print("Choose r for rock , p for paper , s for scissor\n")
    points = 0
    while True:
        user = input("Enter your choice: ").lower()
        if user not in ["r", "p", "s"]:
            print("Invalid choice. Please enter r, p or s.")
            continue
        else:
            computer = random.choice(["r","s","p"])
            if user == computer:
                    print("It's a tie!\n")
            else:
                user_win = working(user,computer)
                if user_win == True:
                    print("You win!\n")
                    points += 10
                elif user_win == False:
                    print("Computer wins!\n")
                    break
    print("Your points: ", points)
    print("Thanks for playing")
if __name__ == "__main__":
    main()
