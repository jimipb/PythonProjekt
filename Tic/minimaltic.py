import tkinter as tk

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

def circle(canvas,x,y,r,w):
    item = canvas.create_oval(x-r,y-r,x+r,y+r,width=w)
    return item

def cross(canvas,x,y):
    item = canvas.create_line(x,y,x+60,y+60,width=3)
    return item


def clicked(state1,state2,turn,nr):
    def fn(*args):
        if turn==True:
            state1.append(nr)
        else:
            state2.append(nr)
    return fn

def board(state1,state2,turn):
    btns = ["1","2","3","4","5","6","7","8","9"]
    x=5
    y=5
    for i in range(9):
        w.create_rectangle(x,y,x+100,y+100, fill="light grey",
                width=3,tags=btns[i])
        w.tag_bind(btns[i],"<Button-1>",clicked(state1,state2,turn,i))
        turn = not turn
        if x >= 200:
            x = 5
            y += 100
        else:
            x += 100
    for i in state1:
        if i < 3:
            circle(w,55+i*100,55,30,3)
        elif i > 3 and i < 6:
            circle(w, 55+i*100,155,30,3)
        else:
            circle(w,55+i*100,255,30,3)
    for i in state2:
        if i < 3:
            cross(w,25+i*100,25)
        elif i > 3 and i < 6:
            cross(w,25+i*100,125)
        else:
            cross(w,25+i*100,225)
    return turn

master = tk.Tk()

state1=[]
state2=[]
turn = False
    
w = tk.Canvas(master, width=310, height=310)
turn = board(state1,state2,turn)
w.pack()
tk.mainloop()