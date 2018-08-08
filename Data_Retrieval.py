import sqlite3

conn = sqlite3.connect('modelstats.db')
c = conn.cursor()

t = ('Daemons')
# c.execute('SELECT * FROM model_stats WHERE Faction=?', t)
# #c.execute('SELECT * FROM model_stats')
# print(c.fetchone())

if False:
    c.execute('''CREATE TABLE model_stats(
                    ModelName varchar(255),
                    ModelPoints int,
                    Move int,
                    WS int,
                    BS int,
                    Strength int,
                    Toughness int,
                    Wounds int,
                    Attacks int,
                    Leadership int,
                    Faction varchar(255)
                    )''')

def sanitized_input(prompt,validation_type,user_entry):

    input_to_check = user_entry
    while True:
        if validation_type == "string":
            print(prompt)







def rowentry():
    print("Row entry process started")
    rowentrylist = ['Model Points', 'Movement Value', 'Weapon Skill(WS)', 'Ballistic Skill(BS)', 'Strength', 'Toughness'
        , 'Wounds', 'Attacks', 'Leadership', 'ModelName', 'Faction']
    selectionCount = 0
    rowentryinputlist = []
    #list length will be from 0-9 for int, 10 and 11 for str
    print("Entering entry loop")
    doContinue = True
    while doContinue:

        print("Please input " + rowentrylist[selectionCount] + " and press enter to continue")
        stat_input = input()
        rowentryinputlist.append(stat_input)
        print(len(rowentryinputlist))
        selectionCount += 1
        if len(rowentryinputlist) == 11:

            prompt_on = True
            while prompt_on:
                print(rowentryinputlist)
                print("Does this look correct? Please press y for yes or n for no to restart")

                choice = input()
                choice = choice.lower()
                if choice == "y" or choice == "n":
                    print("correct block")
                    doContinue = False
                    break
                else:
                    "input not valid, Please input y or n"
                    continue




