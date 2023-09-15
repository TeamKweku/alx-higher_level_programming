#!/usr/bin/python3
""" a python script that select all cities from the database """


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <username> <password> <database> <state>")

    username, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", db=database, port=3306, user=username, passwd=passwd
    )

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor = db.cursor()
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    city_names_str = ", ".join(city_names)

    print(city_names_str)

    cursor.close()
    db.close()
