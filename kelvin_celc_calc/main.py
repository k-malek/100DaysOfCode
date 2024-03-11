import tkinter
import tkinter.ttk as ttk

APP_FONT=("Arial Narrow",12,"bold")
GRID_ELEMENTS_PADDING_X,GRID_ELEMENTS_PADDING_Y=(20,10)

def kelv_to_cel_calc(present,amount):
    try:
        amount=float(amount)
    except ValueError:
        present['text']='Please, input integer or decimal'
    else:
        present['text']=f'It is {float(amount)-273.15:.2f}\N{DEGREE SIGN}C'


window = tkinter.Tk()
window.title("Kelvin to Celsius converter")
window.config(padx=30,pady=20)

kelvin_input=ttk.Entry(window, width=8)
kelvin_label = ttk.Label(window,text="How many Kelvins to convert?",font=APP_FONT)
result_label = ttk.Label(window,text="Result will appear here", font=APP_FONT)
button = ttk.Button(window,text="Convert",command=lambda: kelv_to_cel_calc(result_label,kelvin_input.get()))

kelvin_input.grid(row=0,column=1, padx=GRID_ELEMENTS_PADDING_X, pady=GRID_ELEMENTS_PADDING_Y)
kelvin_label.grid(row=0,column=0, padx=GRID_ELEMENTS_PADDING_X, pady=GRID_ELEMENTS_PADDING_Y)
button.grid(row=1,column=0,columnspan=2, padx=GRID_ELEMENTS_PADDING_X, pady=GRID_ELEMENTS_PADDING_Y)
result_label.grid(row=2, column=0, columnspan=2, padx=GRID_ELEMENTS_PADDING_X, pady=GRID_ELEMENTS_PADDING_Y)

window.bind('<Return>',lambda x: kelv_to_cel_calc(result_label,kelvin_input.get()))
window.mainloop()