#!/usr/bin/python3
"""2. Filter states by user input"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(
            user=argv[1],
            password=argv[2],
            database=argv[3],
            host="localhost",
            port=3306
            )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name= '{}' ORDER BY states.id".format(argv[4]))
    for row in cursor.fetchall():
        print(row)
