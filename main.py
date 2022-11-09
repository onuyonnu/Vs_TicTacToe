import tkinter as tk
from tkinter import *
from tkinter import ttk


root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
#ttk.Button(frm, textvariable="Hello World!").grid(column=0, row=0)

Player_turn = tk.StringVar(value= 'X')
move_TL = tk.StringVar(value= " ")
move_TM = tk.StringVar(value= " ")
move_TR = tk.StringVar(value= " ")
move_ML = tk.StringVar(value= " ")
move_MM = tk.StringVar(value= " ")
move_MR = tk.StringVar(value= " ")
move_BL = tk.StringVar(value= " ")
move_BM = tk.StringVar(value= " ")
move_BR = tk.StringVar(value= " ")


def player_choice():
    print(move_TL.get())
    if Player_turn.get() == "X":
        Player_turn.set("O")
    else:
        Player_turn.set("X")


def player_switch():
    global Player_turn
    
    if Player_turn.get() == "O":
        Player_turn.set("X")
    else:
        Player_turn.set("O")
import numpy as np

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

def make_board():
    boards = [[move_TL.get(),move_TM.get(),move_TR.get()],
             [move_ML.get(),move_MM.get(),move_MR.get()],
             [move_BL.get(),move_BM.get(),move_BR.get()]]
    return boards

Player_turn.set("X")
print(Player_turn.get())

TL_inp = ttk.Button(frm, textvariable=move_TL, command=lambda : [move_TL.set(Player_turn.get(), checkWin(make_board())), player_switch(),]).grid(column=0, row=0)
TM_inp = ttk.Button(frm, textvariable=move_TM, command=lambda : [move_TM.set(Player_turn.get()), player_switch()]).grid(column=1, row=0)
TR_inp = ttk.Button(frm, textvariable=move_TR, command=lambda : [move_TR.set(Player_turn.get()), player_switch()]).grid(column=2, row=0)
ML_inp = ttk.Button(frm, textvariable=move_ML, command=lambda : [move_ML.set(Player_turn.get()), player_switch()]).grid(column=0, row=1)
MM_inp = ttk.Button(frm, textvariable=move_MM, command=lambda : [move_MM.set(Player_turn.get()), player_switch()]).grid(column=1, row=1)
MR_inp = ttk.Button(frm, textvariable=move_MR, command=lambda : [move_MR.set(Player_turn.get()), player_switch()]).grid(column=2, row=1)
BL_inp = ttk.Button(frm, textvariable=move_BL, command=lambda : [move_BL.set(Player_turn.get()), player_switch()]).grid(column=0, row=2)
BM_inp = ttk.Button(frm, textvariable=move_BM, command=lambda : [move_BM.set(Player_turn.get()), player_switch()]).grid(column=1, row=2) 
BR_inp = ttk.Button(frm, textvariable=move_BR, command=lambda : [move_BR.set(Player_turn.get()), player_switch()]).grid(column=2, row=2)




#ttk.Button(frm, textvariable="Quit", command=root.destroy).grid(column=1, row=0)
#ttk.Button(frm, textvariable="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
