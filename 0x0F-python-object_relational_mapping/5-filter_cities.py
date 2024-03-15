#!/usr/bin/python3
"""
the script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    password=sys.argv[2],
    database=sys.argv[3])
cursor = connection.cursor()
query = """
SELECT cities.name FROM cities
LEFT JOIN states ON states.id = cities.state_id
WHERE states.name = %s
ORDER BY cities.id ASC
"""
cursor.execute(query, (sys.argv[4],))
results = cursor.fetchall()
for i, row in enumerate(results):
    print('{}'.format(row[0]), end='')
    if i != len(results) - 1:
        print(', ', end='')
    else:
        print()
cursor.close()
connection.close()
