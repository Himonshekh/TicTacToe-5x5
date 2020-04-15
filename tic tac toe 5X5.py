import random
from tkinter import *
import math
from array import *
import numpy as np

import tkinter.messagebox

# Design part
tk = Tk()

tk.title('Tic Tac Toe')
tk.geometry("800x800")


flag = 0
box_h = 3
box_w = 6


#  main code start

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
    button10.configure(state=DISABLED)
    button11.configure(state=DISABLED)
    button12.configure(state=DISABLED)
    button13.configure(state=DISABLED)
    button14.configure(state=DISABLED)
    button15.configure(state=DISABLED)
    button16.configure(state=DISABLED)
    button17.configure(state=DISABLED)
    button18.configure(state=DISABLED)
    button19.configure(state=DISABLED)
    button20.configure(state=DISABLED)
    button21.configure(state=DISABLED)
    button22.configure(state=DISABLED)
    button23.configure(state=DISABLED)
    button24.configure(state=DISABLED)
    button25.configure(state=DISABLED)


# game code from here
flg = 1

board = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]
inf = 9999999


class pos:
    def __init__(self, rowID, columnID):
        self.row = rowID
        self.column = columnID


def fillBoard(board_p):
    for i in range(5):
        for j in range(5):
            if board_p[i][j] == ' ':
                return 0
    return 1


def isDraw(board_p):
    if 1 == fillBoard(board_p):
        return 1
    return 0


def equal_(c1, c2, c3, c4, c5):
    if c1 == c2 and c1 == c3 and c1 == c4 and c1 == c5 and c1 != ' ':
        return 1
    return 0


def bestComputerMove(board_p):
    max_p = -1
    row_p = -1
    id_p = -5
    id_t = -5
    for i in range(5):
        c1 = 0
        c2 = 0
        c3 = 0
        for j in range(5):
            if board_p[i][j] == 'O':
                c1 = c1 + 1
            elif board_p[i][j] == 'X':
                c2 = c2 + 1
            else:
                c3 = c3 + 1
        if c1 > 0 and c2 == 0:
            if max_p < c1:
                max_p = c1
                id_t = i
                row_p = 1

    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0

    for i in range(5):
        c1 = 0
        c2 = 0
        c3 = 0
        for j in range(5):
            if i == j:
                if board_p[i][i] == 'O':
                    c4 = c4 + 1
                elif board_p[i][i] == 'X':
                    c5 = c5 + 1
                else:
                    c6 = c6 + 1
            if i + j == 4:
                if board_p[i][j] == 'O':
                    c7 = c7 + 1
                elif board_p[i][j] == 'X':
                    c8 = c8 + 1
                else:
                    c9 = c9 + 1

            if board_p[j][i] == 'O':
                c1 = c1 + 1
            elif board_p[j][i] == 'X':
                c2 = c2 + 1
            else:
                c3 = c3 + 1
        if c1 > 0 and c2 == 0:
            if max_p < c1:
                max_p = c1
                id_t = i
                row_p = 0

    if c4 > 0 and c5 == 0:
        if max_p < c4:
            max_p = c4
            id_p = -1

    if c7 > 0 and c8 == 0:
        if max_p < c7:
            id_p = -2
            max_p = c7

    # print('here', max_p)
    if id_p == -1:
        if board_p[0][0] == ' ':
            return 0, 0
        elif board_p[1][1] == ' ':
            return 1, 1
        elif board_p[2][2] == ' ':
            return 2, 2
        elif board_p[3][3] == ' ':
            return 3, 3
        else:
            return 4, 4
    elif id_p == -2:
        if board_p[0][4] == ' ':
            return 0, 4
        elif board_p[1][3] == ' ':
            return 1, 3
        elif board_p[2][2] == ' ':
            return 2, 2
        elif board_p[3][1] == ' ':
            return 3, 1
        else:
            return 4, 0
    else:
        if row_p == 1:
            if board_p[id_t][0] == ' ':
                return id_t, 0
            elif board_p[id_t][1] == ' ':
                return id_t, 1
            elif board_p[id_t][2] == ' ':
                return id_t, 2
            elif board_p[id_t][3] == ' ':
                return id_t, 3
            else:
                return id_t, 4
        elif row_p == 0:
            if board_p[0][id_t] == ' ':
                return 0, id_t
            elif board_p[1][id_t] == ' ':
                return 1, id_t
            elif board_p[2][id_t] == ' ':
                return 2, id_t
            elif board_p[3][id_t] == ' ':
                return 3, id_t
            else:
                return 4, id_t
    return -1, -1


