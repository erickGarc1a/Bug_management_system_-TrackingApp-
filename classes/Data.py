import mysql.connector
from mysql.connector.errors import Error


class Data:

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="Aspire123")
            print("Connection success")
        except mysql.connector.errors.ProgrammingError:
            print("Connection Error")
            self.mydb = None

    def set_connect(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="Aspire123")
            print("Connection success")
        except mysql.connector.errors.ProgrammingError:
            print("Connection Error")
            self.mydb = None

    def get_connect(self):
        return self.mydb

    def send_query(self, sql):
        try:
            my_cursor = self.mydb.cursor(dictionary=True)
            try:
                my_cursor.execute(sql)
            except Error as e:
                print("Something went wrong: {}".format(e))
            finally:
                result = my_cursor.fetchall()
                my_cursor.close()
                if len(result) > 0:
                    return result
                return None
        except Error as e:
            print("Something went wrong: {}".format(e))

    def check_database(self):
        try:
            my_cursor = self.mydb.cursor()
            try:
                my_cursor.execute("SELECT SCHEMA_NAME "
                                  "FROM INFORMATION_SCHEMA.SCHEMATA "
                                  "WHERE SCHEMA_NAME = 'BugManagement'")
                if len(my_cursor.fetchall()) == 0:
                    print("Database doesnt exists, creating Database BugManagement")
                    my_cursor.execute("CREATE DATABASE BugManagement")
                my_cursor.execute("USE BugManagement")
                my_cursor.execute("SHOW TABLES LIKE 'Bugs';")
                if len(my_cursor.fetchall()) == 0:
                    my_cursor.execute("CREATE TABLE Bugs (title varchar(100) primary key, "
                                      "project varchar(100) not null, btype varchar(20) , "
                                      "priority int, status varchar(100), author varchar(100), "
                                      "_date_ date)")
                my_cursor.execute("SHOW TABLES LIKE 'Users';")
                if len(my_cursor.fetchall()) == 0:
                    my_cursor.execute("CREATE TABLE Users (name varchar(100) not null, password varchar(100) not null, "
                                      "email varchar(100), phone varchar(10), id_user int primary key, admin boolean)")
            except Error as e:
                print("Something went wrong: {}".format(e))
            finally:
                my_cursor.close()
        except Error as e:
            print("Something went wrong: {}".format(e))

    def close_connect(self):
        try:
            self.mydb.close()
            print("Closing connection with database")
        except Error:
            print("No connection")
