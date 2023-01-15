import runpy
from sys import exit
from utils.exceptions import exceptions_handler


def input_handler(command: str, global_data: dict):
    if command == "":
        return
    parts = command.split()
    try:
        runpy.run_path(f"commands\\{parts[0].lower()}.py")["enter"](global_data, *parts[1:])
    except Exception as e:
        exceptions_handler(e, parts)
