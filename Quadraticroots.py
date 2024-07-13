import math
print("The General quadratic equation is ax*2 + bx   + c = 0.//")
a = float(input("Enter the cofficient of  x^2 : "))
b = float(input("Enter the cofficient of  x    : "))
c = float(input("Enter the constant  term      : "))
dis = b*b - 4*a*c
if dis>0 :
    print("Roots are distinct and real\n")
    root1 = (-b + math.sqrt(dis))/2*a
    root2 = (-b - math.sqrt(dis))/2*a
    """HERE FOR USING THE SQRT FUNCTION YOU HAVE TO IMPORT MATH MODULE AT THE TOP OF THE CODE"""

elif dis==0:
    print("Both Roots are equal ")
    print("Root1 = Root2 = ",-b/2*a)

else:    
    print("Roots are complex and conjugate of each other\n")
    root_real = -b/2*a
    root_img = (math.sqrt(abs(dis)))/2*a
    """HERE WE abs FUNCITON WHICH TELL THE ABSOLUTE VALUE OF THE NUMBER FROM THE NUMBER LINE
    THAT DISTANCE FROM THE 0 EXAMPLE ads(-3) = 3 , abs(3) = 3 YOU CAN THINK ITS LIKE A MODULUS"""
    print("Root1 =",root_real," + ",root_img,"i","Root2 = ",root_real," - ",root_img,"i")
    
    
