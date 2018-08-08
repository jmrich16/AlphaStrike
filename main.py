import sqlite3
import sys
import Data_Retrieval


print("Welcome to AlphaStrike...Alpha")
print("Select option")
print("1.Insert new unit")
print("2.Unit battle")


def optionrouter(selectionvalue):
    if selectionvalue == 1:
        Data_Retrieval.rowentry()

    if selectionvalue == 2:
        print("I got nothing for ya")

while True:
    value = input()
    try:
        value = int(value)
    except (TypeError, ValueError):
        print("Please enter a valid integer")
        continue
    if value >= 0 and value <= 2:
        break
    else:
        print("Please only select a valid option number")

print("You have selected option " + str(value))





optionrouter(value)




