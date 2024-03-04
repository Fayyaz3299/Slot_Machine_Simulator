# Purpose of the Program is to create a Slot machine to take in a deposit amount and ask the user to bet on a spin of the slot machine
# They choose the number of lines (MAX ROWS Columns set through Global Variables ) ranging from 1 line to MAX number of lines present in the slot machine.
# The is the number of lines = x, then the program will only check the top x rows for matches
# Then they select the amount they want to bet on each line
# Total bet = (Bet amount * number of lines)
# It then runs the machine to generate the output ROWS X COLUMNS GRID
# Each character on the GRID (Set in the list symbol_count) will have a value associated to it, based on the probability of that symbol occuring (set in symbol_value)
# After completing this winnings and remaining balances are calculated
# Win = Having a complete row with all same characters
# Winning on one line  = (Value of the symbol in the winning row set in symbol_value) * (number of columns set) Eg : if the winning row is $$$ (we check the value of $ in symbol_value and multiple that by 3 since there are 3 entries hence 3 columns) 
# total_Winnings will be sum of each winning line
# Remaining balance = Present Balance - total_bet + total_Winnings 
# If the user has balance remaining they can repeat the process and continue or end
# If the user has balance less than Minimum_bet value the program will end
 

import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2

ROWS = 3
COLS = 3

symbol_count = {
    "$": 2,
    "%": 4,
    "#": 6,
    "@": 8
}

symbol_value = {
    "$":5,
    "%":4,
    "#":3,
    "@":2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winnings += values[symbol] *bet
            winning_lines.append(line +1)

    return winnings, winning_lines


def get_slot_machine_spin(rows,cols,symbols):
     all_symbols=[]
     for symbol, symbol_count in symbols.items():
         for _ in range(symbol_count):
             all_symbols.append(symbol)

     columns = []
     for _ in range(cols):
         column =[]
         current_symbols = all_symbols[:]
         for _ in range(rows):
             value = random.choice(current_symbols)
             current_symbols.remove(value)
             column.append(value)
         columns.append(column)

     return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
             print(column[row], end="|")
            else:
                print(column[row], end="")

        print()


def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to be on (1-" + str(MAX_LINES) + "): " ) 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines

def spin(balance):
    lines = get_number_of_lines()
    while True:
       bet = get_bet()
       total_bet = bet * lines

       if (total_bet > balance):
           print(f"You have a balance of ${balance}, you cannot bet more than that.")
       else:
           break
    remaining = balance - total_bet   
    print(f" You are betting ${bet} on each line, Number of lines betting on: {lines} Total bet = ${total_bet}, Total remaining balance= ${remaining}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print (f" You have won ${winnings}")
    print (f" You have won on lines :",*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit() 
    while True:
        print(f"Current balance is balance is ${balance}")
        answer = input("Press enter to play (q to quit):")
        if answer == "q":
            break
        balance += spin(balance)
        if balance < MIN_BET:
             print (f"Minimum bet is ${MIN_BET}. You have only ${balance}. Unfortunately you have to quit." )
             break

    print (f"You left with ${balance}." )

main()      