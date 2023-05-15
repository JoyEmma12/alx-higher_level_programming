#!/usr/bin/python3
"""
Script that takes in arguements and displays arguements
where name matches the arguement
and is safe from MySQL arguements
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    safe from MySQL arguements
    """
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
