import re
import requests
import shutil
import os

import internal.usecase.parser.s_constant
from internal.usecase.parser import EOP_FIELDS, RE_PATTERN_EOP
from internal.usecase.parser import SPACE_ENV_FIELDS, RE_PATTERN_SPACE_ENV
from internal.usecase.parser import C20_FIELDS, RE_PATTERN_C20
from internal.usecase.parser import RE_EOP_COMPILED, RE_SPACE_ENV_COMPILED, RE_C20_COMPILED


class InfoParser:
    """
    Class for parsing data from files and other file operations.
    """

    @staticmethod
    def parse(filename: str, d_type: int) -> list[dict]:
        """
        Parses the data from the file.
        Using the regular expression pattern,
        data is parsed and stored in a list of dictionaries.

        Args:
        filename: str - name of the file to parse
        d_type: int - data type

        Returns:
        list[dict] - list of parsed data
        """
        fields: list[str]
        re_pattern: str
        re_compiled: re.Pattern

        match d_type:
            case internal.usecase.parser.s_constant.D_TYPE_EOP:
                fields = EOP_FIELDS
                # re_pattern = RE_PATTERN_EOP
                re_compiled = RE_EOP_COMPILED
            case internal.usecase.parser.s_constant.D_TYPE_SPACE_ENV:
                fields = SPACE_ENV_FIELDS
                # re_pattern = RE_PATTERN_SPACE_ENV
                re_compiled = RE_SPACE_ENV_COMPILED
            case internal.usecase.parser.s_constant.D_TYPE_C20:
                fields = C20_FIELDS
                # re_pattern = RE_PATTERN_C20
                re_compiled = RE_C20_COMPILED
            case _:
                raise ValueError(f"Unknown data type: {d_type}")

        # re_compiled = re.compile(re_pattern)
        out = []
        with open(filename, 'r') as file:
            for line in file:
                match = re_compiled.match(line)
                if match:
                    values = match.groups()
                    parsed_data = dict(zip(fields, values))
                    parsed_data["d_type"] = d_type
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
