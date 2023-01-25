import cli
import colorama
from utils import user
from commands import exit
from FileManager import *

global_data = {
    "discord_id": 88504839439,
    "guild_id": 3485478403,
    "user": {
        "login": "anonymous"
    },
    "logged": False
}

colorama.init()
print(colorama.Fore.GREEN, end="")

if __name__ == "__main__":
    g = Directory("/")

    while True:
        try:
            cli.input_handler(input(user.get_prefix(global_data)), global_data)
        except KeyboardInterrupt:
            print()
            exit.enter(global_data)
