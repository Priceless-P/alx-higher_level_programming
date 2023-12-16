#!/usr/bin/python3
"""Lists all cities of a state
from the database hbtn_0e_0_usa."""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    c.execute(query, (sys.argv[4],))

    result = c.fetchall()
    cities = ', '.join([city[0] for city in result])

    print(cities)
    c.close()
    db.close()
