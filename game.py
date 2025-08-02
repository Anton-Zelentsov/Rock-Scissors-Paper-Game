from tkinter import *
from random import *

root = Tk()
root.title('Камень Ножницы бумага')
root.geometry('600x400')
root.resizable(width = False, height = False)
root['background'] = 'black'

def rock_scissors_paper():
    rsp = ['Камень', 'Ножницы', 'Бумага']
    value = choice(rsp)
    lable_text.configure(text = value)
lable_text = Label(root, text = '', fg = 'white', font =('Comic Sans MS', 20), bg = 'black')
lable_text.place(y = 200, x = 200)

rock = Button(root, text = 'Камень', font = ('Comic Sans MS', 20), bg = 'white', command = rock_scissors_paper)
rock.place(x = 50, y = 300)

scissors = Button(root, text = 'Ножницы', font = ('Comic Sans MS', 20), bg = 'white', command = rock_scissors_paper)
scissors.place(x = 220, y = 300)

paper = Button(root, text = 'Бумага', font = ('Comic Sans MS', 20), bg = 'white', command = rock_scissors_paper)
paper.place(x = 420, y = 300)

root.mainloop()