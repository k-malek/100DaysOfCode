import tkinter
import tkinter.ttk as ttk

app_font=("Arial Narrow",12,"bold")

def kelv_to_cel_calc(present,amount):
    try:
        amount=float(amount)
    except ValueError:
        present['text']='Please, input integer or decimal'
    else:
        present['text']=f'It is {float(amount)-273.15:.2f}\N{DEGREE SIGN}C'


window = tkinter.Tk()


window.title("Kelvin to Celsius converter")
#window.minsize(width=500,height=300)

kelvin_input=ttk.Entry(window)
kelvin_label = ttk.Label(window,text="How many Kelvins?",font=app_font)
result_label = ttk.Label(window,font=app_font)
button = ttk.Button(window,text="Convert",command=lambda: kelv_to_cel_calc(result_label,kelvin_input.get()))

kelvin_input.grid(row=0,column=1)
kelvin_label.grid(row=0,column=0)
button.grid(row=1,column=1)
result_label.grid(row=2, column=0, columnspan=2)

window.bind('<Return>',lambda x: kelv_to_cel_calc(result_label,kelvin_input.get()))
window.mainloop()