#!/usr/bin/python3
"""
Script that takes the name of state as an arguement
list all the cities of the states
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Takes in 4 arguement and its MySQL injection free
    """
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s`
                ON `c`.`state_id`= `s`.`id`)
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
