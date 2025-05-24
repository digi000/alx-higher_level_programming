#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb, sys
    conn = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host="localhost",
            port=3306
            )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    for row in cursor.fetchall():
        print(row)
