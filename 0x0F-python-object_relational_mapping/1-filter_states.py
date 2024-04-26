#!/usr/bin/python3
"""
the script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) > 3:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
        cursor = connection.cursor()
        cursor.execute("""
        SELECT id, name from states WHERE name LIKE 'N%' ORDER BY id ASC
        """)
        results = cursor.fetchall()
        for row in results:
            if row[1][0] == "N":
                print(row)
        cursor.close()
        connection.close()
