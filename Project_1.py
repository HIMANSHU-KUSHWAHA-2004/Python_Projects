import os
import datetime as dt
from tkinter import *
from tkinter.messagebox import showinfo
    
def calculate():
    student_name = name_1.get()
    roll_number = roll_1.get()
    s1 = subject_1.get()
    s2 = subject_2.get()
    s3 = subject_3.get()
    s4 = subject_4.get()
    s5 = subject_5.get()
    total_marks = (s1+s2+s3+s4+s5)
    percentage = (total_marks/500)*100
    perc.config(text=f"PERCENTAGE - {percentage}")
    
    global div
    if percentage>=80:
        div = "1st div"
    elif percentage<80 and percentage>=60:
        div = "2nd div"
    elif percentage>60 and percentage>=40:
        div = "3rd div"
    else:
        div = "Fail"
        division.config(bg="red")
    division.config(text=f"DIVISION - {div}")
    
    
    "THIS IS FILE APPENDING PART"
    directory = "/home/himanshu/Python.py/Tkinter/Projects"
    filename = "Project_1.txt"
    file_with_path = os.path.join(directory,filename)
    file = open(file_with_path,"a")
    file.write(f"DATE & TIME- {dt.datetime.now()}\n")
    file.write(f"Student Name: {student_name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Subject 1 Marks: {s1}\n")
    file.write(f"Subject 2 Marks: {s2}\n")
    file.write(f"Subject 3 Marks: {s3}\n")
    file.write(f"Subject 4 Marks: {s4}\n")
    file.write(f"Subject 5 Marks: {s5}\n")
    file.write(f"Total Marks: {total_marks}\n")
    file.write(f"Percentage: {percentage:.2f}%\n")
    file.write(f"Division: {div}\n\n")
    file.write(f"\n\n")
    
def notify():
    if div == "Fail":
        showinfo("Result", f"""                         SORRY
                \nYOU ARE FAIL YOU CAN APPEARIN NEXT YEAR
            """)
    else:
        showinfo("Result", f"""         CONGRATULATIONS
                \n YOU ARE PASSED WITH {div} DIVISION """)
    
def function_warpper():
    calculate()
    notify()

def clear_fields():
    name_1.set("")
    roll_1.set(0)
    subject_1.set(0)
    subject_2.set(0)
    subject_3.set(0)
    subject_4.set(0)
    subject_5.set(0)
    perc.config(text="PERCENTAGE  -     ")
    division.config(text="DIVISION    -          ", bg="white")
    
    
window = Tk()
window.title("Result")
window.config(bg="lightgreen")
window.resizable(False,FALSE)

system_width = window.winfo_screenwidth()
system_height = window.winfo_screenheight()
height = 1000
width = 820
c_x = int((system_width - width) / 2)
c_y = int((system_height - height) / 2)

window.geometry(f"{width}x{height}+{c_x}+{c_y}")

Frame_1 = Frame(window, height=600, width=400, bg="lightgreen")
# Calculate center position of Frame_1
Frame_1.place(x=0,y=0,height=1000,width=820)

"VARIABLE"
name_1 = StringVar()
roll_1 = IntVar()
subject_1 = DoubleVar()
subject_2 = DoubleVar()
subject_3 = DoubleVar()
subject_4 = DoubleVar()
subject_5 = DoubleVar()


"HEADING"
heading = Label(Frame_1,text="PERCENTAGE CALCULATOR",font=("Times New Roman",40,"bold",UNDERLINE),bg="green",fg="black",justify='center',relief='groove',borderwidth=10)
heading.pack(padx=0,pady=0,ipady=20,fill='x')


"NAME AND ROLL NUMBER"
name = Label(Frame_1,text="Student Name  - ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=160)
text_name = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=30,textvariable=name_1)
text_name.place(x=300,y=160)

name = Label(Frame_1,text="Roll Number  - ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=220)
text_roll_no = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=30,textvariable=roll_1)
text_roll_no.place(x=300,y=220)

"SUBJECTS"
sub_number = Label(Frame_1,text="SUBJECT MARKS",font=("Times New Roman",40,"bold",UNDERLINE),bg="lightgreen",fg="black",justify='center',)
sub_number.pack(padx=100,pady=180,ipadx=20)


"NOW THE SUBJECT START"
sub1 = Label(Frame_1,text="Subject_1      -    ",font=("Times New Roman",25,"bold"),bg="lightgreen")
sub1.place(x=50,y=400)
text_sub1 = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=10,textvariable=subject_1)
text_sub1.place(x=320,y=400)


name = Label(Frame_1,text="Subject_2      -    ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=460)
text_name = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=10,textvariable=subject_2)
text_name.place(x=320,y=460)

name = Label(Frame_1,text="Subject_3      -    ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=520)
text_name = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=10,textvariable=subject_3)
text_name.place(x=320,y=520)

name = Label(Frame_1,text="Subject_4      -    ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=580)
text_name = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=10,textvariable=subject_4)
text_name.place(x=320,y=580)

name = Label(Frame_1,text="Subject_5      -    ",font=("Times New Roman",25,"bold"),bg="lightgreen")
name.place(x=50,y=640)
text_name = Entry(window,borderwidth=2,cursor="pencil",font=("Arial",20),width=10,textvariable=subject_5)
text_name.place(x=320,y=640)

calculate_button = Button(window,text="Calculate",bg="#0C090A",font=("Arial",30),justify=CENTER,relief='raised',borderwidth=5,fg="white",activebackground="#2CD88D",command=function_warpper)
calculate_button.place(x=190,y=750,height=55,width=450)


"FOR THE LAST TWO BLOCK"
perc = Label(Frame_1,text="PERCENTAGE  -     ",font=("Times New Roman",25,"bold"),bg="white")
perc.place(x=40,y=850,height=55,width=350)

division = Label(Frame_1,text="DIVISION    -          ",font=("Times New Roman",25,"bold"),bg="white")
division.place(x=430,y=850,height=55,width=340)

"CLEAR"
clear = Button(Frame_1,text="CLEAR",font=("Times New Roman",25,"bold"),bg="white",relief="raised",borderwidth=5,background="skyblue",activebackground="skyblue",command=clear_fields)
clear.place(x=250,y=930,height=55,width=300)

window.mainloop()
