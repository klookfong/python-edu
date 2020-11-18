from tkinter import *

sc = Tk()
sc.title('Mile to km Converter')
sc.config(padx=20, pady=10)


#Entry Box
num_miles = Entry(width=7)
num_miles.grid(column=1, row=0)



#Three labels
miles_lab = Label(text="Miles")
miles_lab.grid(column=2, row=0)


sen = Label(text="Is equal to")
sen.grid(column=0, row=1)

km_lab = Label(text="km")
km_lab.grid(column=2, row=1)

output = Label(text="0")
output.grid(column=1, row=1)


#Button
def on_press():
    km = float(num_miles.get()) * 1.609
    output['text'] = format(km, '.1f')

button = Button(text="calculate", command = on_press)
button.grid(column=1, row=2)


sc.mainloop()