import tkinter
from  tkinter import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Sudoku Solver')
    # setting the diamentions
    window.geometry("324x550")

    label = Label(window, text ='Fill in the number and click solve').grid(row=0, column=1, columnspan=10)

    errLabel = Label(window, text="", fg='red')
    errLabel.grid(row=15, column=1, columnspan=10, pady=5)

    solvedLabel = Label(window, text="", fg='green')
    solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

    cells = {}

# https://www.youtube.com/watch?v=xAXmfZmC2SI

def validateNumber(P):
    out = (P.isdigit() or P == '') and len(P) < 2
    return out

reg = window.register(validateNumber)


def draw3x3Grid(row, column, bgColor):
    for i in range(3):
        for j in range(3):
            e = Entry(window, width=5, bg=bgColor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row = row + i + 1, column=column + j + 1, sticky="nsew", pady=1, padx=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e

def draw9x9Grid():
    color = '#D0ffff'
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == '#D0ffff':
                color = '#ffffd0'
            else:
                color = '#D0ffff'

def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

def getValue():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(1, 10):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == '':
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)

btn = Button(window, command=getValue, text = "Solve", width = 10)
btn.grid(row = 20, column = 1, columnspan=  5, pady = 20 )

btn = Button(window, command=clearValues, text = "Clear", width = 10)
btn.grid(row = 20, column = 5, columnspan=  5, pady = 20 )

draw9x9Grid()
window.mainloop()

