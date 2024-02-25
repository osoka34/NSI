import re
import requests
import shutil
import os

import parser.s_constant
from parser.s_constant import D_TYPE_EOP, D_TYPE_SPACE_ENV, D_TYPE_C20
from parser.s_constant import EOP_FIELDS, RE_PATTERN_EOP
from parser.s_constant import SPACE_ENV_FIELDS, RE_PATTERN_SPACE_ENV
from parser.s_constant import C20_FIELDS, RE_PATTERN_C20


class InfoParser:
    """
    Class for parsing data from files.

    Attributes:
    fields: list[str] - fields of the data to be parsed
    re_pattern: str - regular expression pattern for parsing the data
    re_compiled: re.Pattern - compiled regular expression pattern
    d_type: int - data type

    """

    # filename: str
    fields: list[str]
    re_pattern: str
    re_compiled: re.Pattern

    def __init__(self, d_type: int):
        """
        Constructor for InfoParser class.

        Before using this class, you need to specify the data type.
        Here are the available data types:
        - D_TYPE_EOP
        - D_TYPE_SPACE_ENV
        - D_TYPE_C20

        Args:
        d_type: int - data type

        """
        match d_type:
            case parser.s_constant.D_TYPE_EOP:
                self.fields = EOP_FIELDS
                self.re_pattern = RE_PATTERN_EOP
            case parser.parser.D_TYPE_SPACE_ENV:
                self.fields = SPACE_ENV_FIELDS
                self.re_pattern = RE_PATTERN_SPACE_ENV
            case parser.s_constant.D_TYPE_C20:
                self.fields = C20_FIELDS
                self.re_pattern = RE_PATTERN_C20
            case _:
                raise ValueError(f"Unknown data type: {d_type}")
        self.d_type = d_type

    def parse(self, filename: str) -> list[dict]:
        """
        Parses the data from the file.
        Using the regular expression pattern,
        he data is parsed and stored in a list of dictionaries.

        Args:
        filename: str - name of the file to parse

        Returns:
        list[dict] - list of parsed data
        """
        self.re_compiled = re.compile(self.re_pattern)
        out = []
        with open(filename, 'r') as file:
            for line in file:
                match = self.re_compiled.match(line)
                if match:
                    values = match.groups()
                    parsed_data = dict(zip(self.fields, values))
                    parsed_data["d_type"] = self.d_type
                    out.append(parsed_data)
        return out

    @staticmethod
    def rename_file(old_name: str, new_name: str) -> None:
        """
        Renames the file.

        Args:
        old_name: str - old name of the file
        new_name: str - new name of the file

        """
        try:
            shutil.move(old_name, new_name)
        except FileNotFoundError:
            print(f"File {old_name} not found.")
        except FileExistsError:
            print(f"File {new_name} already exists.")

    @staticmethod
    def download_from_web(url: str, save_path: str) -> None:
        """
        Downloads a file from the web.
        Use requests library to download the file.

        Args:
        url: str - URL of the file to download
        save_path: str - path to save the file

        """
        try:
            response = requests.get(url, stream=True)
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        except Exception as e:
            print(f"Error occurred while downloading the file: {e}")

    @staticmethod
    def delete_dir(dir_to_delete: str) -> None:
        """
        Deletes the directory recursively.

        Args:
        dir_to_delete: str - directory to delete

        """
        try:
            shutil.rmtree(dir_to_delete)
        except Exception as e:
            print(f'Error occurred while deleting directory: {e}')

    @staticmethod
    def delete_file(file_to_delete: str) -> None:
        """
        Deletes the file if it exists.

        Args:
        file_to_delete: str - file to delete
        """
        try:
            os.remove(file_to_delete)
        except Exception as e:
            print(f'Error occurred while deleting file: {e}')
