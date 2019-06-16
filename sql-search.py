# Asks user what aggregation they would like performed on the data

import sqlite3

conn = sqlite3.connect("newnum.db")

# create the cursor object used to execute the SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

#loop until valid operation entered

while  True:
    #get user input
    x = input(prompt)

    #if user enters any choice from 1 - 4
    if x in set(["1", "2", "3", "4"]):
        #parse the corresponding operation text
        operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(x)]

        #retrieve data
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        #fetchone() retrieves one record from the query
        get = cursor.fetchone()

        #output results to screen
        print(operation + ": %f" % get[0])

    # if user enters 5
    elif x == "5":
        print("Exit")
        break