def checkWin(board_p, who):
    who = who + " Win :) ..."
    for i in range(5):
        if 1 == equal_(board_p[i][0], board_p[i][1], board_p[i][2], board_p[i][3], board_p[i][4]):
            tkinter.messagebox.showinfo("Game Over", who)
            disableButton()
            return 1

    for i in range(5):
        if 1 == equal_(board_p[0][i], board_p[1][i], board_p[2][i], board_p[3][i], board_p[4][i]):
            tkinter.messagebox.showinfo("Game Over ", who)
            disableButton()
            return 1

    if equal_(board_p[0][0], board_p[1][1], board_p[2][2], board_p[3][3], board_p[4][4]):
        tkinter.messagebox.showinfo("Game Over", who)
        disableButton()
        return 1

    if equal_(board_p[0][4], board_p[1][3], board_p[2][2], board_p[3][1], board_p[4][0]):
        tkinter.messagebox.showinfo("Game Over", who)
        disableButton()
        return 1
    if isDraw(board) == 1:
        tkinter.messagebox.showinfo("Game Over", "Game Tie :( ..")
        disableButton()
        return 1
    return 0


def winPossiblity(board_p):
    for i in range(5):
        if 1 == equal_(board_p[i][0], board_p[i][1], board_p[i][2], board_p[i][3], board_p[i][4]):
            if board_p[i][0] == 'X':
                return -10
            else:
                return 10

    for i in range(5):
        if 1 == equal_(board_p[0][i], board_p[1][i], board_p[2][i], board_p[3][i], board_p[4][i]):
            if board_p[0][i] == 'X':
                return -10
            else:
                return 10
    if equal_(board_p[0][0], board_p[1][1], board_p[2][2], board_p[3][3], board_p[4][4]):
        if board_p[0][0] == 'X':
            return -10
        else:
            return 10
    if equal_(board_p[0][4], board_p[1][3], board_p[2][2], board_p[3][1], board_p[4][0]):
        if board_p[0][4] == 'X':
            return -10
        else:
            return 10
    return 0


def alphaBeta(board_p, depth, player, alpha, beta, height):
    score = winPossiblity(board_p)
    # print('inside',score)
    if depth == 3:
        # print(score)
        return score
    if score == 10:
        return score
    if score == -10:
        return score
    if 1 == isDraw(board_p):
        return 0
    if 1 == player:
        best = -inf
        for i in range(5):
            for j in range(5):
                if board_p[i][j] == ' ':
                    board_p[i][j] = 'O'
                    l_best = alphaBeta(board_p, depth + 1, player ^ 1, alpha, beta, height)
                    board_p[i][j] = ' '
                    best = max(best, l_best)
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        return best

        return best
    else:
        best = inf
        for i in range(5):
            for j in range(5):
                if board_p[i][j] == ' ':
                    board_p[i][j] = 'X'
                    l_best = alphaBeta(board_p, depth + 1, player ^ 1, alpha, beta, height)
                    board_p[i][j] = ' '
                    best = min(best, l_best)
                    beta = min(beta, best)
                    if alpha >= beta:
                        return best
        return best


