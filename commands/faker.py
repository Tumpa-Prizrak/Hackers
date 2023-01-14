from typing import Any

import cmd_emul as cmd
from pprint import pprint
from utils.converter import convert_from
from utils.exceptions import ConvertError


def enter(data: dict):
    print("Welcome to faker!")
    print("Enter \"fake <key> <value>\" to change your data")
    print("Enter \"data\" to output all data")
    fake_data = deepcopy(data)
    while True:
        user_input = input("faker | " + cmd.get_prefix(fake_data)).split()
        user_input[1:] = convert_from(user_input[1:])
        for i in user_input:
            print(type(i), i)
        if user_input[0] == "exit":
            print("Exited faker. Your data has been returned to the normal state")
            return
        elif user_input[0] == "fake":
            replace_data(fake_data, user_input[1], user_input[2])
            continue
        elif user_input[0] == "data":
            pprint(fake_data)
            continue
        cmd.input_handler(" ".join(user_input), fake_data)


def replace_data(data: dict, link: str, value: Any):
    def get(d: dict | list, l: str, v: Any) -> None:
        parts = l.split(".")
        if len(parts) == 1:
            try:
                if isinstance(d, dict):
                    return d.update({parts[0]: v})
                else:
                    d[parts[0]] = v
                    return
            except AttributeError as e:
                raise ConvertError("Cannot get attribute") from e
        return get(d[int(parts[0])] if parts[0].isdigit() else d[parts[0]], ".".join(parts[1:]), v)
    get(data, link, value)


def deepcopy(data: dict):
    def change(part: Any):
        if isinstance(part, (list, tuple, set)):
            egg = []
            for i in part:
                egg.append(change(data))
            return egg
        elif isinstance(part, dict):
            egg = dict()
            for i in part:
                egg.update({i: change(part[i])})
            return egg
        else:
            try:
                return part.copy()
            except AttributeError:
                return part

    return change(data.copy())
