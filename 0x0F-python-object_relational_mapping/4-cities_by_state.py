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
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id")

    for row in cur.fetchall():
        print(row)