def findBestMove(board_p):
    bestMove = pos(5, 6)
    bestMove.row = -1
    bestMove.column = -1
    bestVal = -inf
    cnt = 0
    for i in range(5):
        for j in range(5):
            if board_p[i][j] == ' ':
                board_p[i][j] = 'O'
                moveVal = alphaBeta(board_p, 0, 0, -inf, inf, 1)
                board_p[i][j] = ' '
                if moveVal > bestVal:
                    bestMove.row = i
                    bestMove.column = j
                    bestVal = moveVal
                    cnt = cnt + 1
    if cnt == 1 and 0 == moveVal:
        possible = []
        for i in range(5):
            for j in range(5):
                if board_p[i][j] == ' ':
                    possible.append(i)
                    possible.append(j)
        length = len(possible)
        if length > 2:
            a, b = bestComputerMove(board_p)
            if a != -1:
                bestMove.row = a
                bestMove.column = b
        possible.clear()
    return bestMove


def reset():
    for i in range(5):
        for j in range(5):
            board[i][j] = ' '

    button1.configure(state="normal")
    button2.configure(state="normal")
    button3.configure(state="normal")
    button4.configure(state="normal")
    button5.configure(state="normal")
    button6.configure(state="normal")
    button7.configure(state="normal")
    button8.configure(state="normal")
    button9.configure(state="normal")
    button10.configure(state="normal")
    button11.configure(state="normal")
    button12.configure(state="normal")
    button13.configure(state="normal")
    button14.configure(state="normal")
    button15.configure(state="normal")
    button16.configure(state="normal")
    button17.configure(state="normal")
    button18.configure(state="normal")
    button19.configure(state="normal")
    button20.configure(state="normal")
    button21.configure(state="normal")
    button22.configure(state="normal")
    button23.configure(state="normal")
    button24.configure(state="normal")
    button25.configure(state="normal")
    button1["text"] = ' '
    button2["text"] = ' '
    button3["text"] = ' '
    button4["text"] = ' '
    button5["text"] = ' '
    button6["text"] = ' '
    button7["text"] = ' '
    button8["text"] = ' '
    button9["text"] = ' '
    button10["text"] = ' '
    button11["text"] = ' '
    button12["text"] = ' '
    button13["text"] = ' '
    button14["text"] = ' '
    button15["text"] = ' '
    button16["text"] = ' '
    button17["text"] = ' '
    button18["text"] = ' '
    button19["text"] = ' '
    button20["text"] = ' '
    button21["text"] = ' '
    button22["text"] = ' '
    button23["text"] = ' '
    button24["text"] = ' '
    button25["text"] = ' '


def btnClick(buttons, b_id, turn):
    if b_id == 27 or b_id == 28:
        if b_id == 27:
            reset()
        else:
            tk.destroy()
    elif buttons["text"] == " ":
        buttons["text"] = "X"
        b_id = b_id - 1
        x = math.floor(b_id / 5)
        y = b_id % 5

        board[x][y] = 'X'

        turn = game(board)
        if -1 == turn.row:
            return

        board[turn.row][turn.column] = 'O'

        checkWin(board, 'Computer')
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


label = Label(tk, text=" N.B : First turn : player X", font='Times 16 bold', fg='purple')
label.grid(row=1, column=0, columnspan=4)
label = Label(tk, text="", font='Times 20 bold', fg='purple')
label.grid(row=2, column=0, columnspan=4)

button1 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button1, 1, 1))
button1.grid(row=3, column=1)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button2, 2, 1))
button2.grid(row=3, column=2)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button3, 3, 1))
button3.grid(row=3, column=3)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button4, 4, 1))
button4.grid(row=3, column=4)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button5, 5, 1))
button5.grid(row=3, column=5)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button6, 6, 1))
button6.grid(row=4, column=1)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button7, 7, 1))
button7.grid(row=4, column=2)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button8, 8, 1))
button8.grid(row=4, column=3)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                 command=lambda: btnClick(button9, 9, 1))
button9.grid(row=4, column=4)

button10 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button10, 10, 1))
button10.grid(row=4, column=5)

button11 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button11, 11, 1))
button11.grid(row=5, column=1)

