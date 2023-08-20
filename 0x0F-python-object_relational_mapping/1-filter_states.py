#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Get MySQL credentials from command line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Connect to the MySQL server """
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
            )

    """Create a cursor to interact with the database """
    cursor = db.cursor()

    """ Execute the SQL query to select states with names starting with 'N'"""

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    """ Fetch and display the results """
    results = cursor.fetchall()
    for row in results:
        print(row)

    """ Clean up and close the db connection """
    cursor.close()
    db.close()
