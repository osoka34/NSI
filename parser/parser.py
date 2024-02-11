import re
import requests
import shutil


class InfoParser:
    def __init__(self, filename: str, fields: list[str], re_pattern: str, d_type: int):
        self.filename = filename
        self.fields = fields
        self.re_pattern = re_pattern
        self.re_compiled = re.compile(self.re_pattern)
        self.d_type = d_type

    def parse(self) -> list[dict]:
        out = []
        with open(self.filename, 'r') as file:
            for line in file:
                # print(line)
                match = self.re_compiled.match(line)
                if match:
                    values = match.groups()
                    parsed_data = dict(zip(self.fields, values))
                    parsed_data["d_type"] = self.d_type
                    out.append(parsed_data)
        return out

    @staticmethod
    def rename_file(old_name, new_name):
        try:
            shutil.move(old_name, new_name)
        except FileNotFoundError:
            print(f"File {old_name} not found.")
        except FileExistsError:
            print(f"File {new_name} already exists.")

    @staticmethod
    def download_from_web(url: str, save_path: str) -> None:
        try:
            response = requests.get(url, stream=True)
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        except Exception as e:
            print(f"Error occurred while downloading the file: {e}")
