#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Get MySQL credentials from command line argument"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Connect to the MySQL server """
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
            )
    """Create a cursor to interacrt with the database"""
    cursor = db.cursor()

    """Execute the SQL query to select cities along with their state name"""
    query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states ON cities.state_id=states.id "
            "ORDER BY cities.id ASC"
            )
    cursor.execute(query)

    """Fetch and display the results"""
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
