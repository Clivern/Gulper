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

from typing import List, Any, Dict
import subprocess
import shlex


class MySQLClient:
    """
    A wrapper class for MySQL database operations, primarily focused on database dumping.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 3306,
        databases: List[str] = [],
    ):
        """
        Initialize the MySQL wrapper.

        Args:
            host (str): MySQL host
            username (str): MySQL username
            password (str): MySQL password
            port (int): MySQL port
            databases (List[str], optional): Optional MySQL database names. Defaults to all databases.
        """
        self._host: str = host
        self._username: str = username
        self._password: str = password
        self._port: int = port
        self._databases: List[str] = databases

    def dump(self, output_file: str, options: Dict[str, Any]) -> None:
        """
        Dump the MySQL database(s) using mysqldump.

        This method constructs and executes a mysqldump command to create a backup
        of the specified database(s). Additional options can be passed as keyword arguments.

        Args:
            output_file (str): Output file path where the dump will be saved.
            options (Dict[str, Any]): Additional options for mysqldump.
        """
        command = self._build_dump_command(output_file, options)
        self._execute_command(command)

    def _build_dump_command(self, output_file: str, options: Dict[str, Any]) -> str:
        """
        Build the mysqldump command with options.

        This method constructs the mysqldump command string based on the instance attributes
        and any additional options provided.

        Args:
            output_file (str): Output file path where the dump will be saved.
            options (Dict[str, Any]): Additional options for mysqldump.

        Returns:
            str: The complete mysqldump command string.

        Note:
            Boolean options are treated as flags (added if True).
            String options are added as key=value.
            List options are added as multiple instances of key=item.
        """
        command = f"mysqldump -h {self._host} -u {self._username} -P {self._port} -p{self._password}"

        if len(self._databases) > 0:
            dbs = " ".join(self._databases)
            command += f" --databases {dbs}"
        else:
            command += " --all-databases"

        for key, value in options.items():
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

    def _execute_command(self, command: str) -> None:
        """
        Execute a shell command.

        This method is responsible for executing the constructed mysqldump command.

        Args:
            command (str): Command string to execute
        """
        subprocess.check_call(shlex.split(command), shell=False)


def get_mysql_client(
    host: str, username: str, password: str, port: int = 3306, databases: List[str] = []
) -> MySQLClient:
    return MySQLClient(host, username, password, port, databases)
