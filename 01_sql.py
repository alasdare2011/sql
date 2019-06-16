#Create a Sqlite database and table

#import the sqlite3 library
import sqlite3

#create a new database if the database not already exists
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create the table
cursor.execute("""CREATE TABLE population
                  (city TEXT, state TEXT, population INT)
                   """)

conn.close()