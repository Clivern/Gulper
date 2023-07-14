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

from gulper.module import Config
from gulper.module import State
from gulper.module import Logger
from gulper.module import SQLiteClient
from gulper.module import LocalStorage


class Restore:
    """
    Restore Core Functionalities
    """

    def __init__(
        self,
        config: Config,
        state: State,
        logger: Logger,
        sqlite_client: SQLiteClient,
        local_storage: LocalStorage,
    ):
        self._config = config
        self._state = state
        self._logger = logger
        self._sqlite_client = sqlite_client
        self._local_storage = local_storage

    def setup(self):
        """
        Setup calls
        """
        self._logger.get_logger().info("Connect into the state database")
        self._state.connect()
        self._logger.get_logger().info("Migrate the state database tables")
        self._state.migrate()

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
