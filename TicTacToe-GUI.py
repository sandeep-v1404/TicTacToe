from tkinter import *
import sys

player = 'x'
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

tk = Tk()                                                              

label1 = Label(tk, text='Tic-Tac-Toe')                               
label1.pack()

canvas2 = Canvas(tk, width=300, height=300)                    
canvas2.pack()
canvas2.create_line(100,0,100,300)
canvas2.create_line(200,0,200,300)
canvas2.create_line(0,100,300,100)
canvas2.create_line(0,200,300,200)

def drawxo(x,y,row,col):                                        
    """draw x or o on the canvas"""
    global player
    global board
    l=40
    if player == 'x':
        canvas2.create_line(x-l,y-l, x+l,y+l)
        canvas2.create_line(x+l,y-l, x-l,y+l)
        player = 'o'
        label3.config(text='player o')
        board[row][col] = 'x'
    elif player == 'o':
        canvas2.create_line(x,y-l,x+l,y, x+l,y,x,y+l, x,y+l,x-l,y, x-l,y,x,y-l)
        player = 'x'
        label3.config(text='player x')
        board[row][col] = 'o'

def placexo(event):
    """place x or o on the board"""
    if won==0:
        global board
        if event.x<100 and event.y<100:
            if board[0][0]==' ': drawxo(50,50,0,0)
        if 100<event.x<200 and event.y<100:
            if board[0][1]==' ': drawxo(150,50,0,1)
        if 200<event.x<300 and event.y<100:
            if board[0][2]==' ': drawxo(250,50,0,2)
        if event.x<100 and 100<event.y<200:
            if board[1][0]==' ': drawxo(50,150,1,0)
        if 100<event.x<200 and 100<event.y<200:
            if board[1][1]==' ': drawxo(150,150,1,1)
        if 200<event.x<300 and 100<event.y<200:
            if board[1][2]==' ': drawxo(250,150,1,2)
        if event.x<100 and 200<event.y<300:
            if board[2][0]==' ': drawxo(50,250,2,0)
        if 100<event.x<200 and 200<event.y<300:
            if board[2][1]==' ': drawxo(150,250,2,1)
        if 200<event.x<300 and 200<event.y<300:
            if board[2][2]==' ': drawxo(250,250,2,2)
    
canvas2.bind_all('<Button-1>',placexo)                                

label3 = Label(tk, text='player x')                                         
label3.pack()

def close(): 
    tk.destroy()
    sys.exit()
    
closebutton4 = Button(tk, text='exit', command=close)
closebutton4.pack()



def win():
    """check if a player has won"""
    if board[0][0]==board[0][1]==board[0][2]:
        return board[0][0]
    elif board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    elif board[2][0]==board[2][1]==board[2][2]:
        return board[2][0]
    elif board[0][0]==board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    elif board[0][2]==board[1][2]==board[2][2]:
        return board[0][2]
    elif board[0][0]==board[1][1]==board[2][2]:
        return board[1][1]
    elif board[0][2]==board[1][1]==board[2][0]:
        return board[1][1]


won=0
while won==0:
    tk.update()
    if win()=='x' or win()=='o':
        print ('player ',win(),' WINS !!!')
        label3.config(text='Player '+win().upper()+' won...!!!')
        won=1
        zzz=input()
