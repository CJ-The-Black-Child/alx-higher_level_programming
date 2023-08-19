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
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ',')
        FROM cities
        JOIN states ON cities.state_id=states.id
        WHERE states.name = %s
        """
    )
    cursor.execute(query, (state_name,))

    """ Fetch and display the results """
    result = cursor.fetchone()[0]
    if result:
        print(result)

    cursor.close()
    db.close()
