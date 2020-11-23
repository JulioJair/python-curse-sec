from os import environ
import sqlite3
from sqlite3 import Error


class SQLite_controller:
    def __init__(self, db_name: str, password: str, *models):
        """Constructor method

        :param password: Password
        :param db_name: DATABASE Name
        :param models: DATABASE models
        """
        self.db_name = db_name
        self.__password = password
        self.__create_connection(db_name, password, *models)

    def __create_connection(self, db_name: str, password: str, *models):
        """ create a database connection to a SQLite database

        :param password: Password
        :param host: Host or domain
        :param db_name: DATABASE Name
        :param models: DATABASE models
        """
        import os
        def file_exists(file_name: str):

            """ Verificar si es un archivo y si este existe """
            return os.path.isfile(file_name)

        conn = None
        # Droping database MYDATABASE if already exists.
        try:
            if file_exists(db_name):
                os.remove(db_name)

            """ create a database connection to a SQLite database if not exist create a db"""
            conn = sqlite3.connect(db_name)

            self.__create_tables(conn, *models)

            print(sqlite3.version)
        except Error as e:
            raise e
        finally:
            if conn:
                # Closing the connection
                conn.close()

    @staticmethod
    def __create_tables(conn, *models):
        """Create Tables in DB

        :param conn: Connection object
        :param models: table definition
        """
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        try:
            for model in models:
                tb_name = list(model.keys())[0]
                table_sql = f"""CREATE TABLE IF NOT EXISTS {tb_name}(
                    id integer PRIMARY KEY"""
                for field_name, field_type in model[tb_name].items():
                    table_sql = table_sql + f", {field_name} {field_type}"
                try:
                    cursor.execute(table_sql + ")")
                except Error as err:
                    raise err
        except Error as e:
            raise e

    def run_query(self, query: str, parameter=()):
        """Run SQL statement

        :param query: SQL statement
        :type query: str
        :param parameter: SQL statement parameters
        """
        conn = sqlite3.connect(self.db_name)

        try:
            cursor = conn.cursor()
            cursor.execute(query, parameter)
            result = None
            if parameter:
                conn.commit()
            else:
                result = cursor.fetchall()
            return result
        except Error as e:
            raise e
        finally:
            conn.close()


if __name__ == '__main__':
    # create_connection(r"sqlite_example.db")

    # * Table definition
    text_table = {
        "text": {
            "title": "text",
            "content": "text"}}

    # * Create database
    # db_password = environ["contraseña"]
    db_password = "contraseña"
    notes_db = SQLite_controller("sqlite_file.db", db_password, text_table)

    # * Insert value in text table
    QUERY = "INSERT INTO text (title,content) VALUES (?, ?)"
    values = ("my first text", "its note in sqlite")
    notes_db.run_query(QUERY, values)

    # * Query to text table
    QUERY = "SELECT * FROM text"
    print(notes_db.run_query(QUERY))
