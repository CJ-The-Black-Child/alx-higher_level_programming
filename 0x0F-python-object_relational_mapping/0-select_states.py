#!/usr/bin/env python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Get the arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Connect to the MySQL server """
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database
            )
    cursor = db.cursor()

    """ Execute the query to fetch states """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch and print the results """
    results = cursor.fetchall()
    for row in results:
        print(row)

    """ Close the database connection """
    cursor.close()
    db.close()
