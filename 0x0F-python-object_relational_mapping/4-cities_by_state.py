#!/usr/bin/python3
"""
Script that lists all cities from the database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    It takes 3 arguements
    """
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.states_id = states.id ORDER BY cities.id ASC")
    [print(cities) for cities in cur.fetchall()]
