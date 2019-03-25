from Connector import DBConnection




class DBHandler:

    def __init__(self):
        self.conn = DBConnection().getConnection()
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()

    def getData(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.conn.close()
        return data

    def setData(self, query):

        # execute SQL query using execute() method.
        self.cursor.execute(query)
        # Commit your changes in the database.
        self.conn.commit()
        # disconnect from server
        self.conn.close()





