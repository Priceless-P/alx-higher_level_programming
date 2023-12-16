#!/usr/bin/python3
"""Lists all cities of a state
from the database hbtn_0e_0_usa."""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    state_name = MySQLdb.escape_string(sys.argv[4]).decode()
    c.execute("""SELECT cities.name FROM cities JOIN states ON
                states.id = cities.state_id
                WHERE states.name
                = '{}' ORDER BY cities.id""".format(state_name))
    cities = c.fetchall()
    for city in range(len(cities)):
        if (city != len(cities) - 1):
            print(cities[city][0] + ", ", end="")
        else:
            print(cities[city][0], end="")
    print()
    c.close()
    db.close()
