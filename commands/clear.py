from os import system


def enter(_: dict):
    """
    Clears the terminal window.
    Usage: clear
    """
    if system("cls") == 1:
        system("clear")

