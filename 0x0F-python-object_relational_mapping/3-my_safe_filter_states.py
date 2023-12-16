#!/usr/bin/python3
"""Lists all states where name matches the argument
(from the database hbtn_0e_0_usa.
Safe from SQL injection"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = """
    SELECT * FROM states
    WHERE name = %s
    ORDER BY id ASC
    """

    c.execute(query, (sys.argv[4],))
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
