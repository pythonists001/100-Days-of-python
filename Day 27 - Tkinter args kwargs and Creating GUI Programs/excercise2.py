from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
## padding
window.config(padx=20, pady=20)
## we can add padding to label and button as well.

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack(side="top") # side="bottom" #left,right,bottom ##pack label to our screen
my_label["text"] = "New text"
my_label.grid(column=0, row=0)

new_button = Button(text="Click Me")
# button.pack()
new_button.grid(column=2, row=0)

## Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
## pack() place() and grid()

# we can't mix grid and pack in same program.









window.mainloop()  ## makes the window to be open