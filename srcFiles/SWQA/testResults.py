"""Store SWQA test results in a SQLite database.

1. The database filename is generated from the project ID and test level
using the pattern ``projectID-testLevel.sqlite``.

2. The database contains a table for each SW release under test. The pattern name will be SW<major.minor.patch>.<minor>.<patch>.<build>.

3. The table contains the following columns:
    - id: An auto-incrementing primary key.
    - test_name: The name of the test.
    - status: The result of the test (e.g., "PASS", "FAIL", "BLOCKED").
    - test_time_ms: The duration of the test in milliseconds.
    - comments: An optional message providing additional information about the test result.
""" 

import os
import sqlite3
from pathlib import Path
from functools import singledispatchmethod


class TestResults:
    """Provide persistence for software QA test results."""

    def __init__(self, projectID, testLevel, SWID):
        """Initialize the database and create the results table if needed.

        Args:
            projectID (str): Identifier for the project under test.
            testLevel (str): Test level identifier, for example "SW.6".
            SWID (str): Software identifier, for example "SW.major.minor.patch".
        """
        self.__projectID = projectID
        self.__testLevel = testLevel
        self.__SWID = SWID
        self.__db_name = f"{self.__projectID}-{self.__testLevel}.sqlite"
        self.__db_path = Path(self.__db_name)
        self.__connection = sqlite3.connect(self.__db_path)

        if os.path.exists(self.__db_path):
            print(
                f"Database {self.__db_name} already exists. "
                "Using existing database."
            )

        self.__initialize_database()

    def _quoted_table_name(self):
        """Return a SQLite-safe identifier for the SW release table."""
        return f'"{self.__SWID}"'

    def __initialize_database(self):
        """Create the test_results table ralated to the relese SWID if it does not already exist."""
        cursor = self.__connection.cursor()
        table_name = self._quoted_table_name()
        querry = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            test_id INTEGER PRIMARY KEY,
            test_name TEXT NOT NULL,
            test_result TEXT NOT NULL,
            test_time_ms REAL NOT NULL,
            comments TEXT
        )
        """
        cursor.execute(querry)
        self.__connection.commit()

    def get_projectID(self):
        """Return the project identifier.

        Returns:
            str: The project identifier.
        """
        return self.__projectID

    def set_projectID(self, projectID):
        """Set the project identifier.

        Args:
            projectID (str): New project identifier.
        """
        self.__projectID = projectID

    def get_testLevel(self):
        """Return the test level.

        Returns:
            str: The test level identifier.
        """
        return self.__testLevel

    def set_testLevel(self, testLevel):
        """Set the test level.

        Args:
            testLevel (str): New test level identifier.
        """
        self.__testLevel = testLevel

    def get_database_path(self):
        """Return the SQLite database file path.

        Returns:
            str: Path to the SQLite file.
        """
        return str(self.__db_path)
    def set_result(self, test_id, test_name, test_result, test_time_ms, comments=None):
        """Insert or update a test result in the database.

        Args:
            test_id (int): unique ID of the test.
            test_name (str): Name of the test.
            test_result (str): Test result, e.g., "PASS" or "FAIL".
            test_time_ms (float): Time taken for the test in milliseconds.
            comments (str, optional): Additional comments or error details.
        """
        cursor = self.__connection.cursor()
        table_name = self._quoted_table_name()
        querry = (
            f"INSERT INTO {table_name} (test_id, test_name, test_result, test_time_ms, comments) "
            "VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(test_id) DO UPDATE SET "
            "test_name = excluded.test_name, "
            "test_result = excluded.test_result, "
            "test_time_ms = excluded.test_time_ms, "
            "comments = excluded.comments"
        )
        cursor.execute(querry, (test_id, test_name, test_result, test_time_ms, comments))
        self.__connection.commit()
    @singledispatchmethod
    def fetchTestResults(self, testCaseNameOrId):
        """Fetch test results for a specific test case.

        Args:
            testCaseName (str): The name of the test case.
            testCaseId  (int): The unique identifier of the test case.
        Returns:
            list of tuples: Each tuple contains (test_id, test_name, test_result, test_time_ms, comments).
        """
        raise TypeError(f"Unsupported type: {type(testCaseNameOrId)}. Expected str or int.")
    @fetchTestResults.register
    def _(self, testCaseName: str):
        cursor = self.__connection.cursor()
        table_name = self._quoted_table_name()
        query = f"SELECT * FROM {table_name} WHERE test_name = ?"
        cursor.execute(query, (testCaseName,))
        return cursor.fetchone()
    @fetchTestResults.register
    def _(self, testCaseId: int):
        cursor = self.__connection.cursor()
        table_name = self._quoted_table_name()
        query = f"SELECT * FROM {table_name} WHERE test_id = ?"
        cursor.execute(query, (testCaseId,))
        return cursor.fetchone()

    def connection_close(self):
        """Close the database connection."""
        self.__connection.close()