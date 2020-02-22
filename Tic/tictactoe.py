import tkinter as tk

window = tk.Tk()
window.title("Tic-Tac-Toe")

btn = {}
var = {}
rowcnt=0
colcnt=0
cnt=0
for i in range(9):
    i = tk.BooleanVar()
    var[cnt] = i
    cnt += 1

cnt=0
for i in range(9):
    i = tk.Checkbutton(master=window, text="", variable=var[cnt])
    i.grid(row=rowcnt, column=colcnt)
    btn[cnt] = i
    cnt+=1
    if colcnt==2:
        rowcnt+=1
        colcnt=0
    else:
        colcnt+=1

label = tk.Label(window, text="")
label.grid(row=3)

def wincheck(state):
    if 1 in state and 2 in state and 3 in state:
        return True
    elif 4 in state and 5 in state and 6 in state:
        return True
    elif 7 in state and 8 in state and 9 in state:
        return True
    elif 1 in state and 4 in state and 7 in state:
        return True
    elif 2 in state and 5 in state and 8 in state:
        return True
    elif 3 in state and 6 in state and 9 in state:
        return True
    elif 1 in state and 5 in state and 9 in state:
        return True
    elif 3 in state and 5 in state and 7 in state:
        return True
    else:
        return False

def callback(event):
    text=""
    state = []
    for i in range(9):
        state.append((i+1)*var[i].get())
    print(state)
    if wincheck(state):
        text="win"
    label.configure(text=text)

for i in range(9):
    btn[i].bind("<ButtonRelease>", callback)

tk.mainloop()
