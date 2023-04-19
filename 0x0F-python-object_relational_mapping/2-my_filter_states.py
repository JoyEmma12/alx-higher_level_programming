#!/usr/bin/python3

"""
Scripts that takes in an arguement
and displays all values.
"""

import sys
import MySQLdb

if __name__ == '__main__':
       """
       Display all values in the states
       table of the database
       """
       us = sys.argv[1]
       pss = sys.argv[2]
       db = sys.argv[3]

       db = MySQLdb.connect(host='localhost', port=3306, user=us, password=pss, database=db)

       cur = db.cursor()
       cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
       rows = cur.fetchall()

       for row in rows:
           print(row)
