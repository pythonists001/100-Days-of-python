from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
# input.pack()
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 14, "normal"))
#my_label.pack(side="top") # side="bottom" #left,right,bottom ##pack label to our screen
miles_label.grid(column=4, row=0)

inKM = 0
text_label = Label(text="is equal to", font=("Arial", 14, "normal"))
text_label.grid(column=0, row=1)

km_label = Label(text="0 Km", font=("Arial", 14, "normal"))
km_label.grid(column=1, row=1)

def convert_to_km():
    milesVal = int(input.get())
    kmVal = milesVal * 4
    km_label.config(text=f"{kmVal} KM")

button = Button(text="Calculate", command=convert_to_km)
# button.pack()
button.grid(column=1, row=2)

window.mainloop()