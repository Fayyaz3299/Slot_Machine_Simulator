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
