import sqlite3
from sqlite3 import Error
import logging

# Create and configure logger
LOG_FORMAT = "%(levelname)s - %(message)s"
logging.basicConfig(filename="logger.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()


class SQLite_controller:
    def __init__(self, db_name: str, *models):
        """Constructor method

        :param db_name: DATABASE Name
        :param models: DATABASE models
        """
        self.db_name = db_name
        self.__create_connection(db_name, *models)

        logger.info("Object initialized correctly")

    def __create_connection(self, db_name: str, *models):
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
                logger.warning(f"Database '{db_name}' already exist. Dropping..")
                os.remove(db_name)
                logger.debug(f"'{db_name} Dropped")

            """ create a database connection to a SQLite database if not exist create a db"""
            conn = sqlite3.connect(db_name)

            self.__create_tables(conn, *models)
            logger.info(f"DB {self.db_name} Initialized with sqlite {sqlite3.version}")

        except Error as e:
            logger.error(f"Error creating the connection with DB engine {e}")
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

        logger.debug(f"Creating new table")
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
                    logger.error(f"Can't create table {tb_name}")
                    raise err
        except Error as e:
            raise e

    def __run_query(self, query: str, parameter=()):
        logger.debug(f"Attempt to execute SQL statement {query, parameter}")
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
            logger.info(f"Succesful SQL QUERY")
            return result
        except Error as e:
            logger.error(f"{e}")
            raise e
        finally:
            conn.close()

    def get_all(self, table):
        QUERY = f"SELECT * FROM {table}"
        result = self.__run_query(QUERY)
        return result

    def get_by_id(self, table, id):
        QUERY = f"SELECT * FROM {table} WHERE id = {id}"
        result = self.__run_query(QUERY)
        return result

    def get_by_name(self, table, column, value):
        QUERY = f"SELECT * FROM {table} WHERE {column} LIKE '{value}'"
        result = self.__run_query(QUERY)
        return result

    def insert(self, table, values):
        QUERY = f"INSERT INTO {table} VALUES (NULL, ?, ?)"
        result = self.__run_query(QUERY, values)
        return result

    def insert_3(self, table, values):
        QUERY = f"INSERT INTO {table} VALUES (NULL, ?, ?, ?)"
        result = self.__run_query(QUERY, values)
        return result

    def update_by_name(self, table, set_col, new_value, where_col, actual_value):
        QUERY = f"UPDATE {table} SET {set_col} = '{new_value}' WHERE {where_col} LIKE '{actual_value}'"
        result = self.__run_query(QUERY)
        return result


if __name__ == '__main__':
    # create_connection(r"sqlite_example.db")

    # * Table definition
    text_table = {
        "text": {
            "title": "text",
            "content": "text"}}

    # * Create database
    notes_db = SQLite_controller("sqlite_file.db", text_table)

    # * Insert value in text table
    QUERY = "INSERT INTO text (title,content) VALUES (?, ?)"
    values = ("my first text", "its note in sqlite")
    notes_db._SQLite_controller__run_query(QUERY, values)

    # * Query to text table
    QUERY = "SELECT * FROM text"

    print(notes_db._SQLite_controller__run_query(QUERY))

    # Another table def
    text_table = {
        "contacts": {
            "name": "text",
            "telephone_number": "integer"}}

    print(notes_db.get_all('text'))
    notes_db.insert('text', ('second note', 'this is another text'))
    notes_db.insert('text', ('third note', 'what about a new one?'))
    print(notes_db.get_by_id('text', 2))
    print(notes_db.get_all('text'))
