# Python program to create a
# GUI mark sheet using tkinter

# Import tkinter as tk
import tkinter as tk

# creating a new tkinter window
master = tk.Tk()

# assigning a title
master.title("MARKSHEET")

# specifying geomtery for window size
master.geometry("700x250")

# declaring objects for entering data
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


# function to display the total subject
# credits total credits and SGPA according
# to grades entered
def display():
    per = 0
    tot=0
    a=b=c=d=0
    a=e4.get()
    b=e5.get()
    c=e6.get()
    d=e7.get()
    tot= int(a) + int(b) + int(c) + int(d)
    per=(int(tot))/400*100
    # to display total credits
    tk.Label(master, text=str(tot)).grid(row=7, column=4)

    # to display SGPA
    tk.Label(master, text=str(per)).grid(row=8, column=4)
    if per>=85:
        tk.Label(master,text="A").grid(row=9,column=4)
    elif per>=75:
        tk.Label(master, text="B").grid(row=9, column=4)
    elif per>=45:
        tk.Label(master, text="c").grid(row=9, column=4)
    else:
        tk.Label(master, text="Fail").grid(row=9, column=4)

    if per>=45:
        tk.Label(master, text="Pass").grid(row=10, column=4)
    else:
        tk.Label(master, text="Fail").grid(row=10, column=4)



# end of display function

# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)

# label for registration number
tk.Label(master, text="Enrollment No").grid(row=0, column=3)

# label for roll Number
tk.Label(master, text="Roll.No").grid(row=1, column=0)

# labels for serial numbers
tk.Label(master, text="Srl.No").grid(row=2, column=0)
tk.Label(master, text="1").grid(row=3, column=0)
tk.Label(master, text="2").grid(row=4, column=0)
tk.Label(master, text="3").grid(row=5, column=0)
tk.Label(master, text="4").grid(row=6, column=0)

# labels for subject codes
tk.Label(master, text="Subject").grid(row=2, column=1)
tk.Label(master, text="Android").grid(row=3, column=1)
tk.Label(master, text="PHP").grid(row=4, column=1)
tk.Label(master, text="Python").grid(row=5, column=1)
tk.Label(master, text="Management").grid(row=6, column=1)

# label for grades
tk.Label(master, text="Obtained marks").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)

# labels for subject credits
tk.Label(master, text="Maximum marks").grid(row=2, column=3)
tk.Label(master, text="100").grid(row=3, column=3)
tk.Label(master, text="100").grid(row=4, column=3)
tk.Label(master, text="100").grid(row=5, column=3)
tk.Label(master, text="100").grid(row=6, column=3)


# taking entries of name, reg, roll number respectively
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

# organizing them in th e grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

# button to display all the calculated credit scores and sgpa
button1 = tk.Button(master, text="submit", bg="green", command=display)
button1.grid(row=8, column=1)

tk.Label(master, text="Total").grid(row=7, column=3)
tk.Label(master, text="Percentage").grid(row=8, column=3)
tk.Label(master, text="Grade").grid(row=9,column=3)
tk.Label(master,text="Result").grid(row=10,column=3)
master.mainloop()

# This Marksheet can be snapshotted and printed out
# as a report card for the semester
# This code has been contributed by Tanavi Narkhede, Kaushal Khachane, Amarbirsingh Randhawa
