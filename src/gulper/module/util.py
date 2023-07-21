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

from typing import Dict, Any
from rich.console import Console
from rich.table import Table


def success(message: str):
    """
    Print a success message with green formatting.

    Args:
        message (str): The success message to be printed.
    """
    Console().print(f"[bold green][SUCCESS][/bold green] {message}")
    exit(0)


def error(message: str):
    """
    Print an error message with red formatting.

    Args:
        message (str): The error message to be printed.
    """
    Console().print(f"[bold red][ERROR][/bold red] {message}")
    exit(1)


def table(data: list[Dict[str, Any]]):
    """
    Print a tabular data

    Args:
        data (list[Dict[str, Any]]): The data to output
    """
    # Create a console object
    console = Console()

    # Create a table
    table = Table(title="Database Backups")

    # Add columns
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Database Name", style="magenta")
    table.add_column("Backups Available", justify="center", style="green")
    table.add_column("Created At", style="yellow")
    table.add_column("Updated At", style="yellow")

    # Add rows to the table
    for item in data:
        table.add_row(
            item["id"],
            item["dbIdent"],
            "Yes" if item["backups_exists"] else "No",
            item["createdAt"],
            item["updatedAt"],
        )

    console.print(table)
    exit(0)
