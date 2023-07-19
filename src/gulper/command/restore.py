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

from typing import Optional
from gulper.core import Restore
from gulper.module import success
from gulper.module import error


class RestoreCommand:
    """
    Restore Command
    """

    def __init__(self, restore: Restore):
        """
        Class Constructor

        Args:
            restore (Restore): The restore class instance
        """
        self._restore = restore
        self._restore.setup()

    def run(self, db_name: Optional[str], backup_id: Optional[str]):
        """
        Restore the database

        Args:
            db_name (str): The database name
            backup_id (str): The backup id
        """
        try:
            result = self._restore.run(db_name, backup_id)
        except Exception as e:
            error(str(e))

        if result:
            success("Database restore operation succeeded!")
        else:
            error("Database restore operation failed!")


def get_restore_command(restore: Restore) -> RestoreCommand:
    """
    Get an instance of restore command

    Args:
        restore (Restore): An instance of restore class

    Returns:
        RestoreCommand: an instance of restore command
    """
    return RestoreCommand(restore)
