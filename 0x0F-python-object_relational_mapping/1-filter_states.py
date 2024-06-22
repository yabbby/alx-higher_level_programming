#!/usr/bin/python3
"""Database"""

import sys

import MySQLdb

if __name__ == "__main__":
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=USERNAME,
                         passwd=PASSWORD, db=DB_NAME)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE states.name LIKE "N%"')

    for row in cur.fetchall():
        print(row)
