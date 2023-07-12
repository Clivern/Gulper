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

import os
import datetime
from .file_system import FileSystem


class LocalStorage:
    """
    Manages local file storage for backups
    """

    def __init__(self, base_path: str, file_system: FileSystem):
        """
        Initializes the LocalStorage instance with a base directory path.

        Args:
            base_path (str): The base directory path for file management.
            file_system (FileSystem): The file system object
        """
        self._base_path = base_path.rstrip("/")
        self._file_system = file_system

    def delete_old_files(self, days: int) -> int:
        """
        Deletes files older than the specified number of days within the base directory and its subdirectories.

        Args:
            days (int): The number of days; files older than this will be deleted.

        Returns:
            int: The number of files deleted.
        """
        now = datetime.datetime.now()
        deleted_files_count = 0

        for root, dirs, files in os.walk(self._base_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_modified = datetime.datetime.fromtimestamp(
                    os.path.getmtime(file_path)
                )
                if (now - file_modified).days > days:
                    os.remove(file_path)
                    deleted_files_count += 1

        return deleted_files_count

    def store_file(self, current_path: str, new_name: str):
        """
        Store backup file in the local storage

        Args:
            current_path (str): The current file path to backup
            new_name (str): The backup file name
        """
        self._file_system.backup(current_path, f"{self._base_path}/{new_name}")


class S3Storage:
    pass


def get_local_storage(base_path: str, file_system: FileSystem) -> LocalStorage:
    return LocalStorage(base_path, file_system)


def get_s3_storage() -> S3Storage:
    return S3Storage()
