'''
This class is intended to load store the test results in a SQLite database
The class should fullfil the following requirements:
    1. It should generate a unique DB (SQL lite) to store the test results of the project
        The name should follow the pattern: ProductID-TestLevel. e.g: OBCAMG-SW.6
    2. each test should have an unique row
    3. each test should have an unique column, one/SW release 
    4 the possible results of a test should be: PASS, FAIL, BLOCKED, NOT EXECUTED
    5. the class should provide a method to add a new test result to the database
    6. the class should provide a method to retrieve the test results of a specific test    
'''
import sqlite3
from pathlib import Path

class TestResults:
        def __init__(self, projectID, testLevel):
            self.__projectID = projectID
            self.__testLevel = testLevel
            self.__db_name = f"{self.__projectID}-{self.__testLevel}.sqlite"
            self.__db_path = Path(self.__db_name)
            self.__connection = sqlite3.connect(self.__db_path)
            self.__initialize_database()

        def __initialize_database(self):
            cursor = self.__connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS test_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id TEXT NOT NULL,
                    test_level TEXT NOT NULL,
                    test_name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    duration_ms REAL NOT NULL,
                    message TEXT
                )
                """
            )
            self.__connection.commit()

        def get_projectID(self):
            return self.__projectID

        def set_projectID(self, projectID):
            self.__projectID = projectID

        def get_testLevel(self):
            return self.__testLevel

        def set_testLevel(self, testLevel):
            self.__testLevel = testLevel

        def get_database_path(self):
            return str(self.__db_path)
    
