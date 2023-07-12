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

from dumpitt.module import Config
from dumpitt.module import DatabaseClient
from dumpitt.module import Logger
from dumpitt.module import SQLiteClient
from dumpitt.module import LocalStorage


class Restore:
    """
    Restore Core Functionalities
    """

    def __init__(
        self,
        config: Config,
        db_client: DatabaseClient,
        logger: Logger,
        sqlite_client: SQLiteClient,
        local_storage: LocalStorage,
    ):
        self._config = config
        self._db_client = db_client
        self._logger = logger
        self._sqlite_client = sqlite_client
        self._local_storage = local_storage

    def setup(self):
        """
        Setup calls
        """
        self._logger.get_logger().info("Connect into the database")
        self._db_client.connect()
        self._logger.get_logger().info("Migrate the database tables")
        self._db_client.migrate()

    def restore(self, db_ident: str, backup_id: str) -> bool:
        """
        Restore a database from a backup

        Args:
            db_ident (str): The database Ident
            backup_id (str): The backup Id

        Returns:
            Whether the restore succeeded or not
        """
        pass
