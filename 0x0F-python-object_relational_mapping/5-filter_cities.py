#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Get MySQL credentials and state name from command line argument """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to the MYSQL server """
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
            )

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """Execute the SQL query to select cities of the given state"""
    query = (
        """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id=states.id
        WHERE states.name = %s
        ORDER by cities.id ASC
        """
    )
    cursor.execute(query, (state_name,))

    """ Fetch and display the results """
    results = cursor.fetchall()
    for row in results:
        print(row[1])

    cursor.close()
    db.close()
