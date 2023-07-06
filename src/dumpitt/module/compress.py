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

import tarfile


class Compress:
    """Class to Compress and Extract .tar.gz files"""

    def compress_as_tar_gz(input_file: str, output_file: str):
        """
        Compresses a file into a tar.gz archive.

        Args:
            input_file (str): The path to the file to be compressed.
            output_file (str): The path where the compressed tar.gz file will be saved.

        Returns:
            None
        """
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(input_file)

    def extract_tar_gz(tar_file_path: str, extract_to: str):
        """
        Extracts the contents of a tar.gz file to a specified directory.

        Args:
            tar_file_path (str): The path to the tar.gz file to be extracted.
            extract_to (str): The directory where the contents will be extracted.

        Returns:
            None
        """
        with tarfile.open(tar_file_path, "r:gz") as tar:
            tar.extractall(extract_to)


def get_compress() -> Compress:
    """
    Get an instance of Compress class

    Returns:
        An instance of Compress class
    """
    return Compress()
