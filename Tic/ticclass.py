import tkinter as tk
import random

class tictac:
    def __init__(self, master, players):
        #states save the ticked squares for players 1 and 2 as numbers 0-8
        self.state1 = []
        self.state2 = []
        self.canvas = tk.Canvas(master, width=310, height=310)
        self.canvas.pack()
        self.turn   = True
        self.players= players
        self.wincnt1 = 0
        self.wincnt2 = 0
        self.drawcnt = 0
        self.draw()
        
    def wincheck(self,state):
        win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for comb in win:
            if comb[0] in state and comb[1] in state and comb[2] in state:
                return True
        else:
            return False

    #the event function alone cant take arguments: pass a function taking arguments
    #with the outter function
    def clicked(self,i):
        def fn(*args):
            if self.turn == True:
                #cant tic the same square twice
                if i not in self.state1+self.state2:
                    self.state1.append(i)
                    self.turn = not self.turn
            else:
                if i not in self.state1+self.state2:
                    self.state2.append(i)
                    self.turn = not self.turn
            self.update()
            if self.players==1:
                if (len(self.state1+self.state2) < 9 and not 
                    self.wincheck(self.state1)):
                    self.AI()
        return fn
    
    def circle(self,x,y):
        item = self.canvas.create_oval(x-30,y-30,x+30,y+30,width=3,tags="tic")
        return item

    def cross(self,x,y):
        ln1 = self.canvas.create_line(x,y,x+60,y+60,width=3,tags="tic")
        ln2 = self.canvas.create_line(x+60,y,x,y+60,width=3,tags="tic")
        item = ln1 + ln2
        return item

    def draw(self):
        btns = ["1","2","3","4","5","6","7","8","9"]
        for i in range(9):
            #create_rectange(start_x,start_y,end_x,end_y):
            #the x coord should increase for 100 each iteration, to a maximum of
            #205 (the board is shifted (5,5) since the lines take space too)
            #the y coord should increase by 100 every 3 iterations, since the int
            #cast just cuts the digits after the comma the total for y increases
            #every 3rd iteration
            #the end coords are shifted 100
            self.canvas.create_rectangle(5+(i%3)*100,5+(int(i/3)*100),
            5+(i%3+1)*100,5+(int(i/3)+1)*100, fill="light grey",
                    width=3,tags=btns[i])
            self.canvas.tag_bind(btns[i],"<Button-1>",self.clicked(i))

    def update(self):
        #see draw() method
        for i in self.state1:
            self.circle(55+(i%3)*100,55+(int(i/3)*100))
        for i in self.state2:
            self.cross(25+(i%3)*100,25+(int(i/3)*100))

        if (self.wincheck(self.state1) or self.wincheck(self.state2)
            or len(self.state1+self.state2)>8):
            self.gameoverscreen()

    def gameoverscreen(self):
        self.canvas.create_oval(20,95,295,215,fill = "light grey",
            outline = "black",width=1,tags="end")
        if self.wincheck(self.state1):
            self.canvas.create_text(155,155,font=("Purisa", 20),
                text=" Player 1 \n  wins!",tags="end")
            self.wincnt1 += 1
        elif self.wincheck(self.state2) == True:
            self.canvas.create_text(155,155,font=("Purisa", 20),
                text=" Player 2 \n  wins!",tags="end")
            self.wincnt2 += 1
        elif len(self.state1 + self.state2) > 8:
            self.canvas.create_text(155,155,font=("Purisa", 20),text="Draw!",
                tags="end")
            self.drawcnt += 1
        self.canvas.tag_bind("end","<Button-1>",self.newgame)
        
        self.canvas.create_rectangle(80,218,235,282,fill="light grey",tags="end")
        self.canvas.create_text(155,250,text="Wins Player 1: " + str(self.wincnt1) +
            "\nWins Player 2: " + str(self.wincnt2) + "\n        Draws:" + str(self.drawcnt),
            tags="end",font=("Serif", 8))

    def newgame(self,event):
        self.turn=True
        self.canvas.delete("end","tic")
        self.state1 = []
        self.state2 = []
        self.update()

    def AI(self):
        #check if AI could win next round
        if self.turn==False:
            for i in range(9):
                if self.wincheck(self.state2+[i]) and i not in self.state1+self.state2:
                    self.state2.append(i)
                    self.turn=True
                    break
        #check if player could win next round
        if self.turn==False:
            for i in range(9):
                if self.wincheck(self.state1+[i]) and i not in self.state1+self.state2:
                    self.state2.append(i)
                    self.turn=True
                    break
        #check if player could win in two rounds
        if self.turn==False:
            for i in range(0,8,2):
                if i not in self.state1+self.state2:
                    self.state2.append(i)
                    self.turn=True
                    break
        if self.turn==False:
            for i in range(1,9,3):
                if i not in self.state1+self.state2:
                    self.state2.append(i)
                    self.turn=True
                    break
        self.update()

class menu:
    def __init__(self,master):
        self.canvas = tk.Canvas(master,height=310,width=310)
        self.canvas.pack()

        self.canvas.create_rectangle(55,80,255,140,fill="light grey",tags="single")
        self.canvas.create_text(155,110,text="1 Player",tags="single")
        self.canvas.tag_bind("single","<Button-1>",self.one)

        self.canvas.create_rectangle(55,160,255,220,fill="light grey",tags="twop")
        self.canvas.create_text(155,190,text="2 Player",tags="twop")
        self.canvas.tag_bind("twop","<Button-1>",self.two)


    def one(self,event):
        self.canvas.destroy()
        tictac(master,1)

    def two(self,event):
        self.canvas.destroy()
        tictac(master,2)


master = tk.Tk()
master.title("Tic-Tac-Toe")

menu(master)

tk.mainloop()
