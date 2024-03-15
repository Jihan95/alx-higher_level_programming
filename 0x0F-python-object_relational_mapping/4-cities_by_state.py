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
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC
"""
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()
connection.close()
