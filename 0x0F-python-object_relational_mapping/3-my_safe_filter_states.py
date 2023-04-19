#!/usr/bin/python3
"""
This script takes in arguements
and displays all values in the
states table of the database.

Script that is safe from MySQL
injections.
"""
if __name__ == '__main__':
    """
    Access the database and get states
    from the database.
    """

    db = MySQLbd.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    with db.cursor as mycur:
        mycur.execute("""
			SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY states.id ASC""", {'name': argv[4]})

	rows = mycur.fetchall()

      if rows is not None:
          for row in rows:
	      print(row)
