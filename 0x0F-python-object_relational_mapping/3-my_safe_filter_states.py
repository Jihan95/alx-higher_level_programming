#!/usr/bin/python3
"""
the script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])
    cursor = connection.cursor()
    query = "SELECT id, name FROM states WHERE name = %s"
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
