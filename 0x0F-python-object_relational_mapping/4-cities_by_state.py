#!/usr/bin/python3
"""Lists all cities
(from the database hbtn_0e_0_usa.)"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
                FROM states JOIN cities ON
                states.id=cities.states_id ORDER BY cities.id ASC""")
    states = c.fetchall()
    for state in states:
        print(state)
    db.close()
