#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__' :
    use = sys.argv[1]
    pss = sys.argv[2]
    databse = sys.argv[3]

    db = MySQLdb.connect(host = 'localhost',
                         user = use,
                         password = pss,
                         db = databse,
                         port = 3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
