#!/usr/bin/python3

"""
Scripts that list all states
with a name starting with N
from the database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Get the states from the database.
    """

    use = sys.argv[1]
    pss = sys.argv[2]
    databse = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=use, password=pss, db=databse, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
		    WHERE name LIKE BINARY 'n%' \
		    ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
              print(row)
