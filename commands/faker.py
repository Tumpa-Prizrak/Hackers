import cmd_emul as cmd
from pprint import pprint

def enter(data: dict):
    print("Welcome to faker!")
    print("Enter \"fake <key> <value>\" to change your data")
    print("Enter \"data\" to output all data")
    fake_data = data.copy()
    while True:
        user_input = cmd.splitter(input("faker | " + cmd.get_prefix(fake_data)))
        if user_input[0] == "exit":
            print("Exited faker. Your data has been returned to the normal state")
            return
        elif user_input[0] == "fake":
            fake_data.update({user_input[1]: user_input[2]})
            continue
        elif user_input[0] == "data":
            pprint(fake_data)
            continue
        cmd.input_handler(" ".join(user_input), fake_data)
