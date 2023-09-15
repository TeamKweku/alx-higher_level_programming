#!/usr/bin/python3
""" a python script that select all cities from the database """


if __name__ == "__main__":
    import MySQLdb
    import sys

    username, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", db=database, port=3306, user=username, passwd=passwd
    )

    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
