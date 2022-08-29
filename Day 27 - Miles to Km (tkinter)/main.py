from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")
window.config(padx=50, pady=20)

def do_the_math():
    number = int(input.get())
    result = number * 1.6
    result_label.config(text=result)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

input_label = Label(text="is equal to", font=("Arial", 10))
input_label.grid(column=0, row=1)

result_label = Label (text="0", font=("arial", 10))
result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=do_the_math)
button.grid(column=1, row=2)



window.mainloop()