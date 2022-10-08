print(" ╭∩╮( ͡⚆ ͜ʖ ͡⚆)╭∩╮ Welcome to EFT Scav money tracker.╭∩╮( ͡⚆ ͜ʖ ͡⚆)╭∩╮ ")

def view():
    given_file = open("C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt","r")
    numbers = []
    for number in given_file:
        numbers.append(int(number))
        total = sum(numbers)
        length = len(numbers)
        avy = total / length
    print(" Roubles made:" , f'{total:,}' "\n Average per run:", f'{avy:,}')


def add():
    rubles = input("Enter amount of rubles made: ")
    with open('C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt', 'a') as f:
        f.write(rubles + "\n")
def reset():
    file = open("C:/Users/Shane/Downloads/eft_scav_profit/eft_scav_profit.txt","a")
    file.truncate(0)
    file.close()



while True:
    mode=input("ENTER 'add' to add the amount you made that scav run. \nENTER 'view' to see the average and the amount you made: ")
    if mode== "q":
        break

    if mode== "view":
        view()
    elif mode=="add":
        add()
    elif mode== "reset":
        reset()
    else:
        print("Invalid mode")
        continue
