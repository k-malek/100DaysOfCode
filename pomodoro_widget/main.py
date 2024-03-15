import tkinter as tk
from PIL import Image,ImageTk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#dddddd"
WIDGET_FONT = ("Courier",30,'bold')
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
POMODORO_SET=[WORK_MIN,SHORT_BREAK_MIN]*3+[WORK_MIN,LONG_BREAK_MIN]
POMODORO_LABELS=["WORK!!!","RELAX..."]*4

# ---------------------------- POMODORO REPS ------------------------------- #
rep=1

def start_pomodoro(master):
    global curr_time,rep
    if curr_time==0:
        if rep<=len(POMODORO_SET) and rep>0:
            set_timer(master,POMODORO_SET[rep-1])
        elif rep==0:
            rep=1
            set_timer(master,POMODORO_SET[rep-1])
        present_labels()
        

def present_labels():
    global rep
    if rep==0 or rep>len(POMODORO_LABELS):
        label['text']="TIMER"
        label['fg']=PINK
    else:
        label['text']=POMODORO_LABELS[rep-1]
        if rep%2==1:
            label['fg']=RED
        else:
            label['fg']=GREEN
    checkmarks['text']='✔'*(rep//2)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global curr_time,rep
    curr_time=0
    rep=0
    present_time()
    present_labels()
# ---------------------------- TIMER MECHANISM ------------------------------- # 
curr_time=0

def time_to_string(time_val):
        time_val=int(time_val)
        return str(time_val) if len(str(time_val))>1 else '0'+str(time_val)

def present_time():
    canvas.itemconfig(timer_label,text=time_to_string(curr_time//60)+':'+time_to_string(curr_time%60))
     

def set_timer(master,set_time_mins):
    global curr_time
    curr_time=set_time_mins*60
    present_time()
    # Window timer, applying timer functionality
    master.after(1000,timer_tick,master)
     

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    
def timer_tick(master):
    global curr_time,rep
    if curr_time>0:
        curr_time-=1
        present_time()
        master.after(1000,timer_tick,master)
    elif rep>0:
         rep+=1
         start_pomodoro(master)

# ---------------------------- UI SETUP ------------------------------- #

# Window setup

window=tk.Tk()
window.title("Pomodoro widget")
window.config(padx=100,pady=50,background=YELLOW)

# UI elements configuration

label=tk.Label(text="TIMER",font=WIDGET_FONT,foreground=PINK,background=YELLOW)

canvas=tk.Canvas(width=200,height=224,master=window,background=YELLOW,highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(100,112,image=tomato_img)
timer_label=canvas.create_text(100,132,text="00:00",font=WIDGET_FONT,fill=GREY)

start_button=tk.Button(text='Start',anchor='e',command=lambda:start_pomodoro(window))
reset_button=tk.Button(text='Reset',anchor='w',command=lambda:reset_timer())

checkmarks=tk.Label(font=WIDGET_FONT,foreground=GREEN,background=YELLOW)

# Items placement

label.grid(row=0,column=1)
canvas.grid(row=1,column=1)
start_button.grid(row=2,column=0)
reset_button.grid(row=2,column=2)
checkmarks.grid(row=3,column=1)

# Mainloop

window.mainloop()