from cli import get_command


def enter(_: dict, command: str):
    """
    Get command info.
    """
    command_info = get_command(command)
    print(command_info.__doc__)
