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

def circle(canvas,x,y):
    r=25
    item = canvas.create_oval(x-r,y-r,x+r,y+r,width=5)
    return item

def cross(canvas,x,y):
    l=50
    item1 = canvas.create_line(x,y,x+l,y+l, width=5)
    item2 = canvas.create_line(x+l,y,x,y+l, width=5)
    return item1,item2

def clicked(nr):
    def fn(*args):
        state.append(nr)
        turn==False
    return fn

def board(state1, state2):
    x = 6 
    y = 6
    fill= "white"
    btns = ["1","2","3","4","5","6","7","8","9"]
    for i in range(9):
        w.create_rectangle(x,y,x+100,y+100,fill="light grey",activefill=fill,outline="black",tags=btns[i])
        w.tag_bind(btns[i],"<Button-1>",clicked(i))
        if x>=200:
            y += 100
            x = 6 
        else:
            x += 100
    x=6
    y=6
    for i in range(1,10):
        if i in state1:
            circle(w,x+50,y+50)
        if x>=200:
            y+=100
            x = 6
        else:
            x+=100
    x=31
    y=31
    for i in range(1,10):
        if i in state2:
            cross(w,x,y)
        if x>=200:
            y+=100
            x = 31
        else:
            x+=100


master = tk.Tk()
master.title("Tic-Tac-Toe")
w = tk.Canvas(master, width=310, height=310)
w.configure(background="light grey")
w.pack()

state1 = []
state2 = []
turn = True
players=1

while wincheck(state1) == False  and wincheck(state2) == False and (len(state1+state2)<9):
    board(state1,state2)
    #if turn == True:
    #    if int(players)!=0:
    #        tic = input("Player 1:")
    #        if tic not in ["1","2","3","4","5","6","7","8","9"]:
    #            print("Invalid Input!")
    #        elif int(tic) in state1+state2:
    #            print("Already ticked!")
    #        else:
    #            state1.append(int(tic))
    #            turn=False
    #    else:
    #        AI(state2,state1)
    #        turn=False
    #elif turn == False:
    #    if int(players)>1:
    #        tic = input("Player 2:")
    #        if eval(tic) not in list(range(10)):
    #            print("Invalid input!")
    #        elif int(tic) in state1+state2:
    #            print("Already ticked!")
    #        else:
    #            state2.append(int(tic))
    #            turn=True
    #    else:
    #        AI(state1,state2)
    #        turn=True

if wincheck(state1) == True:
    w.create_oval(20,95,295,215, fill = "light grey", outline = "black",width=1)
    w.create_text(155,155,font=("Purisa", 20),text=" Player 1 \n  wins!")
elif wincheck(state2) == True:
    w.create_oval(20,95,295,215, fill = "light grey", outline = "black",width=1)
    w.create_text(155,155,font=("Purisa", 20),text=" Player 2 \n  wins!")
else:
    w.create_oval(20,95,295,215, fill = "light grey", outline = "black",width=1)
    w.create_text(155,155,font=("Purisa", 20),text="Draw!")
 
master.mainloop()
