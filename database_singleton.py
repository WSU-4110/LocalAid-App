import mysql.connector

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new DB connection...")
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yourpassword",
                database="localaid"
            )
        return cls._instance

    def get_connection(self):
        return self.connection

# Example usage
if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print("Same instance:", db1 is db2)
