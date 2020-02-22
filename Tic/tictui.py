import os
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

def gameboard(state1, state2):
    board = ""
    for i in range(1,10):
        if i in state1:
            board += "|x"
        elif i in state2:
            board += "|o"
        else:
            board += "|" + str(i)
        if i in [3,6,9]:
            board += "|\n"
    board += "x: Player 1, o: Player 2 \n"
    return board

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

clear = lambda: os.system('clear')

draw = 0
win1 = 0
win2 = 0
state1 = []
state2 = []
turn = True
players = input("How many Players? ")
while players not in ["0","1","2","3","4","5","6","7","8","9"]:
    print("Invalid Input")
    players = input("How many Players? ")
game=True
for i in range(30):
    while(wincheck(state1) == False  and wincheck(state2) == False 
            and (len(state1+state2)<9)):
        clear()
        print(gameboard(state1,state2))
        if turn == True:
            if int(players)!=0:
                tic = input("Player 1:")
                print(tic)
                if tic not in ["1","2","3","4","5","6","7","8","9"]:
                    print("Invalid Input!")
                elif int(tic) in state1+state2:
                    print("Already ticked!")
                else:
                    state1.append(int(tic))
                    turn=False
            else:
                AI(state2,state1)
                turn=False
        elif turn == False:
            if int(players)>1:
                tic = input("Player 2:")
                if eval(tic) not in list(range(10)):
                    print("Invalid input!")
                elif int(tic) in state1+state2:
                    print("Already ticked!")
                else:
                    state2.append(int(tic))
                    turn=True
            else:
                AI(state1,state2)
                turn=True
     
    clear()
    print(gameboard(state1,state2))
    if wincheck(state1) == True:
        print("Player 1 won!")
        time.sleep(0.5)
        win1 += 1
    elif wincheck(state2) == True:
        print("Player 2 won!")
        time.sleep(0.5)
        win2 += 1
    else:
        print("Draw!")
        time.sleep(0.5)
        draw +=1
    state1 = []
    state2 = []
print("Draws:", draw)
print("Wins Player 1:", win1)
print("Wins Player 2:", win2)
