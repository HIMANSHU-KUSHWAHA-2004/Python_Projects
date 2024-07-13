quetions = [ ["Which cricketer has won the most number of IPL titles?",
"A Gautam Gambhir", "B Virat Kohli" , "C Rohit Sharma","D MS Dhoni","C Rohit Sharma"
],
["Which team won the inaugural IPL in 2008?","A) Rajasthan Royals", "B) Chennai Super Kings"
,"C) Kolkata Knight Riders" ," D) Mumbai Indians","A) Rajasthan Royals"],

["Who is the leading wicket-taker in the Indian Premier League (IPL)?","A) Lasith Malinga",
"B) Sohail Tanveer", "C) Harbhajan Singh", "D) Yuvraj Singh" ,"A) Lasith Malinga"],

["Who is the highest run-scorer in the IPL? ","A) Rohit Sharma","B) Virat Kohli" ,
"C) Suresh Raina","D) Chris Gayle","B) Virat Kohli"],

["Which team has finished the league stage in 2nd position every time they have won the IPL?",
"A) Chennai Super Kings" ,"B) Kolkata Knight Riders","C) Mumbai Indians", 
"D) Rajasthan Royals" ,"A) Mumbai Indians"]
]
"""# Creating a list of lists
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accessing elements in the nested list
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][2])  # Output: 6
print(nested_list[2][1])  # Output: 8"""
answer = [3,1,1,2,3]
summ = 0
level = [1000000,2000000,3000000,5000000,10000000]
for i in range(0,len(quetions)):
    print(f"Question for the amount {level[i]} ")
    print(f"{i})Question {quetions[i][0]}")
    print(f" 1 {quetions[i][1]}               2 {quetions[i][2]}")
    print(f" 3 {quetions[i][3]}               4 {quetions[i][4]}")
    choose = int(input("ENTER THE ANSWER (1 - 4) : ")) 
    print()
    if choose == answer[i]:
        print("Correct answer")
        summ += level[i]
        print(f"YOU WIN Rs. {summ}")
        print()
        if i == 3 :
            quit = input("DO YOU WANNA QUIT : Y/N : ")
        if quit == "y" or "Y":
            print(F"YOU QUIT THE GAME WITH THE AMOUNT : {summ}")
            break
    else:
        print("Wrong answer")
        break    