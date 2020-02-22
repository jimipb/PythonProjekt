import tkinter as tk
import random
import time

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

def AI(state1,state2):
    time.sleep(0.5)
    turn=False
    for i in range(1,10):
        if wincheck(state2 + [i]) and i not in state1+state2 and turn==False:
            state2.append(i)
            break
        if wincheck(state1 + [i]) and i not in state1+state2 and turn==False:
            state2.append(i)
            turn=True
            break
    if 5 not in state1+state2 and turn==False:
        state2.append(5)
        turn=True
    elif 1 not in state1+state2 and turn==False:
        state2.append(1)
        turn=True
    elif 3 not in state1+state2 and turn==False:
        state2.append(3)
        turn=True
    elif 7 not in state1+state2 and turn==False:
        state2.append(7)
        turn=True
    elif 9 not in state1+state2 and turn==False:
        state2.append(9)
        turn=True
    else:
        while turn==False:
            tic = random.randint(1,9)
            if tic not in state1+state2:
                state2.append(tic)
                turn=True

def circle(canvas,x,y,r,w):
    item = canvas.create_oval(x-r,y-r,x+r,y+r,width=w)
    return item

def clicked(state,nr):
    def fn(*args):
        state.append(i+1)

#def clicked(nr,scale,turn):
#    def fn(*args):
#        for i in range(9):
#            if turn == True:
#                if i == nr:
#                    state1.append(i+1)
#                    if i > 2 and i < 6:
#                        x = 20+(i-3)*100*scale
#                        y = 20+100*scale
#                    elif i < 3:
#                        x = 20+i*100*scale
#                        y = 20
#                    else:
#                        x = 20+(i-6)*100*scale
#                        y = 20+200*scale
#                    w.create_line(x+3*scale,y+3*scale,x+85*scale-3*scale,
#                            y+85*scale-3*scale,width=3*scale)
#                    w.create_line(x+85*scale-3*scale,y+3*scale,x+3*scale,
#                            y+85*scale-3*scale,width=3*scale)
#            else:
#                if i == nr:
#                    state2.append(i+1)
#                    if i > 2 and i < 6:
#                        x = 52.5*scale+(i-3)*100*scale
#                        y = 52.5*scale+100*scale
#                    elif i < 3:
#                        x = 52.5*scale+i*100*scale
#                        y = 52.5*scale
#                    else:
#                        x = 52.5*scale+(i-6)*100*scale
#                        y = 52.5*scale+200*scale
#                    circle(w,x,y,40*scale,3*scale)
#    return fn

def gameboard(state1,state2,scale,turn):
    btns = ["1","2","3","4","5","6","7","8","9"]
    x=5
    y=5
    for i in range(9):
        w.create_rectangle(x,y,x+100*scale,y+100*scale, fill="light grey",
                width=3*scale,tags=btns[i])
        w.tag_bind(btns[i],"<Button-1>",clicked(i,scale,turn))
        turn = not turn
        if x >= 200*scale:
            x = 5
            y += 100*scale
        else:
            x += 100*scale

while 1:
    master = tk.Tk()

    state1=[]
    state2=[]
    
    turn = False
    
    scale = 2 
    
    w = tk.Canvas(master, width=310*scale, height=310*scale)
    
    gameboard(state1,state2,scale,turn)
    
    if wincheck(state1) == True:
        w.create_oval(20,95,295,215, fill = "light grey", outline = "black",width=1)
        w.create_text(155,155,font=("Purisa", 20),text=" Player 1 \n  wins!")
    elif wincheck(state2) == True:
        w.create_oval(20,95,295,215, fill = "light grey", outline = "black",width=1)
        w.create_text(155,155,font=("Purisa", 20),text=" Player 2 \n  wins!")
    
    w.pack()
    tk.mainloop()

