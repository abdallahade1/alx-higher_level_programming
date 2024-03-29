#!/usr/bin/python3
"""
Get the states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Get the states from the database by accessing it.
    """
    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")

    rows_selected = cur.fetchall()

    for row in rows_selected:
        print(row)

    cur.close()
    conn.close()
