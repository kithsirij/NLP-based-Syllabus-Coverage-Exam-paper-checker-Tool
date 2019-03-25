import MySQLdb

class DBConnection:

    db = ""

    # Open database connection

    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')


    # Return DB Connection

    def getConnection(self):
        return self.db

