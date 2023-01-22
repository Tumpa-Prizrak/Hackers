import runpy
from builtins import function

from utils.exceptions import exceptions_handler


def input_handler(command: str, global_data: dict) -> None:
    """
    Check if the command is valid and call the corresponding function.

    Parameters
    ----------
    command: str
        User input command.
    global_data: dict
        Global data of the application.

    Returns
    -------
    None
    """
    if command == "":
        return
    parts = command.split()
    try:
        get_command(parts[0])(global_data, *parts[1:])
    except Exception as e:
        exceptions_handler(e, parts)


def get_command(command: str) -> function:
    """
    Get the corresponding function of the command.

    Parameters
    ----------
    command: str
        User input command.

    Returns
    -------
    function
        Function corresponding to the command.
    """
    return runpy.run_path(f"commands\\{command.lower()}.py")["enter"]
