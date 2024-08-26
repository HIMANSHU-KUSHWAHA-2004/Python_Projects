import tictactoe_logo 

def sum(a,b,c):
    return a+b+c
def printboard(xstate,zstate):
    
    """THIS STEP NEED UNDERSTANDING AS WE CAN SEE THAT WE RECIEVE TWO LIST IN IT THAT IS xstate
    AND zstate IN THE FIRST TIME WHEN FUNCTION IS CALL IT PRINT ALL THE NUMBER 1 TO 9 BECAUSE IT
    RECIEVE ALL INDEX VALUE EQUAL TO ZERO WHICH IS A FALSE SO THE FALSE STATEMENT IS PRINT THAT 
    IS PRINTING ALL THE NUMBER
    2) AFTER THAT """
    
    zer = 'X' if xstate[1] else ( '0' if zstate[1] else 1)
    one = 'X' if xstate[2] else ( '0' if zstate[2] else 2)
    two = 'X' if xstate[3] else ( '0' if zstate[3] else 3)  
    the = 'X' if xstate[4] else ( '0' if zstate[4] else 4)
    fou = 'X' if xstate[5] else ( '0' if zstate[5] else 5)
    fiv = 'X' if xstate[6] else ( '0' if zstate[6] else 6)
    six = 'X' if xstate[7] else ( '0' if zstate[7] else 7)
    sev = 'X' if xstate[8] else ( '0' if zstate[8] else 8)
    eig = 'X' if xstate[9] else ( '0' if zstate[9] else 9)
    print(f"     |     |     ")
    print(F"  {zer}  |  {one}  |  {two}  ")
    print(F"_____|_____|_____")
    print(F"     |     |     ")
    print(F"  {the}  |  {fou}  |  {fiv}  ")
    print(F"_____|_____|_____")
    print(F"     |     |     ")
    print(F"  {six}  |  {sev}  |  {eig}  ")
    print(f"     |     |     \n")
    
    """value_if_true  if  condition  else  value_if_false
    IN PYTHON THE CONDITION IS IN THE CENTER IF THE CONDITION IS TRUE THEN IT WILL RESULT IN
    THE VALUE ON THE LEFT SIDE OF THE CONDITION AND IF THE CONDITION IS FALSE THEN IT WILL RESULTF0
    """
    
def duplicate(xstate,zstate,value):
    if zstate[value] == xstate[value]:
        print("THE VALUE IS ALREADY TAKEN")
        return True
    
    
def checkwin(list_x,list_0):
    wins_chances = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in wins_chances:
        #THIS LOOP WILL GO UPTO 8 SINCE THERE ARE SMALL 8 SUBLIST IS THERE IN THE win_chance 
        if (sum(list_x[win[0]],list_x[win[1]],list_x[win[2]]) == 3):
            print("THE WINNER IS X")
            return 1
        if (sum(list_0[win[0]],list_0[win[1]],list_0[win[2]]) == 3):
            print("THE WINNER IS 0")            
            return 0
        
    return -1
        
        
def main():
    print(tictactoe_logo.logo())
    xstate = [0,0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0,0]
    print("Welcome to the TIC TAC TOE game\n")
    turn = 1
    while (True):
        printboard(xstate,zstate)
        if turn == 1:
            cwin = checkwin(xstate,zstate)
            if cwin != -1:
                print("Match Over")
                break
            print("ITS 'X' TURN NOW : ")
            value = int(input("Please Enter the value : "))
            print()
            xstate[value] = 1
            if duplicate(xstate,zstate,value) == True:
                continue
            # print(xstate)
            # print(zstate)
            """THESE BOTH STATEMENT WILL TELL THE UDATES OF BOTH LIST YOU CAN OBSERVE AT EACH
            STEP HOW THIS ALL WORKS WHEN THERE IS X TURN SO THE VALUE OF xstate IS UPDATED THEN
            PASS INTO THE FUNCTION WHICH PRINT THEM ON THE BOARD SINCE THE ANY NUMBER (OUR CASE
            IS 1) RETURNS TRUE """
        else:
            cwin = checkwin(xstate,zstate)
            if cwin != -1:
                break
            print("ITS 'O' TURN NOW : ")
            value = int(input("Please Enter the value : "))
            print()
            zstate[value] = 1
            if duplicate(xstate,zstate,value) == True:
                continue
            # print(xstate)
            # print(zstate)
        turn = 1 - turn

if __name__ == "__main__":
    main()