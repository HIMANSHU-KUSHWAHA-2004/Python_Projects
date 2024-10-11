year = int(input("Enter the year : "))
if year % 100 == 0:
    if year % 400 ==0:
        print(year,"is the leap year")
    else:
        print(year,"is not the leap year")   
    """---->HERE WE USED DIFFERET LOGIC FOR THE CENTURIES YEAR FIRST WE DIVIDE IT WITH 100 TO 
        KNEW THAT THE YEAR IS THE CENTURY AFTER KNOWING THAT THE YEAR IS CENTURY YEAR THEN WE 
        DIVIDE IT 400 TO ENSURE THAT WHEATHER THE YEAR IS A LEAP YEAR OR NOT 
        ---> WE DID ALL THIS DUE TO CENTURIES YEARS BECAUSE FROM OUR LOGIC OF DIVIDING THE YEAR
        FROM 4 .LEAD EVERY CENTURY YEAR IS A LEAP YEAR BUT THATS NOT ACTUALLY TRUE
        --->LIKE YEAR 3000 IS NOT A LEAP YEAR BUT OF YOU DIVIDE IT FROM 4 IT GIVE REMENDER 0 """ 
else:    
    if year % 4 == 0:
        print(year,"is the leap year")
    else:
        print(year,"is not the leap year")       