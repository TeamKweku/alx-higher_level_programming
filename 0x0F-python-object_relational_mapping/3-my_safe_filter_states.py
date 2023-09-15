#!/usr/bin/python3
""" a python script to select all states from a mysql database """


if __name__ == "__main__":
    import MySQLdb
    import sys

    username, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", db=database, port=3306, user=username, passwd=passwd
    )

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    cursor = db.cursor()
    cursor.execute(query, (name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
