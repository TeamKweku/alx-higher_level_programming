#!/usr/bin/python3
""" a python script to select all states from a mysql database """
import MySQLdb
import sys

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

connection = MySQLdb.connect(
    host="localhost", db=database, port=3306, user=username, passwd=password
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