button12 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button12, 12, 1))
button12.grid(row=5, column=2)

button13 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button13, 13, 1))
button13.grid(row=5, column=3)

button14 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button14, 14, 1))
button14.grid(row=5, column=4)

button15 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button15, 15, 1))
button15.grid(row=5, column=5)

button16 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button16, 16, 1))
button16.grid(row=6, column=1)

button17 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button17, 17, 1))
button17.grid(row=6, column=2)

button18 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button18, 18, 1))
button18.grid(row=6, column=3)

button19 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button19, 19, 1))
button19.grid(row=6, column=4)

button20 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button20, 20, 1))
button20.grid(row=6, column=5)

button21 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button21, 21, 1))
button21.grid(row=7, column=1)

button22 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button22, 22, 1))
button22.grid(row=7, column=2)

button23 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button23, 23, 1))
button23.grid(row=7, column=3)

button24 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button24, 24, 1))
button24.grid(row=7, column=4)

button25 = Button(tk, text=' ', font='Times 20 bold', bg='spring green', fg='purple', height=box_h, width=box_w,
                  command=lambda: btnClick(button25, 25, 1))
button25.grid(row=7, column=5)

button26 = Button(tk, text='', font='Times 20 bold', bg='#F0F0F0', fg='#F0F0F0', height=box_h, width=box_w,
                  borderwidth=0)
button26.grid(row=9, column=0)
# play Again button?
button27 = Button(tk, text='Play Again?', font='Times 12 bold', bg='#E93ACB', fg='#FFFFFF', height=box_h,
                  width=box_w + 5, borderwidth=0, command=lambda: btnClick(button27, 27, 1))
button27.grid(row=1, column=3, columnspan=3)
# exit game button
button28 = Button(tk, text='Exit ?', font='Times 12 bold', bg='#E93ACB', fg='#FFFFFF', height=box_h,
                  width=box_w + 5, borderwidth=0, command=lambda: btnClick(button28, 28, 1))
button28.grid(row=1, column=5, columnspan=3)

button26.configure(state=DISABLED)


def setComputerTurn(x_id):
    if 1 == x_id:
        button1["text"] = "O"
    elif x_id == 2:
        button2["text"] = "O"
    elif 3 == x_id:
        button3["text"] = "O"
    elif 4 == x_id:
        button4["text"] = "O"
    elif 5 == x_id:
        button5["text"] = "O"
    elif 6 == x_id:
        button6["text"] = "O"
    elif x_id == 7:
        button7["text"] = "O"
    elif x_id == 8:
        button8["text"] = "O"
    elif x_id == 9:
        button9["text"] = "O"
    elif x_id == 10:
        button10["text"] = "O"
    elif x_id == 11:
        button11["text"] = "O"
    elif x_id == 12:
        button12["text"] = "O"
    elif x_id == 13:
        button13["text"] = "O"
    elif x_id == 14:
        button14["text"] = "O"
    elif x_id == 15:
        button15["text"] = "O"
    elif x_id == 16:
        button16["text"] = "O"
    elif x_id == 17:
        button17["text"] = "O"
    elif x_id == 18:
        button18["text"] = "O"
    elif x_id == 19:
        button19["text"] = "O"
    elif x_id == 20:
        button20["text"] = "O"
    elif x_id == 21:
        button21["text"] = "O"
    elif x_id == 22:
        button22["text"] = "O"
    elif x_id == 22:
        button22["text"] = "O"
    elif x_id == 23:
        button23["text"] = "O"
    elif x_id == 24:
        button24["text"] = "O"
    elif x_id == 25:
        button25["text"] = "O"
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe Computer ?", "Button already Clicked!")


def game(board_p):
    temp = pos(-1, -1)
    if checkWin(board_p, 'Player') == 1:
        return temp
    bestMove = findBestMove(board_p)
    x_id = bestMove.row * 5 + (bestMove.column + 1)
    setComputerTurn(x_id)
    return bestMove


tk.mainloop()
