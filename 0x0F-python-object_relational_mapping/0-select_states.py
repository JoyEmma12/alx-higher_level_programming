#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':

    us = sys.argv[1]
    ps = sys.argv[2]
    dbe = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=us,
                         passwrd=ps,
                         db=dbe,
                         port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')

    rows = cursor.fetchall()

    for row in rows:
        print(row)   
