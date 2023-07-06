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

import subprocess
import shlex


class MySQL:
    def __init__(self, host, username, password, database=None):
        """
        Initialize the MySQL wrapper.

        Args:
            host (str): MySQL host
            username (str): MySQL username
            password (str): MySQL password
            database (str, optional): Optional MySQL database name. Defaults to None.
        """
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def dump(self, output_file, **kwargs):
        """
        Dump the MySQL database using mysqldump.

        Args:
            output_file (str): Output file path
            **kwargs: Additional options for mysqldump
        """
        command = self._build_dump_command(output_file, **kwargs)
        self._execute_command(command)

    def _build_dump_command(self, output_file, **kwargs):
        """
        Build the mysqldump command with options.

        Args:
            output_file (str): Output file path
            **kwargs: Additional options for mysqldump
        Returns:
            str: mysqldump command string
        """
        command = f"mysqldump -h {self.host} -u {self.username} -p{self.password}"

        if self.database:
            command += f" {self.database}"

        for key, value in kwargs.items():
            if isinstance(value, bool):
                if value:
                    command += f" --{key}"
            elif isinstance(value, str):
                command += f" --{key}={value}"
            elif isinstance(value, list):
                for item in value:
                    command += f" --{key}={item}"

        command += f" > {output_file}"

        return command

    def _execute_command(self, command):
        """
        Execute a shell command.

        Args:
            command (str): Command string to execute
        """
        subprocess.check_call(shlex.split(command), shell=False)


def get_mysql_client(host: str, username: str, password: str, database=None) -> MySQL:
    return MySQL(host, username, password, database)
