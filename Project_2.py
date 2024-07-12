from tkinter import *
from tkinter import ttk

def button_click(symbol):
    current_value = var1.get()# Get the current value from var1
    if symbol == "=":
        i = eval(current_value)
        """ THIS IS AN VERY IMPORTANT FUNCTION SINCE IT CAN CALCULATE THE EXPRESSION VALUE 
            EVER IF THEY ARE STRING"""
        var1.set(i)
        "NOW WE ARE JUST UPDATING THE VALUE IN THE SCREEN "
    elif symbol == "DEL":
        var1.set(current_value[:-1])
        """ AS YOU CAN SEE THAT current_value IS A STRING AND WHEN WE CLICK 'DEL' THEN WHEN
            WE SET THE STRING TILL THE SECONDLAST CHARACTER THEN IT PRINT IT AGAIN THAT MEANS
            IT WILL DELETE THE LAST CHARACTER.  AND IT WILL HAPPEN AGAIN AND AGAIN TILL YOU 
            CLICK THE DELETE THE LAST CHARACTER TILL THE STRING BECOME ""      """
    elif symbol == "C":
        var1.set("")
        """ THIS IS JUST A CLEAR BUTTON WHICH WILL CLEAR THE SCREEN """
    elif symbol == "√":
        y = int(current_value)
        var1.set(y**0.5)
    elif symbol == "^2":
        y = int(current_value)
        var1.set(y*y)
    else:
        var1.set(current_value + symbol)
window = Tk()
window.title("Calculator")
window.config(bg="yellow")

system_width = window.winfo_screenwidth()
system_height = window.winfo_screenheight()
height = 525
width = 630
c_x = int((system_width - width) / 2)
c_y = int((system_height - height) / 2)

window.geometry(f"{width}x{height}+{c_x}+{c_y}")
window.resizable(False, False)

var1 = StringVar()
var1.set("") 

main_frame = Frame(window,height=525,width=630,bg="green")
main_frame.place(x=0,y=0)

main_screen = Entry(main_frame,bg="white",relief='solid',borderwidth=5,textvariable=var1
                    ,font=("arial",50,"bold"),justify='right')
main_screen.place(x=0,y=0,width=630,height=100)

frame_1 = Frame(main_frame,width=370,height=400,bg="black")
frame_1.place(x=0,y=100)


button_texts_list = [
    "DEL","  √  "," ^2 ","  C  ",
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    "0", ".", "=", "+",
]

for i in range(5):  # Loop through rows
    for j in range(4):  # Loop through columns
        index = i * 4 + j
        button_text = button_texts_list[index]
        button = Button(frame_1, text=button_text, padx=35, pady=11,font=("Arial",30,"bold"),
        command = lambda symbol = button_text : button_click(symbol.strip()))
        button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew") 

window.mainloop()