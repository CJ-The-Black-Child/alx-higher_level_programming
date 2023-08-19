#!/usr/bin/python3
"""
Script that taskes in an argument and displays all values in the states table
of hbtn_0e_usa where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":

    """ Get MySQL credentials and state name from command line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to the MySQL server"""
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
            )
    """ Create a cursor to interact with the db """
    cursor = db.cursor()

    """ Create the SQL using format and user input """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    """ Fetch and display the results """
    results = cursor.fetchall()
    for row in results:
        print(row)

    """ Clean up and close the database connection """
    cursor.close()
    db.close()
