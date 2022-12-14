from tkinter import *


def button_clicked():
    """When click button, do something!"""
    miles_text = int(entry.get())
    km_text = miles_text * 1.609344
    result_label.config(text=km_text)

# Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Labels
miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)
km_label = Label(text="Km", font=("Arial", 20))
km_label.grid(column=2, row=1)
equal_label = Label(text="is equal to", font=("Arial", 20))
equal_label.grid(column=0, row=1)
result_label = Label(text="0", font=("Arial", 20))
result_label.grid(column=1, row=1)

#Buttons
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entries
entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1, row=0)

window.mainloop()
