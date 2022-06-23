import mysql.connector


class Data:

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="Death_One21")
            print("Connection success")
        except mysql.connector.errors.ProgrammingError:
            print("Connection Error")
            self.mydb = 0
    
    def check_database(self):
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute("SELECT SCHEMA_NAME "
                                "FROM INFORMATION_SCHEMA.SCHEMATA "
                                "WHERE SCHEMA_NAME = 'BugManagement'")
            if len(mycursor.fetchall()) == 0:
                print("Database doesnt exists")
            mycursor.close
        except AttributeError:
            print("No connection")
    
    def close_connect(self):
        try:
            self.mydb.close()
            print("Closing connection with database")
        except AttributeError:
            print("No connection")
    
data = Data()

data.check_database()
data.close_connect()