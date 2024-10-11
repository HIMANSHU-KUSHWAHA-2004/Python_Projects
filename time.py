import time
import os
timenow = time.strftime("%H - %M - %S")
timehour = int(time.strftime("%H"))
"""this time.strftime is use to tell the time and this will return a string so you have to  
convert the string to the integer as I do"""
print(timenow)
if (0<timehour<12):
    print("GOOD MORNING SIR HOW MAY I HELP YOU")
elif(12<=timehour<17):    
    print("GOOD AFTERNOON SIR HOW MAY I HELP YOU")
elif(17<timehour<24):
    print("GOOD NIGHT SIR HAVE A NICE SLEEP ")
