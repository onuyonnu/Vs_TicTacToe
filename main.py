import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk




#Main window frame
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#Setting up initial button varibles
Player_turn = tk.StringVar(value= 'X')
move_TL = tk.StringVar(value = None)
move_TM = tk.StringVar(value = None)
move_TR = tk.StringVar(value = None)
move_ML = tk.StringVar(value = None)
move_MM = tk.StringVar(value = None)
move_MR = tk.StringVar(value = None)
move_BL = tk.StringVar(value = None)
move_BM = tk.StringVar(value = None)
move_BR = tk.StringVar(value = None)

reset_list = [move_TL, move_TM,move_TR ,move_ML, move_MM, move_MR,move_BL,move_BM, move_BR]



#Player turn fuction
def player_switch():
    global Player_turn
    if Player_turn.get() == "O":
        Player_turn.set("X")
    else:
        Player_turn.set("O")
#Row win check	
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            #print(f'{row[0]},test')
            return win_screen(row[0])
    return 0
#Diagonals win check
def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        #print('diag1')
        return win_screen(board[0][0])
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        #print('diag2')
        return win_screen(board[0][len(board)-1])
    return 0
    
#Full win check function also calls for pop up win for winner
def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return win_screen(result)
    return checkDiagonals(board)
#Makes a temporary board to check over for winner and fills empty spots with ascending ints
def make_board():
    boards = [[move_TL.get(),move_TM.get(),move_TR.get()],
             [move_ML.get(),move_MM.get(),move_MR.get()],
             [move_BL.get(),move_BM.get(),move_BR.get()]]
    checker = ["X","O"]
    place_holder = 1
    for line in boards:
        #print(line)
        for spot in range(len(line)):
            if line[spot] not in checker:
                #print(spot)
                line[spot] = place_holder
                place_holder += 1
    #print(boards)
    return boards


def win_screen(winner):
    top = tk.Toplevel(frm)
    top.wm_title("Game over")
    tk.Label(top, text= f'{winner}, is the winner!').grid(column=0, row=0)
    for reset in reset_list:
        reset.set(value = "")
    tk.Button(top, text = "Play again?", command=  top.destroy).grid(column=0, row=1)
    tk.Button(top, text = "Quit",command = root.destroy).grid(column=1, row=1)



Player_turn.set("X")
#print(Player_turn.get())

TL_inp = ttk.Button(frm, textvariable=move_TL, command=lambda : [move_TL.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=0, row=0)
TM_inp = ttk.Button(frm, textvariable=move_TM, command=lambda : [move_TM.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=1, row=0)
TR_inp = ttk.Button(frm, textvariable=move_TR, command=lambda : [move_TR.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=2, row=0)
ML_inp = ttk.Button(frm, textvariable=move_ML, command=lambda : [move_ML.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=0, row=1)
MM_inp = ttk.Button(frm, textvariable=move_MM, command=lambda : [move_MM.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=1, row=1)
MR_inp = ttk.Button(frm, textvariable=move_MR, command=lambda : [move_MR.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=2, row=1)
BL_inp = ttk.Button(frm, textvariable=move_BL, command=lambda : [move_BL.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=0, row=2)
BM_inp = ttk.Button(frm, textvariable=move_BM, command=lambda : [move_BM.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=1, row=2) 
BR_inp = ttk.Button(frm, textvariable=move_BR, command=lambda : [move_BR.set(Player_turn.get()), checkWin(make_board()), player_switch()]).grid(column=2, row=2)




#ttk.Button(frm, textvariable="Quit", command=root.destroy).grid(column=1, row=0)
#ttk.Button(frm, textvariable="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

