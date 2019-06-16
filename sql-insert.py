# Create a new database and insert 100 random numbers into it

import sqlite3
import random

# Establish connection and create new database newnum.db
with sqlite3.connect("newnum.db") as connection:

    #open cursor
    c = connection.cursor()

    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")

    #insert 100 random numbers into numbers table

    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))
