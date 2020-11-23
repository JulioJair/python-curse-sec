import sqlite3
from sqlite3 import Error


class SQLite_controller:
    def __init__(self, user: str, password: str, host: str, db_name: str, *models):
        """Constructor method

        :param user: User name
        :param password: Password
        :param host: Host or domain
        :param db_name: DATABASE Name
        :param models: DATABASE models
        """
        self.__create_database(user, password, host, db_name, *models)
        self.user = user
        self.__password = password
        self.host = host
        self.db_name = db_name

    @staticmethod
    def create_connection(self, user: str, password: str, host: str, db_name: str, *models):
        """ create a database connection to a SQLite database

        :param user: User name
        :param password: Password
        :param host: Host or domain
        :param db_name: DATABASE Name
        :param models: DATABASE models
        """
        conn = None
        try:
            conn = sqlite3.connect(user=user, password=password, host=host)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    create_connection(r"sqlite_example.db")
