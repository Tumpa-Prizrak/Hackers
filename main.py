import cmd_emul as cmd
import colorama

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

while True:
    cmd.input_handler(input(cmd.get_prefix(global_data)), global_data)
