#!/usr/bin/python3
"""
Get the cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv
import sys

if __name__ == '__main__':
    """
    Get the states from the database by accessing it.
    """
    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = conn.cursor()

    query = """ SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC """

    cur.execute(query, (sys.argv[4],))
    rows_selected = cur.fetchall()

    for row in rows_selected:
        print(row)

    cur.close()
    conn.close()
