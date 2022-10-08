from tkinter import *
import tkinter as tk


root = tk.Tk()
root.configure(bg='#475763')
root.title("EFT Scav profit Calculator")
root.iconbitmap('D:\Shane\Pictures\EscapeFromTarkov.ico')
root.geometry("1200x600")

bg = PhotoImage(file="D:\Shane\Pictures\Escape-From-Tarkov.gif")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)



def view():
    given_file = open("C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt","r")
    numbers = []
    for number in given_file:
        numbers.append(int(number))
        total = sum(numbers)
        length = len(numbers)
        avy = total / length
        rub_info = tk.Label(root,text="Total rubles made:₽ " f'{total:,}'"\nAverage Rubles per run:₽ " f'{avy:,}',height=2,width=30, font=("Arial", 20),bg='#887e5b')
        rub_info.grid(row= 2 ,column= 0)

def add():
    rubles = rub_input.get()
    with open('C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt', 'a') as f:
        f.write(rubles + "\n")

def reset():
    file = open("C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt","a")
    file.truncate(0)
    file.close()

greeting = tk.Label(text="Welcome to EFT Scav Calculator", font=("Arial", 24),bg='#887e5b')
greeting.grid(row= 0 ,column= 1, columnspan=1)

text_info = tk.Label(root, height=2,width=15,text="Rubles made:", font=("Arial", 18),bg='#887e5b')
text_info.grid(row= 1 ,column= 0)




rub_input = tk.Entry(root,font=("Arial", 25))
rub_input.grid(row= 1 ,column= 1, columnspan=2,padx=5, pady=5, ipadx=5, ipady=5)

view_button = tk.Button(root,text="View",font=("Arial", 15),
command = view
)
view_button.grid(row= 2 ,column= 2)

button = tk.Button(root,text="ADD",font=("Arial", 15),
command = add
)
button.grid(row= 1 ,column= 2)

reset_button = tk.Button(root,text="Reset",font=("Arial", 15),
command = reset
)
reset_button.grid(row= 3 ,column= 2)

root.mainloop()
