# MIT License
#
# Copyright (c) 2025 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import uuid
import sqlite3
from typing import Dict, Any


class DatabaseClient:
    """A class to manage SQLite database operations."""

    def __init__(self, path: str):
        """Initialize the database with a file path.

        Args:
            path (str): Path to the SQLite database file.
        """
        self._path = path
        self._connection = None

    def connect(self) -> int:
        """Establish a connection to the SQLite database.

        Returns:
            int: The number of total changes to the database.
        """
        self._connection = sqlite3.connect(self._path)
        return self._connection.total_changes

    def migrate(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self._connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS backup (id TEXT, dbIdent TEXT, meta TEXT, lastStatus TEXT, lastBackupAt TEXT, createdAt TEXT, updatedAt TEXT)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS log (id TEXT, record TEXT, type TEXT, meta TEXT, createdAt TEXT, updatedAt TEXT)"
        )

        cursor.close()
        self._connection.commit()

    def insert_backup(self, backup: Dict[str, Any]) -> int:
        """Insert a new backup item

        Args:
            backup (Dict): The backup data

        Returns:
            The total rows inserted
        """
        cursor = self._connection.cursor()

        result = cursor.execute(
            "INSERT INTO backup VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now'))",
            (
                backup.get("id", str(uuid.uuid4())),
                backup.get("dbIdent"),
                backup.get("meta", "{}"),
                backup.get("lastStatus"),
                backup.get("lastBackupAt"),
            ),
        )

        cursor.close()

        self._connection.commit()

        return result.rowcount

    def insert_log(self, log: Dict[str, Any]) -> int:
        """Insert a new log record

        Args:
            log (Dict): The log data

        Returns:
            The total rows inserted
        """
        cursor = self._connection.cursor()

        result = cursor.execute(
            "INSERT INTO log VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))",
            (
                log.get("id", str(uuid.uuid4())),
                log.get("record"),
                log.get("type"),
                log.get("meta", "{}"),
            ),
        )

        cursor.close()

        self._connection.commit()

        return result.rowcount

    def delete_backup(self, id: str) -> None:
        """Delete a backup by its ID.

        Args:
            id (str): The ID of the backup to delete.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM backup WHERE id = ?", (id,))
        cursor.close()
        self._connection.commit()

    def delete_log(self, id: str) -> None:
        """Delete a log by its ID.

        Args:
            id (str): The ID of the log to delete.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM log WHERE id = ?", (id,))
        cursor.close()
        self._connection.commit()

    def get_backup_by_id(self, id: str) -> Dict[str, Any]:
        """Retrieve a backup by its ID.

        Args:
            id (str): The ID of the backup to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the backup details.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM backup WHERE id = ?", (id,))
        result = cursor.fetchone()
        cursor.close()

        return (
            dict(
                zip(
                    [
                        "id",
                        "dbIdent",
                        "meta",
                        "lastStatus",
                        "lastBackupAt",
                        "createdAt",
                        "updatedAt",
                    ],
                    result,
                )
            )
            if result
            else None
        )

    def get_log_by_id(self, id: str) -> Dict[str, Any]:
        """Retrieve a log by its ID.

        Args:
            id (str): The ID of the log to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the log details.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM log WHERE id = ?", (id,))
        result = cursor.fetchone()
        cursor.close()

        return (
            dict(
                zip(["id", "record", "type", "meta", "createdAt", "updatedAt"], result)
            )
            if result
            else None
        )


def get_database_client(path: str) -> DatabaseClient:
    """Create and return a Database instance.

    Args:
        path (str): SQLite database path.

    Returns:
        Database: Initialized Database client.
    """
    return DatabaseClient(path)
