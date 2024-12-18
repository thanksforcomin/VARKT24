import json


class Logger:

    def __init__(self, file_name: str, mode: str = "w"):
        self.__memory = {}
        self.__file_name = file_name
        self.__mode = mode

    def insert(self, key, value) -> None:
        self.__memory[key] = value

    def dump(self):
        with open(self.__file_name, self.__mode) as file:
            json.dump(self.__memory, file, indent=2)
