#!/usr/bin/python3
"""
Get states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Get states from the database by accessing it"""

    con = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states")

    selected_rows = cur.fetchall()

    for rows in selected_rows:
        print(rows)
