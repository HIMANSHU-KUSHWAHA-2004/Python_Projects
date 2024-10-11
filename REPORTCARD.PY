a = input("Enter your name : ")
eng = float(input("Enter your English  marks"))
maths = float(input("Enter Your Mathematics Marks: "))
phy = float(input("Enter Your Physics Marks: "))
chemistry=float(input("Enter Your Chemistry Marks: "))
total = eng + maths + phy + chemistry
percentage = round((total/400)*100,4)
"""HERE AS YOU CAN SEE YOU CAN CONTROL THE DECIMAL PLACES BY USING ROUND FUNCTION IT WILL 
ROUND OF THE NUMBER UP TO THE DIGIT YOU WANT SYNTAX IS round(number,digit) """
if  percentage >=90 and percentage <=100:
    print("Your Percentage is ",percentage ,"Your Grade is A")
elif percentage >=80 and percentage <90:
    print("Your Percentage is ",percentage ,"Your Grade is B")
elif percentage >=70 and percentage <80:
    print("Your Percentage is ",percentage ,"Your Grade is C")
else:
    print("Your Percentage is ",percentage ,"Your Grade is D")
    print(type(percentage))
    