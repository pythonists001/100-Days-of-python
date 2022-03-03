from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top") # side="bottom" #left,right,bottom ##pack label to our screen
my_label["text"] = "New text"


## Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()













window.mainloop()  ## makes the window to be open