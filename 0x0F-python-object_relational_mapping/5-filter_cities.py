#!/usr/bin/python3
"""Database"""

import sys

import MySQLdb

if __name__ == "__main__":
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]
    STATE = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=USERNAME,
                         passwd=PASSWORD, db=DB_NAME)
    cur = db.cursor()
    cur.execute(
        'SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id WHERE states.name = %s',
        (STATE,))

    for i, row in enumerate(cur.fetchall()):
        if i != 0:
            print(f', {row[0]}', end="")
        else:
            print(row[0], end="")

    print()
